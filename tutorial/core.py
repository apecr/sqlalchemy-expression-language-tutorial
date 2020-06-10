import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, Sequence
from sqlalchemy.engine import Engine, ResultProxy

print(sqlalchemy.__version__)
"""
Lazy Connecting

The Engine, when first returned by create_engine(), has not actually tried to connect 
to the database yet; that happens only the first time it is asked to perform a task 
against the database.
"""


def get_test_engine() -> Engine:
    return create_engine('sqlite:///:memory', echo=True)


def users_table(meta) -> Table:
    return Table('users', meta,
                 Column('id', Integer, Sequence('user_id_seq'), primary_key=True),
                 Column('name', String(50)),
                 Column('fullname', String(50)))


def addresses_table(meta) -> Table:
    return Table('addresses', meta,
                 Column('id', Integer, Sequence('address_id_seq'), primary_key=True),
                 Column('user_id', ForeignKey('users.id')),
                 Column('email_address', String(50), nullable=False))


def create_tables():
    metadata = MetaData()
    users = users_table(metadata)
    addresses = addresses_table(metadata)
    metadata.create_all(get_test_engine())
    return metadata, users, addresses


def get_user_insert(user_table):
    return user_table.insert().values(name='jack', fullname='Jack Jones')


def get_user_insert_string(user_table) -> str:
    return str(get_user_insert(user_table))


def execute_insert(engine: Engine, users_insert) -> ResultProxy:
    conn = engine.connect()
    result: ResultProxy = conn.execute(users_insert)
    print(result)
    print(result.inserted_primary_key)
    return result


def execute_insert_many_addresses(engine: Engine, address_table):
    conn = engine.connect()
    return conn.execute(address_table.insert(), [
        {'user_id': 1, 'email_address': 'jack@yahoo.com'},
        {'user_id': 1, 'email_address': 'jack@msn.com'},
        {'user_id': 2, 'email_address': 'www@www.org'},
        {'user_id': 2, 'email_address': 'wendy@aol.com'},
    ])



# result = execute_insert(engine=get_test_engine())
# print(get_user_insert(users_table(MetaData())).compile().params)
# print(result)
# get_user_insert().bind = get_test_engine()
# print(str(get_user_insert(users_table(MetaData()))))
# print(result.inserted_primary_key)
