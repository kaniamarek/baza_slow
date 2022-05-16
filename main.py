import sqlite3

con = sqlite3.connect('test.db')
con.row_factory = sqlite3.Row
cur = con.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS slowa (
        id INTEGER PRIMARY KEY ASC,
        slowo varchar(250) NOT NULL,
        liczba varchar(250) DEFAULT ''
    )""")


def uzupelnij():
    plik = open(r"C:\Users\marek\Downloads\sjp-20220424\slowa.txt", "r", encoding="utf-8")
    zamiana = {"s": 0, "z": 0, "t": 1, "d": 1, "n": 2, "m": 3, "r": 4, "l": 5, "j": 6, "k": 7, "g": 7, "f": 8, "w": 8,
               "p": 9, "b": 9}

    for i in plik:
        linia = i.strip()
        var = ""
        for litera in linia:
            if litera in zamiana:
                var += str(zamiana[litera])
        if var != "":
            print(linia,var)
            cur.execute("INSERT INTO main.slowa VALUES(NULL, ?, ?);",(linia, var))
    con.commit()

def szukaj(x):
    cur.execute("SELECT *  FROM main.slowa WHERE liczba = ?;", (x,))
    rows = cur.fetchall()
    for row in rows:
            print(row["slowo"])

szukana = (input("Podaj Liczbe do sprawdzienia: ").strip())
print(szukana)
szukaj(szukana)