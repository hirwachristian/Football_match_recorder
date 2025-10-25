from typing import List
from models.match import Match
from models.team import Team
from services.data_service import DataService
from utils.helpers import display_match_details

class MatchService:
    def __init__(self):
        self.data_service = DataService()
        self.matches = self.load_matches()
    
    def load_matches(self) -> List[Match]:
        """Load matches from storage"""
        matches_data = self.data_service.load_data("matches.json")
        return [Match.from_dict(match_data) for match_data in matches_data]
    
    def save_matches(self):
        """Save matches to storage"""
        matches_data = [match.to_dict() for match in self.matches]
        self.data_service.save_data(matches_data, "matches.json")
    
    def create_match(self, teams: List[Team]):
        """Create a new match"""
        print("\n--- Create New Match ---")
        
        if not teams:
            print("❌ No teams available. Please add teams first.")
            return
        
        print("Available teams:")
        for team in teams:
            print(f"{team.id}. {team.name} ({team.country})")
        
        try:
            team1_id = int(input("Enter home team ID: "))
            team2_id = int(input("Enter away team ID: "))
            
            # Find teams
            team1 = next((t for t in teams if t.id == team1_id), None)
            team2 = next((t for t in teams if t.id == team2_id), None)
            
            if not team1 or not team2:
                print("❌ Invalid team ID!")
                return
            
            stadium = input("Enter stadium: ").strip()
            date = input("Enter match date (YYYY-MM-DD): ").strip()
            
            match = Match(
                match_id=len(self.matches) + 1,
                home_team=team1,
                away_team=team2,
                stadium=stadium,
                date=date
            )
            
            self.matches.append(match)
            self.save_matches()
            print(f"✅ Match created: {team1.name} vs {team2.name}")
            
        except ValueError:
            print("❌ Invalid input!")
    
    def start_match(self):
        """Start a scheduled match"""
        print("\n--- Start Match ---")
        
        scheduled_matches = [m for m in self.matches if m.status == 'scheduled']
        if not scheduled_matches:
            print("❌ No scheduled matches.")
            return
        
        print("Scheduled matches:")
        for match in scheduled_matches:
            print(f"{match.id}. {match.home_team.name} vs {match.away_team.name} - {match.date}")
        
        try:
            match_id = int(input("Enter match ID to start: "))
            match = next((m for m in scheduled_matches if m.id == match_id), None)
            
            if match:
                match.start()
                self.save_matches()
                print(f"✅ Match started: {match.home_team.name} vs {match.away_team.name}")
            else:
                print("❌ Match not found!")
                
        except ValueError:
            print("❌ Invalid input!")
    
    def end_match(self):
        """End an ongoing match"""
        print("\n--- End Match ---")
        
        active_matches = [m for m in self.matches if m.status == 'in_progress']
        if not active_matches:
            print("❌ No active matches.")
            return
        
        print("Active matches:")
        for match in active_matches:
            score = match.score
            print(f"{match.id}. {match.home_team.name} {score['home']}-{score['away']} {match.away_team.name}")
        
        try:
            match_id = int(input("Enter match ID to end: "))
            match = next((m for m in active_matches if m.id == match_id), None)
            
            if match:
                match.end()
                self.save_matches()
                
                score = match.score
                print(f"✅ Match ended: {match.home_team.name} {score['home']}-{score['away']} {match.away_team.name}")
                
                # Determine result
                if score['home'] > score['away']:
                    winner = match.home_team.name
                elif score['away'] > score['home']:
                    winner = match.away_team.name
                else:
                    winner = "Draw"
                
                print(f"🏆 Result: {winner}")
            else:
                print("❌ Match not found!")
                
        except ValueError:
            print("❌ Invalid input!")
    
    def view_match_details(self):
        """View detailed information about a match"""
        print("\n--- Match Details ---")
        
        if not self.matches:
            print("❌ No matches available.")
            return
        
        print("All matches:")
        for match in self.matches:
            status_icon = "⏳" if match.status == 'scheduled' else "⚽" if match.status == 'in_progress' else "✅"
            score = match.score
            print(f"{match.id}. {status_icon} {match.home_team.name} {score['home']}-{score['away']} {match.away_team.name} - {match.date}")
        
        try:
            match_id = int(input("Enter match ID to view details: "))
            match = next((m for m in self.matches if m.id == match_id), None)
            
            if match:
                display_match_details(match)
            else:
                print("❌ Match not found!")
                
        except ValueError:
            print("❌ Invalid input!")
    
    def get_active_matches(self) -> List[Match]:
        """Get all active matches"""
        return [m for m in self.matches if m.status == 'in_progress']