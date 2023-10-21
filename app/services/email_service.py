import argparse
from typing import Union
from datetime import date
import requests
from requests.exceptions import (
    RequestException,
)
from email_validator import (
    validate_email,
    EmailNotValidError,
)
from ..utils import (
    EmailValidationError,
    EmailServiceError,
)
from ..config import (
    MAILGUN_API_KEY,
    MAILGUN_API_URL,
    ROOT_DIRECTORY_PATH,
)
from ..utils import (
    extract_team_names,
    extract_round_details,
    extract_winning_team,
    generate_html_header,
    generate_html_footer,
    generate_html_battle_results_header,
    generate_html_round_details_table,
    generate_html_winning_team,
)


class Email_Service:
    """
    A class for sending battle results via email.
    """

    ###########################################################
    # PUBLIC METHODS
    ###########################################################

    @classmethod
    def process_email(cls, email_address: str) -> None:
        try:
            Email_Service._validate_email_address(email_address)
            Email_Service._send_email(
                email_address,
                "Resultados de Batalla",
                "Aqui los resultados de la batalla.",
            )
        except (
            EmailValidationError,
            EmailServiceError,
        ) as e:
            print(f"Error en Servicio de Email. {str(e)}")

    @classmethod
    def get_email_provided_by_user(cls) -> Union[str, None]:
        """
        Get the email address provided by the user.

        Returns:
            Union[str, None]: The email address provided by the user, or None if not provided.
        """
        parser = argparse.ArgumentParser()
        parser.add_argument("-email", nargs="?", type=str, help="Email address")
        args = parser.parse_args()
        return args.email if args.email else None

    ###########################################################
    # AUXILIARY METHODS
    ###########################################################

    @staticmethod
    def _send_email(
        recipient: str,
        subject: str,
        content: str,
    ) -> None:
        """
        Send an email to the recipient.

        Args:
            recipient: The recipient's email address.
            subject: The subject of the email.
            content: The content of the email.

        Returns:
            None.

        Raises:
            EmailServiceError: If the email could not be sent due to connection problems with the Mailgun API.
        """
        url = MAILGUN_API_URL
        auth = ("api", MAILGUN_API_KEY)
        data = {
            "from": "Superhero Battle <bigsamu@superherobattle.com>",
            "to": recipient,
            "subject": (
                f"SuperHero Battle Simulation from BigSamu - {date.today()}"
            ),
            "text": content,
            "html": Email_Service._parse_log_file_to_html(),
        }
        try:
            response = requests.post(
                url,
                auth=auth,
                data=data,
            )
            response.raise_for_status()
            print(f"Email enviado a {recipient}")
        except RequestException as e:
            raise EmailServiceError(
                f"No se pudo conectart con Mailgun API.\n{e}"
            )

    @staticmethod
    def _validate_email_address(email: str) -> None:
        """
        Validate the format of an email address.

        Args:
            email: The email address to validate.

        Returns:
            bool: True if the email address is valid, False otherwise.

        Raises:
            EmailValidationError: If the email address is not valid.
        """
        try:
            validated = validate_email(email)
            if validated:
                print(
                    "Email válido. Enviando resultados a la dirección de"
                    " correo proporcionada."
                )
        except EmailNotValidError as e:
            raise EmailValidationError(
                "Email proporcionado no válido.\nLos resultados de la"
                " batalla no se envían a ninguna dirección."
            )

    @staticmethod
    def _parse_log_file_to_html() -> str:
        """
        Parse the battle log file into HTML format for detailed email content.

        Returns:
            str: The HTML content representing the battle results.
        """
        log_path = f"{ROOT_DIRECTORY_PATH}/battle_log.txt"
        with open(log_path, "r") as file:
            log_content = file.readlines()

        (
            team_1,
            team_2,
        ) = extract_team_names(log_content)
        round_details = extract_round_details(log_content)
        winning_team = extract_winning_team(log_content)

        html = generate_html_header()
        html += generate_html_battle_results_header(team_1, team_2)
        html += generate_html_round_details_table(round_details)
        html += generate_html_winning_team(winning_team)
        html += generate_html_footer()

        return html
