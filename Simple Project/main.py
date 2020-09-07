import sqlite3
from random import randint
bank = sqlite3.connect('bank.db')
c = bank.cursor()

def make_table():
    c.execute('CREATE TABLE IF NOT EXISTS accounts(user_id TEXT, balance REAL)')

def add(user, balance):
    
    c.execute(f"INSERT INTO accounts (user_id, balance) VALUES(?, ?)",(user, balance))
    bank.commit()

# read all from database
def read_from_db():
    c.execute('SELECT * FROM accounts')
    # data = c.fetchall()
    # you can do c.fetchone()
    # print(data)

    for row in c.fetchall():
        print(row)


def read_specific_person(value, name):
    c.execute(f"SELECT * FROM accounts WHERE balance = {value} and user_id = '{name}'")
    for row in c.fetchall():
        print(row)


def read_specific_person(value, name):
    c.execute(f"SELECT * FROM accounts WHERE balance = {value} and user_id = '{name}'")
    for row in c.fetchall():
        print(row)

def get_balance(account_name):
    c.execute(f"SELECT balance FROM accounts WHERE user_id = '{account_name}'")
    for row in c.fetchall():
        print(row)
 
def update():
    c.execute("UPDATE accounts SET balance = 10 WHERE user_id = 'jake'")
    # saves the change
    bank.commit()

    c.execute("SELECT * FROM accounts")
    [print(row) for row in c.fetchall()]

def delete():
    c.execute("DELETE FROM accounts WHERE user_id = 'eugene'")
    bank.commit()

    c.execute("SELECT * FROM accounts")
    [print(row) for row in c.fetchall()]

add('eugene', 10)