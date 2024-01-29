"""
Base Database Module
=====================

This module provides a base class, `Base`, that serves as the declarative
base for SQLAlchemy models. It inherits from SQLAlchemy's `DeclarativeBase`
and is intended to be used as a base class for declarative models in
SQLAlchemy.

Classes
-------
- Base: DeclarativeBase
    Base class for declarative models.

Usage
------
To use this module, inherit from the `Base` class when defining your
SQLAlchemy models. For example:

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from your_module import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
```

Note
----
Ensure that you have SQLAlchemy installed to use this module.
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):  # pylint: disable=too-few-public-methods
    """
    Base class for declarative models in SQLAlchemy.

    This class is intended to be used as a base class for declarative models
    in SQLAlchemy. It inherits from `DeclarativeBase`, the declarative base
    class provided by SQLAlchemy.

    Example
    -------
    ```python
    from sqlalchemy import Column, Integer, String
    from your_module import Base

    class User(Base):
        __tablename__ = 'users'

        id = Column(Integer, primary_key=True)
        username = Column(String, nullable=False)
        email = Column(String, nullable=False, unique=True)
    ```
    """
