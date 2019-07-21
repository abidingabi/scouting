from util import TeamResult, Result
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict
from sys import exit
from random import randint, choice
import json

def analyze(results):
    teams = {}

    for result in results:
        if result.team1.num in teams:
            teams[result.team1.num].append(result.team1)
        else:
            teams[result.team1.num] = [result.team1]
    
        if result.team2.num in teams:
            teams[result.team2.num].append(result.team2)
        else:
            teams[result.team2.num] = [result.team2]

    team_stats = {}

    for team in teams:
        scores = list(map(lambda t: t.score(), teams[team]))
        
        team_stats[team] = (min(scores), np.mean(scores), max(scores))

    return team_stats

def draw(team_stats):
    if len(team_stats) == 0: exit("draw called with no data; exiting")
    stats = OrderedDict(sorted(team_stats.items(), key=lambda item: item[1][1], reverse=True))

    teams = list(stats.keys())
    team_range = np.arange(len(teams))

    min_scores = list(map(lambda t: stats[t][0], stats))
    mean_scores = list(map(lambda t: stats[t][1], stats))
    max_scores = list(map(lambda t: stats[t][2], stats))

    plt.bar(team_range, max_scores, label='Maximum Score', color='xkcd:green')
    plt.bar(team_range, mean_scores, label='Mean Score', color='xkcd:baby blue')
    plt.bar(team_range, min_scores, label='Minimum Score', color='xkcd:red')

    plt.xticks(team_range, teams)
    
    plt.xlabel('Team')
    plt.ylabel('Score')

    plt.title("Score Results")

    plt.legend()

    plt.show()

def gen_random_json():
    return json.dumps(
        {
            "matchNum": randint(1, 180),
            "allianceColor": choice(["red", "blue"]),
            "team1": {
                "num": randint(1,90),
                "auto": {
                    "land": choice([True, False]),
                    "sample": choice([True, False]),
                    "claim": choice([True, False]),
                    "park": choice([True, False])
                },
                "teleOp": {
                    "cargoHoldMinerals": randint(1, 60),
                    "depotHoldMinerals": randint(1, 10)
                },
                "endgame": {
                    "endgameState": choice(["hang, partialPark, fullPark. none"])
                }
            },
            "team2": {
                "num": randint(1,90),
                "auto": {
                    "land": choice([True, False]),
                    "sample": choice([True, False]),
                    "claim": choice([True, False]),
                    "park": choice([True, False])
                },
                "teleOp": {
                    "cargoHoldMinerals": randint(1, 60),
                    "depotHoldMinerals": randint(1, 10)
                },
                "endgame": {
                    "endgameState": choice(["hang", "partialPark", "fullPark", "none"])
                }
            }
        }
    )

if __name__ == "__main__":
    results = set()
    
    for i in range(360):
        results.add(Result(gen_random_json()))

    team_stats = analyze(results)
    draw(team_stats)