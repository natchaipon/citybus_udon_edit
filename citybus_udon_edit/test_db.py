import sqlite3
money = 20
date_time = "12-23-43"

with sqlite3.connect("C:/Users/Natchaipon/Desktop/citybus_udon_edit/citybus_udon.db") as con:
    cur = con.cursor()
    # cur.execute("INSERT INTO citybus_table (money , time) VALUES (? , ?)", (money , date_time))
    # con.commit()

    cur.execute("SELECT SUM(money) FROM citybus_table")
    rows = cur.fetchone()
    print(rows[0])
    # for row in rows:
    #     print(row)

# import sqlite3  
  
# con = sqlite3.connect("C:/Users/Natchaipon/Desktop/citybus_udon_edit/citybus_udon.db")  
# print("Database opened successfully")  