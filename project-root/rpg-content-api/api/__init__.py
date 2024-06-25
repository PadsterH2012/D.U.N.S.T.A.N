from flask import Flask

app = Flask(__name__)

# Import endpoints after app initialization to avoid circular imports
import api.endpoints
