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



