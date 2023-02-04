import datetime

from beanie import Document


class BaseModel(Document):
    created_on: datetime.datetime = datetime.datetime.now()
    updated_on: datetime.datetime = datetime.datetime.now()
