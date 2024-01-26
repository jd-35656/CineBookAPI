"""
wsgi module
=======================

This module initializes the main application instance using the MyApp class.

Usage
-----
Create an instance of MyApp to initialize the Flask application:

    >>> from src.main.app import MyApp
    >>> app_instance = MyApp()
    >>> application = app_instance.create_app()
"""


from src.main.app import MyApp

app_instance = MyApp()

application = app_instance.create_app()
