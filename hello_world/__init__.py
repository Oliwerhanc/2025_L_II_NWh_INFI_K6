import hello_world.views  # ← import przeniesiony na górę

from hello_world import app
from hello_world.formater import get_formatted
from hello_world.formater import SUPPORTED, PLAIN
from flask import request

# Dodaj pustą linię na końcu pliku