import pymysql
import os
from dotenv import load_dotenv

load_dotenv()
passDB = os.environ["passDB"]
hostDB = "localhost"
userDB = "root"
nameDB = "main"
db = pymysql.connect(host=hostDB, user=userDB, password=passDB, database=nameDB, cursorclass = pymysql.cursors.DictCursor)

cursor = db.cursor()

def cekDBOpen():
    if (not db.open):
        db.connect