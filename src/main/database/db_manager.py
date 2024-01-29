"""
Database Management Module
===========================

This module provides a convenient class, MyDB, for managing
database connections in a Flask application. It includes methods
for initializing the database connection, creating read-only
sessions, and creating transactional sessions. The module also
defines exceptions for handling database-related errors.

Classes
-------
    MyDB: class
        Database Connection Management class.

Example
-------
Passing Flask as an argument.
>>>from db_manager import MyDB
>>>from flask import Flask
>>>app = Flask(__name__)
>>>db = MyDB(app)

Without passing Flask app as an argument.
>>>from db_manager import MyDB
>>>db=MyDB()
"""
from typing import Optional

from flask import Flask
from sqlalchemy import Engine
from sqlalchemy.orm import Session


class MyDB:
    """
    Database Connection Management.

    This class provides a simple interface for managing
    database connections in a Flask application. It includes
    methods for initializing the database connection, creating
    read-only sessions, and creating transactional sessions.

    Args
    ----
        app: (Optional[Flask])
            Flask application instance.
    """

    def __init__(self, app: Optional[Flask] = None) -> None:
        self._uri: Optional[str] = None
        self._engine: Optional[Engine] = None
        self._db_session: Optional[Session] = None
