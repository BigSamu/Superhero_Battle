###########################################################
# CUSTOM EXCEPTIONS
###########################################################


class CharacterDataFetchError(Exception):
    """
    Exception raised when there is an error fetching character data from the Superhero API.
    """

    pass


class TeamPopulationError(Exception):
    """
    Exception raised when there is an error populating a team with characters.
    """

    pass


class TeamCreationError(Exception):
    """
    Exception raised when there is an error creating a team.
    """

    pass


class BattleStartError(Exception):
    """
    Exception raised when there is an error starting a battle.
    """

    pass


class SimulationError(Exception):
    """
    Exception raised when there is an error in the battle simulation.
    """

    pass


class EmailValidationError(Exception):
    """
    Exception raised when there is an error validating an email address.
    """

    pass


class EmailServiceError(Exception):
    """
    Exception raised when there is an error with the Mailgun API.
    """

    pass
