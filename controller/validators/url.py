from typing import NoReturn
from controller.errors.http.exceptions import bad_request
import re

class UrlValidator:
    def __init__(self, url_data: dict) -> NoReturn:
        self.url_data = url_data
        self.validate_url()
        self.validate_alias()

    def validate_url(self) -> NoReturn:
        url_re = re.compile(
            r'^(?:http|https):\/\/'
            r'(?:[\w-]+\.)+[a-zA-Z]{2,}'
            r'(?:\/[^\s]*)?$'
        )
        if not(url_re.match(self.url_data['url'])):
            raise bad_request(f"{self.url_data['url']} is not a URL")

    def validate_alias(self) -> NoReturn:
        alias_re = re.compile(
            r'^[^. =?]+$'
        )
        if not(alias_re.match(self.url_data['alias'])):
            raise bad_request(f"Invalid alias: {self.url_data['alias']}")