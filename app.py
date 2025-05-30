from vetiver import VetiverModel
from dotenv import load_dotenv, find_dotenv
import vetiver
import pins
import os

load_dotenv(find_dotenv())

print("Current working directory:", os.getcwd())
print("Contents of current directory:", os.listdir())
print("Contents of /vetiver/data/model:", os.listdir("/vetiver/data/model"))

# Create board with pickle read enabled
b = pins.board_folder('/vetiver/data/model', allow_pickle_read=True)

# Try to list available versions
try:
    versions = b.pin_versions('peng_model')
    print("Available versions:", versions)
except Exception as e:
    print("Error getting versions:", str(e))

# Try to load without version first
v = VetiverModel.from_pin(b, 'peng_model')

# Create the API
vetiver_api = vetiver.VetiverAPI(v)
api = vetiver_api.app
