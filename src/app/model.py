from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)
from ether import Base


class Member(Base):
    __tablename__ = 'member'

    member_id = Column(Integer, primary_key=True, autoincrement=True)
    member_name = Column(String(250), nullable=False, unique=True)
    created = Column(DateTime, default=datetime.now)
    exclude_columns = ['member_id', 'created']

    def __str__(self):
        return f'{self.__class__.__name__}({self.member_id}, {self.member_name})'
