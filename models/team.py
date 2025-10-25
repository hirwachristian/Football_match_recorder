from typing import List, Dict, Any

class Player:
    def __init__(self, name: str, position: str, jersey_number: str):
        self.name = name
        self.position = position
        self.jersey_number = jersey_number
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "position": self.position,
            "jersey_number": self.jersey_number
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Player':
        return cls(
            name=data["name"],
            position=data["position"],
            jersey_number=data["jersey_number"]
        )

class Team:
    def __init__(self, team_id: int, name: str, country: str):
        self.id = team_id
        self.name = name
        self.country = country
        self.players: List[Player] = []
    
    def add_player(self, player: Player):
        self.players.append(player)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "country": self.country,
            "players": [player.to_dict() for player in self.players]
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Team':
        team = cls(
            team_id=data["id"],
            name=data["name"],
            country=data["country"]
        )
        for player_data in data.get("players", []):
            team.add_player(Player.from_dict(player_data))
        return team