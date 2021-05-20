from google.auth.transport import requests
from google.oauth2 import id_token


class Google:
    """
    Google class to fetch the usr info and return it
    """

    @staticmethod
    def validate(auth_token):
        """
        Validate method Queries the Google oAuth2 api to fetch the user info
        """

        try:
            id_info = id_token.verify_oauth2_token(auth_token, requests.Request())

            if "accounts.google.com" in id_info["iss"]:
                return id_info
        except:
            return "The token is either invaid or has expired Google"
