import random
import time
import requests
from typing import Dict

from . import Character
from ..utils import (
    CharacterDataFetchError,
    TeamPopulationError,
    print_character_info,
)
from ..config import SUPERHERO_API_URL
from ..services import Character_Service


class Team:
    """
    Class representing a team of characters in a superhero battle simulation.
    """

    teams = []  # Class attribute

    ###########################################################
    # CLASS CONSTRUCTOR
    ###########################################################

    def __init__(self, name: str):
        """
        Initialize a Team instance.

        Args:
            name: The name of the team.
        """
        self.name = name
        self.members = []
        self.team_alignment = None
        self.teams.append(self)

    ###########################################################
    # PUBLIC METHODS
    ###########################################################

    def populate_team(self) -> None:
        """
        Populate the team with characters.

        Returns:
            None.

        Raises:
            TeamPopulationError: If the team cannot be populated with characters.
        """
        character_id = None

        while len(self.members) < 5:
            if character_id is None:
                character_id = Team._generate_random_character_id()

            while Team._is_character_in_any_team(character_id):
                print(
                    f"El personaje con ID {character_id} ya está en un equipo."
                )
                character_id = self._generate_random_character_id()

            try:
                (
                    name,
                    alignment,
                    base_stats,
                ) = Character_Service.get_character_data(character_id)
                character = Character(character_id, name, alignment, base_stats)
                if character:
                    self._add_character_to_team(character)
                    character_id = None  # Reset character_id since the character was successfully added
                else:
                    print(
                        "No se pudo agregar un personaje con ID"
                        f" {character_id} al equipo {self.name}."
                    )

            except CharacterDataFetchError as e:
                raise TeamPopulationError(f"{str(e)}")

        self._set_team_alignment()
        self._calculate_FB_stats_HP_and_attcks_for_team_members(
            self.team_alignment
        )

    def team_has_members(self) -> bool:
        """
        Check if the team has members.

        Returns:
            bool: True if the team has members, False otherwise.
        """
        return len(self.members) > 0

    def select_random_character(
        self,
    ) -> Character:
        """
        Select a random character from the team.

        Returns:
            Character: A random character from the team.
        """
        return random.choice(self.members)

    def remove_member(self, member: Character) -> None:
        """
        Remove a member from the team.

        Args:
            member: The character to remove from the team.

        Returns:
            None.
        """
        if member in self.members:
            self.members.remove(member)
        else:
            print(
                f"El personaje {member.name} no pertenece al equipo {self.name}"
            )

    ###########################################################
    # PRIVATE METHODS
    ###########################################################

    @classmethod
    def _is_character_in_any_team(cls, character_id: int) -> bool:
        """
        Check if a character with the given ID exists in any team.

        Args:
            character_id: The ID of the character.

        Returns:
            bool: True if the character is in any team, False otherwise.
        """
        for team in cls.teams:
            for member in team.members:
                if member.id == character_id:
                    return True
        return False

    def _add_character_to_team(self, character: Character) -> None:
        """
        Add a character to the team.

        Args:
            character: The character to add to the team.

        Returns:
            None.
        """
        self.members.append(character)
        print(
            f"Se ha agregado el personaje {character.name} con ID"
            f" {character.id} al equipo {self.name}"
        )

    def _set_team_alignment(
        self,
    ) -> None:
        """
        Set the alignment of the team based on the characters' alignments.

        Returns:
            None.
        """
        alignment_dict = {}
        for member in self.members:
            alignment = member.alignment
            if alignment in alignment_dict:
                alignment_dict[alignment] += 1
            else:
                alignment_dict[alignment] = 1
        team_alignment = max(
            alignment_dict,
            key=alignment_dict.get,
        )
        self.team_alignment = team_alignment

    def _calculate_FB_stats_HP_and_attcks_for_team_members(
        self, team_alignment: str
    ) -> None:
        """
        Calculate the FB stats, HP, and attacks for the team members once team alignment is defined.

        Args:
            team_alignment: The alignment of the team.

        Returns:
            None.
        """
        for member in self.members:
            member.init_FB_stats_HP_and_attacks(self.team_alignment)

    ###########################################################
    # AUXILIAR METHODS
    ###########################################################

    @staticmethod
    def _generate_random_character_id() -> int:
        """
        Generate a random character ID.

        Returns:
            int: A random character ID.

        """
        return random.randint(1, 731)
