# Создаем подключение к базе данных (файл players.db будет создан)
# connection = sqlite3.connect('players.db')
# выполнения SQL-запросов и операций с базой данных
# cursor = connection.cursor()
#
# Сохраняем изменения и закрываем соединение
# connection.commit()
# connection.close()

import sqlite3

class PlayerDatabase:
    def __init__(self, db_name="players.db"):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        self.init_db()

    def init_db(self):
        try:
            self.connection = sqlite3.connect('players.db')
            self.cursor = self.connection.cursor()

            self.cursor.execute('''
                    CREATE TABLE IF NOT EXISTS players (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        hp REAL NOT NULL,
                        armor REAL NOT NULL,
                        attack REAL NOT NULL
                    )
                ''')
            self.connection.commit()
        except sqlite3.Error as error:
            print(error)

        def close_db(self):
            self.connection.close()
