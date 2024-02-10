"""
List of blueprints to be resistred to Flask App.
"""

from src.main.utils.register import register
from src.owner_auth import blp as owner_auth_blp

BLUEPRINTS = [
    register(owner_auth_blp, "/owner", "owner_auth"),
]
