from models.match import Match

def get_action_icon(action_type: str) -> str:
    """Get emoji icon for action type"""
    icons = {
        "Goal": "⚽",
        "Yellow Card": "🟨",
        "Red Card": "🟥",
        "Substitution": "🔄",
        "Penalty": "🎯",
        "Free Kick": "📏",
        "Corner": "↩️",
        "Offside": "🚫",
        "Foul": "💥",
        "Injury": "🏥",
        "Shot on Target": "🎯",
        "Shot off Target": "❌",
        "Save": "✋",
        "Cross": "↗️",
        "Tackle": "⚔️",
        "Interception": "🛑"
    }
    return icons.get(action_type, "📝")

def display_match_details(match: Match):
    """Display detailed match information"""
    print("\n" + "="*60)
    print(f"MATCH DETAILS")
    print("="*60)
    print(f"🏟️  {match.home_team.name} vs {match.away_team.name}")
    print(f"📅 Date: {match.date}")
    print(f"🏟️  Stadium: {match.stadium}")
    print(f"📊 Status: {match.status.upper()}")
    
    score = match.score
    print(f"📊 SCORE: {match.home_team.name} {score['home']} - {score['away']} {match.away_team.name}")
    print("="*60)
    
    if match.actions:
        print("ACTIONS TIMELINE:")
        print("-" * 60)
        for action in sorted(match.actions, key=lambda x: x['minute']):
            icon = get_action_icon(action['action_type'])
            print(f"{action['minute']}' {icon} {action['team']} - {action['player']}: {action['action_type']}")
            if action['description']:
                print(f"   📝 {action['description']}")
    else:
        print("No actions recorded yet.")
    
    print("="*60)