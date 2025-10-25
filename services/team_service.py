from typing import List
from models.team import Team, Player
from models.action import PlayerPositions
from services.data_service import DataService

class TeamService:
    def __init__(self):
        self.data_service = DataService()
        self.teams = self.load_teams()
    
    def load_teams(self) -> List[Team]:
        """Load teams from storage"""
        teams_data = self.data_service.load_data("teams.json")
        return [Team.from_dict(team_data) for team_data in teams_data]
    
    def save_teams(self):
        """Save teams to storage"""
        teams_data = [team.to_dict() for team in self.teams]
        self.data_service.save_data(teams_data, "teams.json")
    
    def add_team(self):
        """Add a new team to the database"""
        print("\n--- Add New Team ---")
        team_name = input("Enter team name: ").strip()
        country = input("Enter country: ").strip()
        
        # Check if team already exists
        for team in self.teams:
            if team.name.lower() == team_name.lower():
                print("❌ Team already exists!")
                return
        
        team = Team(
            team_id=len(self.teams) + 1,
            name=team_name,
            country=country
        )
        
        # Add players
        print("\nAdd players to the team (enter 'done' when finished):")
        while True:
            player_name = input("Enter player name (or 'done' to finish): ").strip()
            if player_name.lower() == 'done':
                break
            
            print("Available positions:", ", ".join(PlayerPositions.get_all()))
            position = input("Enter player position: ").strip()
            jersey_number = input("Enter jersey number: ").strip()
            
            player = Player(
                name=player_name,
                position=position,
                jersey_number=jersey_number
            )
            team.add_player(player)
            print(f"✅ Player {player_name} added!")
        
        self.teams.append(team)
        self.save_teams()
        print(f"✅ Team {team_name} added successfully!")
    
    def view_teams(self):
        """View all teams and their players"""
        print("\n--- Teams ---")
        
        if not self.teams:
            print("❌ No teams available.")
            return
        
        for team in self.teams:
            print(f"\n{team.name} ({team.country})")
            print("Players:")
            for player in team.players:
                print(f"  #{player.jersey_number} {player.name} - {player.position}")
            print("-" * 40)
    
    def get_team_by_id(self, team_id: int) -> Team:
        """Get team by ID"""
        for team in self.teams:
            if team.id == team_id:
                return team
        return None