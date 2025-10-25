from services.team_service import TeamService
from services.match_service import MatchService
from services.action_service import ActionService

def display_main_menu():
    """Display the main menu"""
    print("\n" + "="*60)
    print("🏆 FOOTBALL WORLD CUP MATCH RECORDER")
    print("="*60)
    print("1. Add Team")
    print("2. Create Match")
    print("3. Start Match")
    print("4. Record Action")
    print("5. End Match")
    print("6. View Match Details")
    print("7. View Teams")
    print("8. Exit")
    print("="*60)

def main():
    team_service = TeamService()
    match_service = MatchService()
    action_service = ActionService()
    
    while True:
        display_main_menu()
        
        try:
            choice = input("\nEnter your choice (1-8): ").strip()
            
            if choice == '1':
                team_service.add_team()
            elif choice == '2':
                match_service.create_match(team_service.teams)
            elif choice == '3':
                match_service.start_match()
            elif choice == '4':
                action_service.record_action(match_service.matches)
            elif choice == '5':
                match_service.end_match()
            elif choice == '6':
                match_service.view_match_details()
            elif choice == '7':
                team_service.view_teams()
            elif choice == '8':
                print("👋 Thank you for using Football Match Recorder! Goodbye! 🏆")
                break
            else:
                print("❌ Invalid choice. Please enter a number between 1-8.")
        
        except KeyboardInterrupt:
            print("\n👋 Program interrupted. Goodbye! 🏆")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()