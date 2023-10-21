import re
from typing import List, Tuple

###########################################################
# LOG EXTRACTORS
###########################################################


def extract_team_names(
    log_content: List[str],
) -> Tuple[str, str]:
    """
    Extract the team names from the battle log content.

    Args:
        log_content: The content of the battle log.

    Returns:
        Tuple[str, str]: The names of the two teams.
    """
    team_line = log_content[0].strip()
    team_1, team_2 = re.findall(r"TEAM (\d+)", team_line)
    return team_1, team_2


def extract_round_details(
    log_content: List[str],
) -> List[Tuple[str, str, str, str, str, str]]:
    """
    Extract the round details from the battle log content.

    Args:
        log_content: The content of the battle log.

    Returns:
        List[Tuple[str, str, str, str, str, str]]: A list of tuples containing the round details.
    """
    round_lines = log_content[1:-1]  # Exclude the first and last lines
    round_details = []

    for line in round_lines:
        round_match = re.search(
            (
                r"ROUND (\d+) - (.+?) \(HP: ([\d.]+)\) v/s (.+?) \(HP:"
                r" ([\d.]+)\) - GANADOR: (.+)"
            ),
            line,
        )
        round_number = round_match.group(1)
        attacking_character = round_match.group(2)
        attacking_character_hp = round_match.group(3)
        defending_character = round_match.group(4)
        defending_character_hp = round_match.group(5)
        winner = round_match.group(6)
        round_details.append(
            (
                round_number,
                attacking_character,
                attacking_character_hp,
                defending_character,
                defending_character_hp,
                winner,
            )
        )

    return round_details


def extract_winning_team(
    log_content: List[str],
) -> str:
    """
    Extract the winning team from the battle log content.

    Args:
        log_content: The content of the battle log.

    Returns:
        str: The winning team.
    """
    winner_line = log_content[-1].strip()
    winner_match = re.search(
        r"GANADOR: TEAM (\d+)",
        winner_line,
    )
    winning_team = winner_match.group(1)
    return winning_team
