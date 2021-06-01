import sqlite3

# Verbindung zur Datenbank herstellen / öffnen

# Datenbank erstellen, falls sie nicht existiert
connection = sqlite3.connect('person.db')

# Datenbank im Haupspeicher erstellen
# wird bei jeder Ausführung des Skripts neu erstellt
# connection = sqlite3.connect(':memory:')

# Cursor/Zeiger um mit der Datenbank interagieren zu können
cur = connection.cursor()


def create_database_table():
    """Datenbanktabelle erstellen"""
    cur.execute("""CREATE TABLE IF NOT EXISTS person
                       (
                            person_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            vorname TEXT,
                            nachname TEXT,
                            telefonnummer TEXT
                       );
                    """)


def get_user_input():
    """Benutzereingabe"""
    vorname = input("Bitte einen Vornamen eingeben: ")
    nachname = input("Bitte einen Nachnamen eingeben: ")
    telefonnummer = input("Bitte eine Telefonnummer eingeben: ")

vorname = ''
nachname = ''
telefonnummer = ''


def insert_data_into_database():
    # Datensätze in die Datenbank einfügen
    get_user_input()
    cur.execute("""INSERT INTO person 
                        (vorname, nachname, telefonnummer)
                    VALUES 
                        (:vorname, :nachname, :telefonnummer)""",
                        {'vorname': vorname, 'nachname': nachname, 'telefonnummer': telefonnummer}
                )


create_database_table()
insert_data_into_database()


# In Datenbank schreiben
connection.commit()

"""Datensätze anzeigen"""
result = cur.execute("""SELECT * FROM person""")

# Ergebnis auf der Konsole ausgeben
print(result.fetchall())

# Datenbankverbindung schliessen
connection.close()