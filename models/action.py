from typing import List

class ActionTypes:
    """Constants for action types"""
    GOAL = "Goal"
    YELLOW_CARD = "Yellow Card"
    RED_CARD = "Red Card"
    SUBSTITUTION = "Substitution"
    PENALTY = "Penalty"
    FREE_KICK = "Free Kick"
    CORNER = "Corner"
    OFFSIDE = "Offside"
    FOUL = "Foul"
    INJURY = "Injury"
    SHOT_ON_TARGET = "Shot on Target"
    SHOT_OFF_TARGET = "Shot off Target"
    SAVE = "Save"
    CROSS = "Cross"
    TACKLE = "Tackle"
    INTERCEPTION = "Interception"
    
    @classmethod
    def get_all(cls) -> List[str]:
        return [
            cls.GOAL, cls.YELLOW_CARD, cls.RED_CARD, cls.SUBSTITUTION,
            cls.PENALTY, cls.FREE_KICK, cls.CORNER, cls.OFFSIDE,
            cls.FOUL, cls.INJURY, cls.SHOT_ON_TARGET, cls.SHOT_OFF_TARGET,
            cls.SAVE, cls.CROSS, cls.TACKLE, cls.INTERCEPTION
        ]

class PlayerPositions:
    """Constants for player positions"""
    GOALKEEPER = "Goalkeeper"
    DEFENDER = "Defender"
    MIDFIELDER = "Midfielder"
    FORWARD = "Forward"
    
    @classmethod
    def get_all(cls) -> List[str]:
        return [cls.GOALKEEPER, cls.DEFENDER, cls.MIDFIELDER, cls.FORWARD]