import csv
import random

filename = "fake_match_results.csv"
team_count = 80
match_count = 180   

teams = set()

while len(teams) != team_count:
    teams = set(random.randrange(1,15000) for i in range(team_count))

alliances = []

for i in range(match_count):
    selected_teams = set()

    while len(selected_teams) != 4:
        selected_teams = [random.sample(teams, 1)[0] for i in range(4)]
        
        alliances.append(selected_teams[:2])         
        alliances.append(selected_teams[2:])

with open(filename, "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        'matchNum', 
        'allianceColor', 
        'tallestSkyscraper',
        'teamNum',
        'skystonesDelivered',
        'autoStonesDelivered',
        'autoStonesPlaced',
        'foundationRepositioned',
        'navigated',
        'stonesDelivered',
        'stonesPlaced',
        'capped',
        'capstoneHeight',
        'foundationMoved',
        'parked',
        'teamNum2',
        'skystonesDelivered2',
        'autoStonesDelivered2',
        'autoStonesPlaced2',
        'foundationRepositioned2',
        'navigated2',
        'stonesDelivered2',
        'stonesPlaced2',
        'capped2',
        'capstoneHeight2',
        'foundationMoved2',
        'parked2'])


    for i, alliance in enumerate(alliances):                
        fields = [
            int((i+2)/2), 
            random.choice(['blue', 'red']), 
            random.randrange(0,10), 
            alliance[0], 
            random.randrange(0,2),
            random.randrange(0,6),
            random.randrange(0,4),
            random.choice([True, False]),
            random.choice([True, False]),
            random.randrange(0,20),
            random.randrange(0,20),
            random.choice([True, False]),
            random.randrange(0,10),
            random.choice([True, False]),
            random.choice([True, False]),
            alliance[1], 
            random.randrange(0,2),
            random.randrange(0,6),
            random.randrange(0,4),
            random.choice([True, False]),
            random.choice([True, False]),
            random.randrange(0,20),
            random.randrange(0,20),
            random.choice([True, False]),
            random.randrange(0,10),
            random.choice([True, False]),
            random.choice([True, False])
        ]

        writer.writerow(fields)