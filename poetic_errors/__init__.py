from .handler import PoeticErrorHandler
import sys

# Install the error handler by default when imported
poetic_handler = PoeticErrorHandler()
sys.excepthook = poetic_handler