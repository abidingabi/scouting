import json

class TeamResult:
    def __init__(self, team_content):
        self.num = team_content["num"]
        
        self.auto_land = team_content["auto"]["land"]
        self.auto_sample = team_content["auto"]["sample"]
        self.auto_claim = team_content["auto"]["claim"]
        self.auto_park = team_content["auto"]["park"]

        self.cargo_hold_minerals = int(team_content["teleOp"]["cargoHoldMinerals"])
        self.depot_minerals = int(team_content["teleOp"]["depotHoldMinerals"])

        self.endgame_state = team_content["endgame"]["endgameState"]

    def score(self):
        return self.auto_score() + self.teleop_score() + self.endgame_score()

    def auto_score(self):
        score = 0
        if self.auto_land: score += 30
        if self.auto_sample: score += 25
        if self.auto_claim: score += 15
        if self.auto_park: score += 10
        
        return score
        
    def teleop_score(self):
        score = 0
        score += self.cargo_hold_minerals * 5
        score += self.depot_minerals * 2
        
        return score
        
    def endgame_score(self):
        if self.endgame_state == "hang":
            return 50
        elif self.endgame_state == "partialPark":
            return 15
        elif self.endgame_state == "fullPark":
            return 25
        return 0

class Result:
    def __init__(self, json_string):
        result = json.loads(json_string)
        self.match_num = int(result["matchNum"]) 
        self.color = str(result["allianceColor"])
        self.team1 = TeamResult(result["team1"])
        self.team2 = TeamResult(result["team2"])
