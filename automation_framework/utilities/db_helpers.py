import sqlite3
from configparser import ConfigParser

class DatabaseHelper:
    configur = ConfigParser()
    configur.read('automation_framework\\config\\config.ini') 
    DB_NAME=configur.get('DB', 'DB_NAME')

    def __init__(self, db_name=DB_NAME):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        with self.conn: 
            self.conn.execute("DROP TABLE weather_data")
            self.conn.execute('''CREATE TABLE IF NOT EXISTS weather_data (
                city TEXT PRIMARY KEY,
                temperature REAL,
                feels_like REAL
            )''')

    def add_column(self, name):
        with self.conn:
            self.conn.execute(f"ALTER TABLE weather_data ADD COLUMN {name} REAL")

    def insert_weather_data(self, city, temperature, feels_like):
        # Insert weather data for a city
        with self.conn:
            self.conn.execute("INSERT INTO weather_data (city, temperature, feels_like) VALUES (?, ?, ?)",
                              (city, temperature, feels_like))

    def update_weather_data(self, city, col, value):
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute(f"UPDATE weather_data SET {col} = {value} WHERE city = {city}")

    def get_weather_data(self, city):
        # Get weather data for a city
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM weather_data WHERE city = ?", (city,))
            row = cursor.fetchone()
        return row  # Returns a tuple containing (city, temperature, feels_like) or None if not found
    
    def get_max_by_col(self, col):
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute(f"SELECT MAX( {col} ) FROM weather_data")
            row = cursor.fetchone()
        return row