import sqlite3

conn = sqlite3.connect('shop.db')
# create the cursor
c = conn.cursor()

# create the table
# c.execute("""CREATE TABLE shop (
#     chips text,
#     chocolates text,
#     Cooldrink text,
#     cupcakes text,
#     fruit text,
#     pies text,
#     veggies text
# )""")

# shopitmes = [
#     ('Simbra', 'Cadberry', 'Coke', 'vanilla', 'pear', 'Pepper steak', 'Spinach'),
#     ('Lays', 'Tex', 'Fanta', 'Chocolates', 'apple', 'Chicken', 'Cabbage'),
#     ('', '', '', '', 'orange', '', ''),
# ]

# c.executemany("INSERT INTO shop VALUES(?,?,?,?,?,?,?)", shopitmes)

c.execute("SELECT * FROM shop")
print(c.fetchall())


print('Data has been inserted')
conn.commit()
conn.close()
