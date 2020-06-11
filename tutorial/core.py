import sqlalchemy
from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    ForeignKey,
    Sequence,
    select,
    text,
)
from sqlalchemy.engine import Engine, ResultProxy

print(sqlalchemy.__version__)
"""
Lazy Connecting

The Engine, when first returned by create_engine(), has not actually tried to connect 
to the database yet; that happens only the first time it is asked to perform a task 
against the database.
"""


def get_test_engine() -> Engine:
    return create_engine("sqlite:///:memory", echo=False)


def users_table(meta) -> Table:
    return Table(
        "users",
        meta,
        Column("id", Integer, Sequence("user_id_seq"), primary_key=True),
        Column("name", String(50)),
        Column("fullname", String(50)),
    )


def addresses_table(meta) -> Table:
    return Table(
        "addresses",
        meta,
        Column("id", Integer, Sequence("address_id_seq"), primary_key=True),
        Column("user_id", ForeignKey("users.id")),
        Column("email_address", String(50), nullable=False),
    )


def create_tables():
    metadata = MetaData()
    users = users_table(metadata)
    addresses = addresses_table(metadata)
    metadata.create_all(get_test_engine())
    return metadata, users, addresses


def get_user_insert(user_table):
    return user_table.insert().values(name="jack", fullname="Jack Jones")


def get_user_insert_string(user_table) -> str:
    return str(get_user_insert(user_table))


def execute_insert(engine: Engine, users_insert) -> ResultProxy:
    conn = engine.connect()
    result: ResultProxy = conn.execute(users_insert)
    return result


def execute_insert_many_addresses(engine: Engine, address_table):
    conn = engine.connect()
    return conn.execute(
        address_table.insert(),
        [
            {"user_id": 1, "email_address": "jack@yahoo.com"},
            {"user_id": 1, "email_address": "jack@msn.com"},
            {"user_id": 2, "email_address": "www@www.org"},
            {"user_id": 2, "email_address": "wendy@aol.com"},
        ],
    )


def get_users(users):
    conn = get_test_engine().connect()
    s = select([users])
    return conn.execute(s)


def select_some_columns(users, addresses):
    conn = get_test_engine().connect()
    s = select(
        [users.c.id, users.c.name, users.c.fullname, addresses.c.email_address]
    ).where(users.c.id == addresses.c.user_id)
    return conn.execute(s)


def delete_tables():
    delete_users = text(
        """
    DELETE FROM users
    """
    )
    delete_addresses = text(
        """
    DELETE FROM addresses
    """
    )
    conn = get_test_engine().connect()
    conn.execute(delete_users)
    conn.execute(delete_addresses)
