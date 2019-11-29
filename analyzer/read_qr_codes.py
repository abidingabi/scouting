import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import json
import csv
import matplotlib.pyplot as plt
import os.path

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
font = cv2.FONT_HERSHEY_PLAIN

matches_read = set()

filename = "match_results.csv"

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

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 13:
        break

cv2.destroyAllWindows()

with open(filename, "a") as csvfile:
    writer = csv.writer(csvfile)
    
    for data in matches_read:
        match = json.loads(data)
        
        fields = [
            match['matchNum'], 
            match['allianceColor'], 
            match['tallestSkyscraper'], 
            match['team1']['num'], 
            match['team1']['auto']['skystonesDelivered'],
            match['team1']['auto']['stonesDelivered'],
            match['team1']['auto']['stonesPlaced'],
            match['team1']['auto']['foundationRepositioned'],
            match['team1']['auto']['navigated'],
            match['team1']['teleOp']['stonesDelivered'],
            match['team1']['teleOp']['stonesPlaced'],
            match['team1']['endgame']['capped'],
            match['team1']['endgame']['capstoneHeight'],
            match['team1']['endgame']['foundationMoved'],
            match['team1']['endgame']['parked'],
            match['team2']['num'], 
            match['team2']['auto']['skystonesDelivered'],
            match['team2']['auto']['stonesDelivered'],
            match['team2']['auto']['stonesPlaced'],
            match['team2']['auto']['foundationRepositioned'],
            match['team2']['auto']['navigated'],
            match['team2']['teleOp']['stonesDelivered'],
            match['team2']['teleOp']['stonesPlaced'],
            match['team2']['endgame']['capped'],
            match['team2']['endgame']['capstoneHeight'],
            match['team2']['endgame']['foundationMoved'],
            match['team2']['endgame']['parked']
        ]

        writer.writerow(fields)