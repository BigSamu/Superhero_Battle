###########################################################
# HEADER AND SUBHEADER PRINTERS
###########################################################


def print_header(text) -> None:
    """
    Print a header.

    Returns:
        None.
    """
    char_count = 100
    text_length = len(text)
    space = " " * ((char_count - text_length) // 2)
    print(" ")
    print("*" * char_count)
    print(space + text + space)
    print("*" * char_count)
    print(" ")


def print_subheader(text) -> None:
    """
    Print a subheader.

    Returns:
        None.
    """
    char_count = 100
    print("-" * char_count)
    print(text)
    print("-" * char_count)


###########################################################
# CHARACTER PRINTERS
###########################################################


def print_character_info(
    character: "Character",
) -> None:
    """
    Print detailed information about the character.

    Returns:
        None.
    """
    print(f" - {character.name}:")
    print(f"    - ID: {character.id}")
    print(f"    - Alignment: {character.alignment}")
    print(f"    - AS (Actual Stamina): {character.AS:.2f}")
    print(f"    - FB (Filiation Coefficient): {character.FB:.2f}")
    print(f"    - HP (Health Points): {character.HP:.2f}")
    print(f"    - Stats:")
    for (
        stat,
        value,
    ) in character.stats.items():
        print(f"       - {stat}: {value:.2f}")
    print(f"    - Attacks:")
    for (
        attack_type,
        attack_value,
    ) in character.attacks.items():
        print(f"       - {attack_type}: {attack_value:.2f}")


###########################################################
# TEAM PRINTERS
###########################################################


def print_team_stats(team: "Team") -> None:
    """
    Print the statistics of the team.

    Returns:
        None.
    """
    print(f"Team: {team.name}")
    print(f"Team Alignment: {team.team_alignment}")
    print("Team Members:")
    for member in team.members:
        print_character_info(member)


###########################################################
# BATTLE PRINTERS
###########################################################


def print_intro_message() -> None:
    """
    Print the introduction message for the battle.

    Returns:
        None.
    """
    print_header("BIENVENIDO A SUPERHERO BATTLE")
    print(
        "En este juego, se enfrentarán dos equipos de 5 superhéroes cada"
        " uno."
    )
    print(
        "El equipo vencedor será quien tenga al último (o últimos)"
        " personajes en pie."
    )
    print("¡Que comience la batalla!")


def print_and_return_round_details(
    round_number: int,
    attacking_character: "Character",
    defending_character: "Character",
) -> str:
    """
    Print the round details and return the formatted string.

    Args:
        round_number: The number of the current round.
        attacking_character: The attacking character.
        defending_character: The defending character.

    Returns:
        The formatted round details string.
    """
    round_details = (
        f"ROUND {round_number} - {attacking_character.name} (HP:"
        f" {attacking_character.HP:.2f}) v/s"
        f" {defending_character.name} (HP: {defending_character.HP:.2f})"
    )
    print_subheader(round_details)
    return round_details


def print_round_results(
    attacking_character: "Character",
    defending_character: "Character",
) -> None:
    """
    Print the results of the round.

    Args:
        attacking_character: The attacking character.
        defending_character: The defending character.

    Returns:
        None.
    """
    print(
        f"{' '*7} {defending_character.name} ha sido derrotado. Ganador:"
        f" {attacking_character.name}"
    )


def print_move_details(
    move_number: int,
    attacking_character: "Character",
    defending_character: "Character",
    attack_type: str,
    attack_value: float,
) -> None:
    """
    Print the details of a move in the round.

    Args:
        move_number: The number of the current move.
        attacking_character: The attacking character.
        defending_character: The defending character.
        attack_type: The type of attack.
        attack_value: The value of the attack.

    Returns:
        None.
    """
    move_details = (
        f"Move {move_number}: {attacking_character.name} ataca a"
        f" {defending_character.name} con {attack_type} attack y causa"
        f" {attack_value:.2f} de daño."
    )
    print(move_details)


def print_move_results(
    defending_character: "Character",
) -> None:
    """
    Print the results of a move in the round.

    Args:
        defending_character: The defending character.

    Returns:
        None.
    """
    print(
        f"{' '*7} {defending_character.name} tiene"
        f" {defending_character.HP:.2f} HP restantes."
    )


def print_battle_winner(
    team: "Team",
) -> None:
    """
    Print the winner of the battle.

    Args:
        team: The winning team.

    Returns:
        None.
    """
    print_header("RESULTADOS FIANLES")
    print(f"El equipo ganador es {team.name}.")
