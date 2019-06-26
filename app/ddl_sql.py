import sqlite3


class Database:
    conn = None
    c = None

    def __init__(self):
        self.conn = sqlite3.connect('Data1.db')
        self.c = self.conn.cursor()

    def create_table(self):
        self.c.execute("""CREATE TABLE Data(
                Time text,
                Agent text,
                datein text,
                dateout text,
                Listed integer,
                Std_EP integer,
                Std_CP integer,
                Sup_EP integer,
                Sup_CP integer
                )""")
        self.conn.commit()

    def insert_table(self, time, agent, datein, dateout, listed, std_ep, std_cp, sup_ep, sup_cp):
        self.c.execute("INSERT INTO Data VALUES(?,?,?,?,?,?,?,?,?)",
                       (time, agent, datein, dateout, listed, std_ep, std_cp, sup_ep, sup_cp))
        self.conn.commit()

    def print_db(self):
        self.c.execute("SELECT * FROM Data")
        rows = self.c.fetchall()
        for row in rows:
            print(row)
        self.conn.close()
