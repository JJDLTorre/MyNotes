import logging
from typing import Callable
from urllib.parse import urljoin
import bs4
import requests

# Define the OAuth redirect URL
OAUTH_REDIRECT_URL = 'https://login.microsoftonline.com/common/oauth2/nativeclient'


def cli_input(consent_url: str) -> str:
    """OAuth consent helper for manual consent via the CLI.

    Args:
        consent_url (str): URL for OAuth authentication

    Returns:
        str: Token URL received after successful authentication to consent_url.
    """
    print('Visit the following URL to give consent:')
    print(consent_url)

    return input('Paste the authenticated URL here:\n')


def _get_response_form(res: requests.Response, step_descr: str) -> tuple[str, str, dict[str, str]]:
    """Parses a Response and extracts form details from HTML.

    Args:
        res (requests.Response): The response from a URL request.
        step_descr (str): Description for error messages and logging.

    Raises:
        Exception: When no form is found on the page.
        Exception: When no form action URL is found.

    Returns:
        tuple[str, str, dict[str, str]]: Form method, action URL, and form data.
    """
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    form = soup.find("form")
    if not isinstance(form, bs4.Tag):
        raise Exception(f"{step_descr} - form not found")

    # Get the form action (requested URL)
    url = form.attrs.get("action")
    if not url:
        raise Exception(f"{step_descr} - form action URL not found")
    url = urljoin(res.url, url)

    # Get the form method (POST, GET, DELETE, etc)
    method = form.attrs.get("method", "get").lower()

    # Get the form_data from the inputs inside the form
    form_data: dict[str, str] = {}
    for input_elm in form.find_all("input"):
        if isinstance(input_elm, bs4.Tag):
            name = input_elm.attrs.get("name")
            if name:
                form_data[name] = input_elm.attrs.get("value", "")

    return (method, url, form_data)


def headless(username: str, password: str) -> Callable[[str], str]:
    """Gets a user's authentication without manual interaction.

    Args:
        username (str): The user's fully qualified username.
        password (str): The user's password.

    Returns:
        Callable[[str], str]: OAuth consent helper function that takes a consent URL and returns the
        token URL.
    """

    def consent_fn(consent_url: str) -> str:
        # Add the username to consent_url to skip discovery
        consent_url += f"&login_hint={username}"

        # Create a session for handling cookies
        with requests.Session() as session:
            # Request the consent_url
            res = session.get(consent_url)
            (method, url, form_data) = _get_response_form(res, "Step 1")

            # Request the SAML login page
            if method == "post":
                res = session.post(url, form_data)
            else:
                res = session.request(method, url, params=form_data)
            (method, url, form_data) = _get_response_form(res, "Step 2")

            # Add login credentials
            form_data["_eventId_proceed"] = ""
            for key in form_data:
                lkey = key.lower()
                if "user" in lkey or "email" in lkey:
                    form_data[key] = username
                elif "pass" in lkey:
                    form_data[key] = password

            # SAML Login
            if method == "post":
                res = session.post(url, form_data)
            else:
                res = session.request(method, url, params=form_data)
            (method, url, form_data) = _get_response_form(res, "Step 3")

            # SAML Response
            if method == "post":
                res = session.post(url, form_data)
            else:
                res = session.request(method, url, params=form_data)

            # Check if we have a token
            if OAUTH_REDIRECT_URL in res.url:
                return res.url

            raise Exception(
                "Invalid Authentication URL. Please verify that the user has authorized the application."
            )

    return consent_fn
