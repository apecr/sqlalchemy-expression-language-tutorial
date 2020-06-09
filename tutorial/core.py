import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, Sequence
from sqlalchemy.engine import Engine, ResultProxy

print(sqlalchemy.__version__)
engine: Engine = create_engine('sqlite:///:memory', echo=True)
"""
Lazy Connecting

The Engine, when first returned by create_engine(), has not actually tried to connect 
to the database yet; that happens only the first time it is asked to perform a task 
against the database.
"""

metadata = MetaData()
users = Table('users', metadata,
              Column('id', Integer, Sequence('user_id_seq'), primary_key=True),
              Column('name', String(50)),
              Column('fullname', String(50)))
addresses = Table('addresses', metadata,
                  Column('id', Integer, Sequence('address_id_seq'), primary_key=True),
                  Column('user_id', ForeignKey('users.id')),
                  Column('email_address', String(50), nullable=False))
metadata.create_all(engine)
ins = users.insert()
print(str(ins))
ins = users.insert().values(name='jack', fullname='Jack Jones')
print(str(ins))
print(ins.compile().params)
conn = engine.connect()
print(conn)
result: ResultProxy = conn.execute(ins)
print(result)
ins.bind = engine
print(str(ins))
print(result.inserted_primary_key)
