import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import json
import matplotlib.pyplot as plt
import os.path

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
font = cv2.FONT_HERSHEY_PLAIN

matches_read = set()

filename = "match_results.txt"

while True:
    _, frame = cap.read()
    
    decodedObjects = pyzbar.decode(frame, symbols=[pyzbar.ZBarSymbol.QRCODE])
    for obj in decodedObjects:
        if obj.data == None: continue
        if isinstance(json.loads(obj.data), int): continue 

        if obj.data not in matches_read:    
            thing_to_write = str(obj.data)[2:-1]
            print(thing_to_write)
            matches_read.add(obj.data)

            with open(filename, "a+") as f:
                f.write(thing_to_write + "\n")     

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 13:
        break

cv2.destroyAllWindows()