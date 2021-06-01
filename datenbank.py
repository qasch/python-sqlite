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
    """Benutzereingabe
    ACHTUNG: Es findet noch keine Validierung der Eingaben statt!"""
    vorname = input("Bitte einen Vornamen eingeben: ")
    nachname = input("Bitte einen Nachnamen eingeben: ")
    telefonnummer = input("Bitte eine Telefonnummer eingeben: ")

    user_input_list = [vorname, nachname, telefonnummer]

    return user_input_list


def insert_data_into_database():
    # Datensätze in die Datenbank einfügen
    cur.execute("""INSERT INTO person 
                        (vorname, nachname, telefonnummer)
                    VALUES 
                        (?, ?, ?)""", get_user_input()
                )
    # In Datenbank schreiben
    connection.commit()


create_database_table()


execute_program = True
while execute_program:
    user_action = input("Datensatz [e]infügen\nDatenbank [a]nzeigen\nProgramm [b]eenden?")
    if user_action == 'e':
        insert_data_into_database()
    elif user_action == 'a':
        """Datensätze anzeigen"""
        result = cur.execute("""SELECT * FROM person""")
        # Ergebnis auf der Konsole ausgeben
        print(result.fetchall())
    elif user_action == 'b':
        execute_program = False


# Datenbankverbindung schliessen
connection.close()

print("Das wars, Programm beendet.")
