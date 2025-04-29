# Przed:
from hello_world.app import app
from hello_world.views import hello_world

# Po:
# Importuj tylko to, co jest potrzebne
from hello_world.app import app  # Lub usuń, jeśli 'app' nie jest używane


