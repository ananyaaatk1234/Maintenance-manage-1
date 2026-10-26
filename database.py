import sqlite3

connection = sqlite3.connect("maintenance.db")

cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS machines 
(id INTEGER PRIMARY KEY AUTOINCREMENT,
  machine_id TEXT NOT NULL,
  machine_name TEXT NOT NULL,
  loc TEXT NOT NULL,
  tech TEXT NOT NULL,
  last_maintenance_date TEXT,
  health TEXT NOT NULL,
  running_hours INTEGER,
  temperature REAL)""")

cursor.execute("""INSERT INTO machines 
(machine_id,
  machine_name,
  loc,
  tech,
  last_maintenance_date,
  health,
  running_hours,
  temperature)
VALUES(?,?,?,?,?,?,?,?)""",
  ('M001',
    'CNC Machine',
    'Factory A',
    'John',
    '2026-10-20',
    'Good',
    1250,
    62.5))

connection.commit()

connection.close()

print("Database created successfully!")
