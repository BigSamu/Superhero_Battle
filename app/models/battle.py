from . import Character, Team
from ..utils import (
    TeamPopulationError,
    BattleStartError,
    print_header,
    print_subheader,
    print_team_stats,
    print_intro_message,
    print_and_return_round_details,
    print_round_results,
    print_move_details,
    print_move_results,
    print_battle_winner,
    log_battle_teams,
    log_battle_winner,
    log_round_results,
)

from ..services import Email_Service


class Battle:
    """
    A class representing a battle between two teams of superheroes.
    """

    ###########################################################
    # CLASS CONSTRUCTOR
    ###########################################################

    def __init__(self):
        """
        Initialize a Battle instance.

        Returns:
            None.
        """
        self.team_1 = Team("Team 1")
        self.team_2 = Team("Team 2")

    ###########################################################
    # PUBLIC METHODS
    ###########################################################

    def start_battle(self) -> None:
        """
        Start the battle simulation.

        Returns:
            None.

        Raises:
            SimulationError: If the battle simulation cannot be started.
        """
        try:
            print_intro_message()
            self._create_teams()
            self._simulate_team_battle()
        except BattleStartError as e:
            print(" ")
            print(f"A fallado la simulacion -> {str(e)}")

        print_header("TERMINO DE SIMULACION")

    ###########################################################
    # PRIVATE METHODS
    ###########################################################

    def _create_teams(self) -> None:
        """
        Create the teams and populate them with characters.

        Returns:
            None.

        Raises:
            BattleStartError: If the teams cannot be created.
        """
        print_header("EQUIPOS")
        print("Agregando personajes a cada equipo...")
        print(" ")
        try:
            self.team_1.populate_team()
            self.team_2.populate_team()
        except TeamPopulationError as e:
            raise BattleStartError(f"{str(e)}")

        print(" ")
        print("Equipos conformados...")
        print(" ")
        print_team_stats(self.team_1)
        print(" ")
        print_team_stats(self.team_2)

    def _simulate_team_battle(
        self,
    ) -> None:
        """
        Simulate the battle between the teams.

        Returns:
            None.
        """
        print_header("COMIENZA LA BATALLA")

        round_number = 1
        log_battle_teams(self.team_1, self.team_2)
        while self.team_1.team_has_members() and self.team_2.team_has_members():
            self._simulate_round(round_number)
            round_number += 1

        if self.team_1.team_has_members():
            print_battle_winner(self.team_1)
            log_battle_winner(self.team_1)
        elif self.team_2.team_has_members():
            print_battle_winner(self.team_2)
            log_battle_winner(self.team_2)

        email = Email_Service.get_email_provided_by_user()
        print_header("NOTIFICACION DE EMAIL")
        if email:
            Email_Service.process_email(email)
        else:
            print("No se proporcionó ninguna dirección de correo electrónico.")

    def _simulate_round(self, round_number: int) -> None:
        """
        Simulate a round of attacks between the teams.

        Args:
            round_number: The number of the current round.

        Returns:
            None.
        """
        attacking_team = self.team_1
        defending_team = self.team_2
        attacking_character = attacking_team.select_random_character()
        defending_character = defending_team.select_random_character()
        round_details = print_and_return_round_details(
            round_number,
            attacking_character,
            defending_character,
        )

        move_number = 1
        while True:
            (
                attack_value,
                attack_type,
            ) = attacking_character.attack(defending_character)
            print_move_details(
                move_number,
                attacking_character,
                defending_character,
                attack_type,
                attack_value,
            )
            if defending_character.is_defeated():
                print_round_results(
                    attacking_character,
                    defending_character,
                )
                log_round_results(
                    round_details,
                    attacking_character,
                )
                defending_team.remove_member(defending_character)
                attacking_character.reset_HP()
                break
            else:
                print_move_results(defending_character)
                (
                    attacking_character,
                    defending_character,
                ) = (
                    defending_character,
                    attacking_character,
                )
                (
                    attacking_team,
                    defending_team,
                ) = (
                    defending_team,
                    attacking_team,
                )
                move_number += 1
