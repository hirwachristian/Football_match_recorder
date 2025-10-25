from typing import List, Dict, Any
from datetime import datetime
from models.team import Team

class Match:
    def __init__(self, match_id: int, home_team: Team, away_team: Team, stadium: str, date: str):
        self.id = match_id
        self.home_team = home_team
        self.away_team = away_team
        self.stadium = stadium
        self.date = date
        self.status = "scheduled"  # scheduled, in_progress, completed
        self.score = {"home": 0, "away": 0}
        self.actions: List[Dict[str, Any]] = []
        self.start_time = None
        self.end_time = None
    
    def start(self):
        self.status = "in_progress"
        self.start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def end(self):
        self.status = "completed"
        self.end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def add_action(self, action: Dict[str, Any]):
        self.actions.append(action)
        # Update score for goals
        if action["action_type"] == "Goal":
            if action["team"] == self.home_team.name:
                self.score["home"] += 1
            else:
                self.score["away"] += 1
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "home_team": self.home_team.to_dict(),
            "away_team": self.away_team.to_dict(),
            "stadium": self.stadium,
            "date": self.date,
            "status": self.status,
            "score": self.score,
            "actions": self.actions,
            "start_time": self.start_time,
            "end_time": self.end_time
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Match':
        match = cls(
            match_id=data["id"],
            home_team=Team.from_dict(data["home_team"]),
            away_team=Team.from_dict(data["away_team"]),
            stadium=data["stadium"],
            date=data["date"]
        )
        match.status = data["status"]
        match.score = data["score"]
        match.actions = data["actions"]
        match.start_time = data.get("start_time")
        match.end_time = data.get("end_time")
        return match