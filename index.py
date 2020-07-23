from peewee import *



Mysql = MySQLDatabase("test", user='root', password='123456789', host='localhost', port=3306)
Mysqlcur = Mysql.cursor()

db = SqliteDatabase('clinic.db', pragmas={
            'journal_mode': 'wal',  # allow readers and writers to co-exist
            'cache_size': -1 * 64000,  # 64MB set page-cache size in KiB, e.g. -32000 = 32MB
            'foreign_keys': 1,  # enforce foreign-key constraints
            'ignore_check_constraints': 0,  # enforce CHECK constraints
            'synchronous': 0  # let OS handle fsync (use with caution)
        })
cur = db.cursor()


query = '''
SELECT NAME , SQL FROM sqlite_master 
'''


cur.execute(query)
data = cur.fetchall()


for table in data :
    print(table[0])
    SQL = table[1]
    SQLR = SQL.replace('"','')
    print(SQLR)
    print(SQL)
    Mysqlcur.execute(SQLR)

