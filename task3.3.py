import sqlite3
import json
import os
while False:
    with open (os.path.join(os.sys.path[0], 'BinanceSampleData.json'),'r') as files:
        data = files.read()
        data = json.loads(data)
        
    connection = sqlite3.connect('sample.db')
    cursor = connection.cursor()
    #cursor.execute('CREATE TABLE btcdat2 (price FLOAT, quantity FLOAT, time FLOAT )')
    data_list = []
    for d in data:
        p = float(d['p'])
        q = float(d['q'])
        t = float(d['T'])
        dat = (p, q, t)
        data_list.append(dat)
    print(data_list)
    instruction = """INSERT INTO btcdat2 (price, quantity, time) VALUES (?, ?, ?);"""
    cursor.executemany(instruction, data_list)
    print("Total", cursor.rowcount, "Records inserted successfully into btcdata2 table")
    connection.commit()
    cursor.close()


        
connection = sqlite3.connect('sample.db')
cursor = connection.cursor()

#task 1 : giving the price form the time of the transaction
while False:
    date = 1624711283094
    rows = cursor.execute(
        "SELECT price FROM btcdat2 WHERE time = ?",
        (date,),
    ).fetchall()
    print(rows)

# task 2 : List all datasets, which have a quantity of greater than 1
while False:
    quantity = 1
    rows = cursor.execute(
        "SELECT price, quantity ,time FROM btcdat2 WHERE quantity > ?",
        (quantity,),
        ).fetchall()
    print(rows)

#task 3 : Using COUNT, estimate the number of datasets where the quantiy was lower than 0.1

# cutoff = 0.1
# rows = cursor.execute("SELECT price FROM btcdat2 WHERE quantity < ?",
#     (cutoff,),).fetchall()
# print(len(rows))
while False:
    cutoff = 0.1
    rows = cursor.execute("SELECT COUNT(price) FROM btcdat2 WHERE quantity < ?",
        (cutoff,),).fetchall()
    print(rows)

# task 4 : Using AVG, calculate the average price of all datasets.

avg = cursor.execute("SELECT AVG(price) from btcdat2").fetchall()
print(avg)
 



