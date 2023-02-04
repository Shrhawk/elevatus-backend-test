import datetime

from pydantic import BaseModel as Base


class BaseModel(Base):
    created_on: datetime.datetime = datetime.datetime.now()
    updated_on: datetime.datetime = datetime.datetime.now()
