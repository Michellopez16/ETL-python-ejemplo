
from dotenv import dotenv_values

#sauce_username = os.environ["SpotyClienteID"]
#sauce_access_key = os.environ["SpotyClienteSecret"]


config = dotenv_values(".env")

print(config["NEXT_CONF"])

config["SpotyClienteID"]
config["SpotyClienteSecret"]