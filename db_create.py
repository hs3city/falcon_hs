import fdb
fdb.db.connect()
fdb.db.create_tables([fdb.db.Person])