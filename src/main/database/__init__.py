"""
Database Package
================

This package provides functionality for managing the database
connection and transactions in the CineBookAPI application.

Usage
-----
To interact with the database, you can import the `MyDB`
class from the `src.main.database.db_manager` module:

    >>> from src.main.database.db_manager import MyDB
    >>> db = MyDB()

The `MyDB` class offers methods for creating sessions,
transactions, and initializing the database connection.

Methods
-------
- `session`: Create a context for reading data from the database.
- `transaction`: Create a transactional context for adding,
    editing, and removing data from the database.
- `init_app(app: Flask) -> None`: Initialize the database
    connection with a Flask app.

Examples
--------
Initialize a database instance:

    >>> from src.main.database.db_manager import MyDB
    >>> db = MyDB()

Initialize the database with a Flask app:

    >>> from flask import Flask
    >>> app = Flask(__name__)
    >>> db.init_app(app)

Create a context for reading data from the database:

    >>> with db.session() as session:
    ...     # Your code to read data from the database
    ...     using the 'session' instance

Create a transactional context for adding, editing, and
removing data from the database:

    >>> with db.transaction() as session:
    ...     # Your code to perform database operations
    ...     using the 'session' instance

Note: Make sure to handle exceptions appropriately, and
always close the session or transaction context to ensure
proper database management.
"""

from src.main.database.db_manager import MyDB

db = MyDB()
