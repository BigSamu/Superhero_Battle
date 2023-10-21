import random
import time
from typing import Dict, Union, Tuple
import requests
from requests.exceptions import (
    RequestException,
)
from ..utils import (
    CharacterDataFetchError,
)
from ..config import SUPERHERO_API_URL


class Character_Service:
    """
    A class for fetching character data from the Superhero API.
    """

    ###########################################################
    # PUBLIC METHODS
    ###########################################################

    @classmethod
    def get_character_data(
        cls, character_id
    ) -> Tuple[str, str, Dict[str, float]]:
        """
        Fetch character data from the Superhero API.

        Args:
            character_id: The ID of the character
        Returns:
            A tuple containing the name, alignment, and base stats of the character.
        Raises:
            CharacterFetchError: If there is an error fetching character data from the Superhero API.
        """
        retry_counter = 0
        max_retries = 3
        response = None

        while retry_counter < max_retries:
            try:
                response = requests.get(f"{SUPERHERO_API_URL}/{character_id}")
                response.raise_for_status()

                character_data = response.json()
                name = character_data["name"]
                alignment = character_data["biography"]["alignment"]
                intelligence = character_data["powerstats"]["intelligence"]
                strength = character_data["powerstats"]["strength"]
                speed = character_data["powerstats"]["speed"]
                durability = character_data["powerstats"]["durability"]
                power = character_data["powerstats"]["power"]
                combat = character_data["powerstats"]["combat"]

                base_stats = Character_Service._parse_base_stats_data(
                    intelligence, strength, speed, durability, power, combat
                )

                return name, alignment, base_stats
            except RequestException as e:
                print(
                    "No se pudo obtener la información del personaje con ID"
                    f" {character_id}."
                )
                print("Reintentando en 5 segundos...")
                retry_counter += 1
                time.sleep(5)
                if retry_counter == max_retries:
                    raise CharacterDataFetchError(
                        "No se pudo obtener la data de personajes en Superhero"
                        f" API.\n{str(e)}"
                    )

    ###########################################################
    # AUXILIARY METHODS
    ###########################################################

    @staticmethod
    def _parse_base_stats_data(
        intelligence: str,
        strength: str,
        speed: str,
        durability: str,
        power: str,
        combat: str,
    ) -> Dict[str, int]:
        """
        Parse the base stats of a character obtained from the Superhero API.

        Returns:
            Dict[str, int]: The parsed stats of the character with integer values.
        """

        return {
            "intelligence": int(intelligence) if intelligence != "null" else 0,
            "strength": int(strength) if strength != "null" else 0,
            "speed": int(speed) if speed != "null" else 0,
            "durability": int(durability) if durability != "null" else 0,
            "power": int(power) if power != "null" else 0,
            "combat": int(combat) if combat != "null" else 0,
        }
