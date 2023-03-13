import time
import json
from typing import Dict, Optional

import requests
from requests import Response
from requests.cookies import RequestsCookieJar


class SysAidClient:

    def __init__(self, account_id: str, username: str, password: str) -> Response:
        """
        Log the user in upon initialization.

        Args:
            account_id (str): The account ID of the SysAid instance.
            username (str): The username of the user.
            password (str): The password of the user.
        """

        self.login_time_limit: int = 2700
        self.username: str = username
        self.password: str = password
        self.account_id: str = account_id
        self.jsessionid: Optional[str] = None

        self.access_url: str = f"https://{self.account_id}.sysaidit.com/api/v1"
        self.login_url: str = f"{self.access_url}/login"

    def login(self) -> None:
        """
        Log the user in.
        """

        headers: dict = {
            "Accept": "*/*",
            "User-Agent": "Thunder Client (https://www.thunderclient.com)",
            "Content-Type": "application/json"
        }

        payload: str = json.dumps({"user_name": self.username,
                                   "account_id": self.account_id,
                                   "password": self.password
                                   })

        response: Response = requests.request(
            method="POST", url=self.login_url, data=payload,  headers=headers)
        print(response)
        cookies: RequestsCookieJar = response.cookies

        if "JSESSIONID" not in cookies:
            raise Exception(
                "No JSESSIONID cookie found. User already logged in.")

        self.login_time: float = time.time()
        self.jsessionid: Optional[str] = cookies.get("JSESSIONID")

    def is_alive(self) -> bool:
        """
        Check if the client is still logged in.

        Returns:
            bool: True if logged in, False otherwise.
        """

        # Calculate the time passed since the user logged in.
        time_passed: int = time.time() - self.login_time

        # 45 minutes in seconds.
        return time_passed < self.login_time_limit

    def request_united(self, method: str, endpoint: str, headers: Optional[Dict] = None, payload: Optional[Dict] = None) -> Response:
        """
        Make a request to the SysAid API.

        Args:
            method (str): The HTTP method to use.
            endpoint (str): The endpoint to use.
            headers (Dict): The headers to use.
            payload (Dict): The payload to use.

        Returns:
            Response: The response from the API.
        """

        if payload is None:
            payload = {}
        if headers is None:
            headers = {}

        # Add the JSESSIONID to the headers.
        headers["Cookie"] = f"JSESSIONID={self.jsessionid}"

        # Build the url.
        url: str = f"{self.access_url}{endpoint}"

        # Make the request.
        response: Response = requests.request(
            method=method, url=url, data=payload, headers=headers)

        return response
