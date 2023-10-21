import logging

###########################################################
# BATTLE LOGGERS
###########################################################


def log_battle_teams(team_1: "Team", team_2: "Team") -> None:
    """
    Log the teams participating in the battle.

    Args:
        team_1: The first team.
        team_2: The second team.

    Returns:
        None.
    """
    logging.info(f"{team_1.name.upper()} v/s {team_2.name.upper()}")


def log_battle_winner(
    winner_team: "Team",
) -> None:
    """
        Log the winner of the battle.
        Args:
            winner_team: The winning team.

    Returns:
        None.

    """
    logging.info(f"GANADOR: {winner_team.name.upper()}")


def log_round_results(
    round_details: str,
    attacking_character: "Character",
) -> None:
    """
    Log the results of a round.

    Args:
        round_details: The details of the round.
        attacking_character: The attacking character.

    Returns:
        None.

    """
    logging.info(f"{round_details} - GANADOR: {attacking_character.name}")
