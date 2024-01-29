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
>>>from flask import Flask
>>>db=MyDB()
>>>app=Flask(__name__)
>>>db.init_app(app)
"""
from contextlib import contextmanager
from typing import Any, Generator, Optional

from flask import Flask
from sqlalchemy import Engine, create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, sessionmaker

from src.main.database.exceptions import (
    DatabaseURINotFoundError,
    SessionCreationError,
)


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
    Methods
    -------
    init_app(self, app: Flask) -> None:
        Initialize the database manager with a Flask app.

        Parameters
        ----------
        app : Flask
            The Flask application instance.

        Returns
        -------
        None

        Raises
        ------
        DatabaseURINotFoundError
            If the 'DATABASE_URI' configuration is not found in the app.

    session(self) -> Generator[Session, None, None]:
        Context manager for creating a session to read data
        from the database.

        This method yields a sessionmaker instance, allowing you
        to interact with the database in a read-only manner. The
        session should be used within a `with` statement, and it
        will be automatically closed when exiting the block.

        Yields
        ------
        Session: class
            A Session for reading data from the database.

        Note
        ----
        Make sure to use this session only for read operations
        to avoid unintentional modifications to the database.

        Raises
        ------
        DatabaseConnectionError: Exception
            If there is an issue creating the database session.
    """

    def __init__(self, app: Optional[Flask] = None) -> None:
        self._app: Optional[Flask] = app
        self._uri: Optional[str] = None
        self._engine: Optional[Engine] = None
        self._db_session: Optional[Session] = None

        if self._app:
            self.init_app(self._app)

    def init_app(self, app: Flask) -> None:
        """
        Initialize the database manager with a Flask app.

        Parameters
        ----------
        app : Flask
            The Flask application instance.

        Returns
        -------
        None

        Raises
        ------
        DatabaseURINotFoundError
            If the 'DATABASE_URI' configuration is not found in the app.

        Notes
        -----
        This method initializes the database manager with the 'DATABASE_URI'
        configurationnfrom the Flask app. If the 'DATABASE_URI' is not found
        in the app configuration, it raises a DatabaseURINotFoundError.
        Otherwise, it creates a database engine using the provided URI.

        Example
        -------
        >>> from flask import Flask
        >>> from your_module import YourDatabaseManager
        >>> app = Flask(__name__)
        >>> db_manager = YourDatabaseManager()
        >>> db_manager.init_app(app)
        """
        self._uri = app.config["DATABASE_URI"]
        if self._uri is None:  # type: ignore
            raise DatabaseURINotFoundError("Database URI not found in config")

        self._engine = create_engine(self._uri)  # type: ignore

    def _create_session(self) -> Session:
        if self._engine is None:
            raise RuntimeError(
                "Database engine not initialized. \
                Call init_app() first."
            )
        try:
            sess: Any = sessionmaker(bind=self._engine)
            return sess()
        except SQLAlchemyError as e:
            raise SessionCreationError(f"Error creating session!: {e}") from e

    @contextmanager
    def session(self) -> Generator[Session, None, None]:
        """
        Context manager for creating a session to read data
        from the database.

        This method yields a sessionmaker instance, allowing you
        to interact with the database in a read-only manner. The
        session should be used within a `with` statement, and it
        will be automatically closed when exiting the block.

        Yields
        ------
        Session: class
            A Session for reading data from the database.

        Note
        ----
        Make sure to use this session only for read operations
        to avoid unintentional modifications to the database.

        Raises
        ------
        DatabaseConnectionError: Exception
            If there is an issue creating the database session.
        """
        try:
            self._db_session = self._create_session()
            yield self._db_session
        finally:
            if self._db_session:
                self._db_session.close()
