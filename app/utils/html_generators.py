from typing import List, Tuple

###########################################################
# HTML GENERATORS
###########################################################


def generate_html_header() -> str:
    """
    Generate the HTML header.

    Returns:
        str: The HTML header.
    """
    html = "<html>\n"
    html += "<head>\n"
    html += "<style>"
    html += "table { border-collapse: collapse; }"
    html += "th, td { text-align: center; padding: 10px; }"
    html += "th { background-color: #f2f2f2; }"
    html += "tr:nth-child(even) { background-color: #f9f9f9; }"
    html += "</style>\n"
    html += "</head>\n"
    html += "<body>\n"
    return html


def generate_html_footer() -> str:
    """
    Generate the HTML footer.

    Returns:
        str: The HTML footer.
    """
    return "</body>\n</html>\n"


def generate_html_battle_results_header(team_1: str, team_2: str) -> str:
    """
    Generate the HTML header for the battle results.
    Args:
    team_1: The name of Team 1.
    team_2: The name of Team 2.

    Returns:
        str: The HTML header for the battle results.
    """
    return (
        f"<h1>Battle Results</h1>\n<h2>Team {team_1} v/s Team"
        f" {team_2}</h2>\n"
    )


def generate_html_round_details_table(
    round_details: List[
        Tuple[
            str,
            str,
            float,
            str,
            float,
            str,
        ]
    ]
) -> str:
    """
    Generate the HTML table for the round details.

    Args:
        round_details: A list of tuples containing the round details.

    Returns:
        str: The HTML table for the round details.
    """

    table_header = (
        "<table>\n<tr><th>Round</th><th>Member Team 1</th><th>Member Team"
        " 2</th><th>Winner</th></tr>\n"
    )
    table_rows = ""

    for round_detail in round_details:
        (
            round_number,
            attacking_character,
            attacking_character_hp,
            defending_character,
            defending_character_hp,
            winner,
        ) = round_detail
        table_row = f"<tr><td>{round_number}</td>"
        table_row += (
            f"<td>{attacking_character} (HP: {attacking_character_hp})</td>"
        )
        table_row += (
            f"<td>{defending_character} (HP:"
            f" {defending_character_hp})</td><td>{winner}</td></tr>\n"
        )
        table_rows += table_row

    table = f"{table_header}{table_rows}</table>\n"
    return table


def generate_html_winning_team(
    winning_team: str,
) -> str:
    """
    Generate the HTML section for the winning team.

    Args:
        winning_team: The name of the winning team.

    Returns:
        str: The HTML section for the winning team.
    """
    return f"<h3>Winner: Team {winning_team}</h3>\n"
