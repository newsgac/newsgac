from newsgac import config
from pymodm.connection import connect
db = connect(config.mongo_url, serverSelectionTimeoutMS=1000, maxPoolSize=200, connect=False)
