import sqlite3

database = sqlite3.connect('myworks.sqlite3')
sql = database.cursor()

sql.execute(
    '''CREATE TABLE IF NOT EXISTS myworks (
    works TEXT,
    description TEXT
    )
    '''
)
database.commit()

def register_works():
    global works, description
    works = input('name work: ')
    description = input('description work: ')

    sql.execute(f"SELECT works FROM myworks WHERE works = '{works}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO myworks VALUES (?, ?)",(works, description))
        database.commit()
        print('work add')
        for i in sql.execute(f'SELECT * FROM myworks'):
                print(i)
    else:
        print('this is work was added')
        for i in sql.execute(f'SELECT * FROM myworks'):
            print(i)

for i in sql.execute(f'SELECT * FROM myworks'):
    print(i)

def delete_work():
    works = input('work name: ')
    sql.execute(f"DELETE FROM myworks WHERE works = '{works}' ")
    database.commit()
    for i in sql.execute(f'SELECT * FROM myworks'):
        print(i)

while True:
    answer = input('you want delete or add new work? ')
    if answer == 'add':
        register_works()
    elif answer == 'delete':
        delete_work()
    elif answer == 'exit':
        break
    else:
        print('write (delete) or (add). If you exit, write (exit)')
        continue
 
# register_works()


