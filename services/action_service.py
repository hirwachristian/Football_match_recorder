from typing import List
from datetime import datetime
from models.match import Match
from models.action import ActionTypes
from utils.helpers import get_action_icon

class ActionService:
    def __init__(self):
        self.action_types = ActionTypes.get_all()
    
    def record_action(self, matches: List[Match]):
        """Record an action in a match"""
        print("\n--- Record Match Action ---")
        
        active_matches = [m for m in matches if m.status == 'in_progress']
        if not active_matches:
            print("❌ No active matches. Please start a match first.")
            return
        
        print("Active matches:")
        for match in active_matches:
            print(f"{match.id}. {match.home_team.name} vs {match.away_team.name}")
        
        try:
            match_id = int(input("Enter match ID: "))
            match = next((m for m in active_matches if m.id == match_id), None)
            
            if not match:
                print("❌ Invalid match ID!")
                return
            
            print(f"\nRecording action for: {match.home_team.name} vs {match.away_team.name}")
            
            # Select team
            print(f"1. {match.home_team.name} (Home)")
            print(f"2. {match.away_team.name} (Away)")
            team_choice = input("Select team (1 or 2): ").strip()
            
            if team_choice == '1':
                team = match.home_team
                team_type = "home"
            elif team_choice == '2':
                team = match.away_team
                team_type = "away"
            else:
                print("❌ Invalid choice!")
                return
            
            # Select player
            print(f"\nPlayers from {team.name}:")
            for player in team.players:
                print(f"- {player.name} ({player.position}) - #{player.jersey_number}")
            
            player_name = input("Enter player name: ").strip()
            player = next((p for p in team.players if p.name.lower() == player_name.lower()), None)
            
            if not player:
                print("❌ Player not found!")
                return
            
            # Select action type
            print("\nAction types:")
            for i, action_type in enumerate(self.action_types, 1):
                print(f"{i}. {action_type}")
            
            try:
                action_choice = int(input("Select action type (number): "))
                if 1 <= action_choice <= len(self.action_types):
                    action_type = self.action_types[action_choice - 1]
                else:
                    print("❌ Invalid action type!")
                    return
            except ValueError:
                print("❌ Invalid input!")
                return
            
            minute = input("Enter minute of action: ").strip()
            description = input("Enter additional description (optional): ").strip()
            
            action = {
                "id": len(match.actions) + 1,
                "minute": minute,
                "team": team.name,
                "player": player.name,
                "action_type": action_type,
                "description": description,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            match.add_action(action)
            
            print(f"✅ Action recorded: {player.name} - {action_type} at {minute}'")
            
        except ValueError:
            print("❌ Invalid input!")