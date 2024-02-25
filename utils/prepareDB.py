import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

db = mysql.connector.connect(
    host=os.getenv("DB_IP"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

dbcursor = db.cursor()

dbcursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, dc_id BIGINT NOT NULL, guild_id BIGINT NOT NULL, lvl DOUBLE NOT NULL, kys_count INT, kms_count INT)")