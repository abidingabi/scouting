import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import json
import matplotlib.pyplot as plt
import os.path

from analyzer import analyze, draw
from util import Result

def print_result(result):
    name = "Match Read: " + str(result.match_num) + " - " + result.color
    print(name + ": " + str(result.team1.num) + " Score: " + str(result.team1.score()) + ", " + str(result.team2.num) + " Score: " + str(result.team2.score()))


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
font = cv2.FONT_HERSHEY_PLAIN

registered_results = set()
printed_names = set()

filename = "match_results.txt"

if os.path.isfile(filename): 
    if input("Use existing match results? y/n: ").lower() == "y":
        with open(filename) as f:
            for line in f:
                result = Result(line)
                print_result(result)
                registered_results.add(result)

while True:
    _, frame = cap.read()
    
    decodedObjects = pyzbar.decode(frame, symbols=[pyzbar.ZBarSymbol.QRCODE])
    for obj in decodedObjects:
        if obj.data == None: continue
        if isinstance(json.loads(obj.data), int): continue 

        result = Result(obj.data)

        registered_results.add(result)

        if result.color == "red":
            cv2.putText(frame, "Match #" + str(result.match_num), (50, 50), font, 2, (0, 0, 255), 3)
        elif result.color == "blue":
            cv2.putText(frame, "Match #" + str(result.match_num), (50, 50), font, 2, (255, 0, 0), 3)

        name = "Match Read: " + str(result.match_num) + " - " + result.color

        if name not in printed_names:
            printed_names.add(name)
            print_result(result)
            with open(filename, "a+") as f:
            f.write(str(obj.data)[2:-1] + "\n")

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 13:
        break

cv2.destroyAllWindows()

stats = analyze(registered_results)
draw(stats)