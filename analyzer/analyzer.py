from util import TeamResult, Result
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from collections import OrderedDict
from sys import exit
from random import randint, choice
import json
from math import floor

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
    stats = OrderedDict(sorted(team_stats.items(), key=lambda item: item[1][1]))

    teams = list(stats.keys())
    team_range = np.arange(len(teams))

    min_scores = list(map(lambda t: stats[t][0], stats))
    mean_scores = list(map(lambda t: stats[t][1], stats))
    max_scores = list(map(lambda t: stats[t][2], stats))

    fig, ax = plt.subplots(figsize=(10,6))
    plt.subplots_adjust(bottom=0.25)

    bar_width = 0.25
    opacity = 0.8

    bar_max = plt.barh(team_range + bar_width*2, max_scores, bar_width,
        alpha=opacity,
        color='g',
        label='Max Score',
        align='edge')

    bar_mean = plt.barh(team_range + bar_width, mean_scores, bar_width,
        alpha=opacity,
        color='xkcd:royal blue',
        label='Mean Score',
        align='edge')

    bar_min = plt.barh(team_range, min_scores, bar_width,
        alpha=opacity,
        color='r',
        label='Minimum Score',
        align='edge')

    plt.tight_layout()

    plt.yticks(team_range + bar_width*1.5, teams)
    
    plt.ylabel('Team Number')
    plt.xlabel('Score')

    plt.title("Score Results")

    plt.legend(loc="lower right")

    plt.subplots_adjust(bottom=0.25)

    plt.axis([0, 10, -1, 1])

    axcolor = 'lightgoldenrodyellow'
    axpos = plt.axes([0.2, 0.1, 0.65, 0.03])

    amount_to_show = 10
    max_scroll = len(team_range)-amount_to_show

    class DiscreteSlider(Slider):
        """A matplotlib slider widget with discrete steps."""
        def __init__(self, *args, **kwargs):
            """Identical to Slider.__init__, except for the "increment" kwarg.
            "increment" specifies the step size that the slider will be discritized
            to."""
            self.inc = kwargs.pop('increment', 0.5)
            Slider.__init__(self, *args, **kwargs)

        def set_val(self, val):
            discrete_val = int(val / self.inc) * self.inc
            # We can't just call Slider.set_val(self, discrete_val), because this 
            # will prevent the slider from updating properly (it will get stuck at
            # the first step and not "slide"). Instead, we'll keep track of the
            # the continuous value as self.val and pass in the discrete value to
            # everything else.
            xy = self.poly.xy
            xy[2] = discrete_val, 1
            xy[3] = discrete_val, 0
            self.poly.xy = xy
            self.valtext.set_text(self.valfmt % discrete_val)
            if self.drawon: 
                self.ax.figure.canvas.draw()
            self.val = val
            if not self.eventson: 
                return
            for cid, func in self.observers.items():
                func(discrete_val)

    spos = DiscreteSlider(axpos, 'Quality', 0.0, max_scroll, valinit=max_scroll, increment=amount_to_show)

    def update(val):
        pos = floor(spos.val/amount_to_show)*amount_to_show
        ax.axis([0,max(max_scores),pos,pos+amount_to_show])
        fig.canvas.draw_idle()

    spos.on_changed(update)

    update(max_scroll)

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