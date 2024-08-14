from models.url import Url
from uuid import uuid4
from datetime import datetime

def create_url_object(url_data: dict) -> Url:
    url = Url(
        id = str(uuid4()),
        url = url_data['url'],
        alias = url_data['alias'],
        create_at = datetime.now()
    )
    return url