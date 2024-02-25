import mysql.connector
import src.config as env

db = mysql.connector.connect(
    host=env.DB_HOST,
    user=env.DB_USER,
    password=env.DB_PASSWORD,
    database=env.DB_NAME
)

dbcursor = db.cursor()

dbcursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, dc_id BIGINT NOT NULL, guild_id BIGINT NOT NULL, lvl DOUBLE NOT NULL, kys_count INT, kms_count INT)")