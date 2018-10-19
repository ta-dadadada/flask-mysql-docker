from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from .settings import DATA_SOURCE, ECHO
engine = create_engine(DATA_SOURCE, echo=ECHO)
engine.echo = True
session = scoped_session(sessionmaker(bind=engine))


def query(*args, **kwargs):
    """
    sqlalchemy session.query

    :param args: モデルクラス、カラム
    :param kwargs:
    :return: query
    """
    return session.query(*args, **kwargs)


def add(*entities, auto_flush=True, auto_commit=True):
    """
    session add

    :param entities: モデルクラス
    :param bool auto_flush:
    :param bool auto_commit:
    """
    session.add_all(entities)
    if auto_commit:
        session.commit()
    elif auto_flush:
        session.flush()


def delete(entity):
    """session delete"""
    session.delete(entity)


def commit():
    """session commit"""
    session.commit()


def flush():
    """session flush"""
    session.flush()


def rollback():
    """session rollback"""
    session.rollback()
