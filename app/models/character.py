import random
from typing import Dict, Tuple


class Character:
    """
    A class representing a character in the simulation.
    """

    ###########################################################
    # CLASS CONSTRUCTOR
    ###########################################################

    def __init__(
        self,
        id: int,
        name: str,
        alignment: str,
        base_stats: Dict[str, float],
    ) -> None:
        """
        Initialize a Character instance.

        Args:
            id: The ID of the character.
            name: The name of the character.
            base_stats: The base stats of the character.
            alignment: The alignment of the character.
        """
        self.id = id
        self.name = name
        self.base_stats = base_stats
        self.alignment = alignment
        self.AS: int = random.randint(0, 10)
        self.FB: float = None
        self.stats: Dict[str, float] = None
        self.HP: float = None
        self.attacks: Dict[str, float] = None

    ###########################################################
    # PUBLIC METHODS
    ###########################################################

    def init_FB_stats_HP_and_attacks(self, team_alignment: str) -> None:
        """
        Initialize the FB, stats, HP, and attacks of the character.

        Args:
            team_alignment: The alignment of the team the character belongs to.
        Returns:
            None.
        """
        self._calculate_FB(team_alignment)
        self._calculate_stats()
        self._calculate_HP()
        self._calculate_attack_values()

    def attack(self, opponent: "Character") -> Tuple[float, str]:
        """
        Perform an attack on the opponent.

        Args:
            opponent: The opponent character.

        Returns:
            A tuple containing the attack value and attack type.
        """
        attack_type: str = random.choice(list(self.attacks.keys()))
        attack_value: float = self.attacks[attack_type]
        opponent.HP -= attack_value
        return attack_value, attack_type

    def is_defeated(self) -> bool:
        """
        Check if the character is defeated.

        Returns:
            True if the character's HP is less than 0, False otherwise.
        """
        return self.HP < 0

    def reset_HP(self) -> None:
        """
        Reset the character's HP.

        Returns:
            None.
        """
        self._calculate_HP()

    ###########################################################
    # PRIVATE METHODS
    ###########################################################

    def _calculate_FB(self, team_alignment: str) -> None:
        """
        Calculate the Filiation Coefficient (FB) of the character.

        Args:
            team_alignment: The alignment of the team the character belongs to.
        Returns:
            None. The calculated FB is assigned to the `self.FB` attribute of the character.
        """
        if self.alignment == team_alignment:
            self.FB = 1 + random.randint(0, 9)
        else:
            self.FB = 1 / (1 + random.randint(0, 9))

    def _calculate_stats(self) -> None:
        """
        Calculate the stats of the character.

        Args:
            base_stats: The base stats of the character.

        Returns:
            None. The calculated stats are assigned to the `self.stats` attribute of the character.
        """
        self.stats = {
            k: ((2 * v + self.AS) / 1.1 * self.FB)
            for k, v in self.base_stats.items()
        }

    def _calculate_HP(self) -> None:
        """
        Calculate the Health Points (HP) of the character.

        Returns:
            None. The calculated HP is assigned to the `self.HP` attribute of the character.
        """
        strength: float = self.stats["strength"]
        durability: float = self.stats["durability"]
        power: float = self.stats["power"]
        self.HP = (
            (strength * 0.8 + durability * 0.7 + power) / 2 * (1 + self.AS / 10)
        ) + 100

    def _calculate_attack_values(
        self,
    ) -> None:
        """
        Calculate the attack values for the character's attacks.

        Returns:
            None. The calculated attack values are assigned to the `self.attacks` attribute of the character.
        """
        attack_types: Dict[str, Dict[str, float]] = {
            "mental": {
                "intelligence": 0.7,
                "speed": 0.2,
                "combat": 0.1,
            },
            "strong": {
                "strength": 0.6,
                "power": 0.2,
                "combat": 0.2,
            },
            "fast": {
                "speed": 0.55,
                "durability": 0.25,
                "strength": 0.2,
            },
        }

        self.attacks = {}
        for (
            attack_type,
            coefficients,
        ) in attack_types.items():
            attack_value = (
                sum(
                    self.stats[stat] * coeff
                    for stat, coeff in coefficients.items()
                )
                * self.FB
            )
            self.attacks[attack_type] = attack_value
