import sqlite3
from configparser import ConfigParser

class DatabaseHelper:
    configur = ConfigParser()
    configur.read('../config/config.ini')
    DB_NAME=configur.get('DB', 'DB_NAME')

    def __init__(self, db_name=DB_NAME):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        # Create tables if they don't exist
        with self.conn:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS weather_data (
                city TEXT PRIMARY KEY,
                temperature REAL,
                feels_like REAL
            )''')

    def insert_weather_data(self, city, temperature, feels_like):
        # Insert weather data for a city
        with self.conn:
            self.conn.execute("""INSERT INTO weather_data (
                              city, temperature, feels_like) 
                              VALUES (?, ?, ?)""",
                              (city, temperature, feels_like))

    def get_weather_data(self, city):
        # Get weather data for a city
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM weather_data WHERE city = ?", (city,))
            row = cursor.fetchone()
        return row  # Returns a tuple containing (city, temperature, feels_like) or None if not found