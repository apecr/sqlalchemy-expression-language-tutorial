from tutorial.core import get_user_insert_string, create_tables, execute_insert, get_test_engine, get_user_insert, \
    execute_insert_many_addresses


class Table:
    instance = None

    def __new__(cls, *args, **kwargs):
        if not Table.instance:
            print('Creating tables')
            Table.instance = create_tables()
        return Table.instance


def test_create_tables():
    metadata, users, addresses = Table()
    assert users is not None


def test_get_user_insert_string():
    metadata, users, addresses = Table()
    users_insert = get_user_insert_string(users)
    assert """INSERT INTO users (id, name, fullname) VALUES""" in users_insert


def test_insert_element():
    metadata, users, addresses = Table()
    result = execute_insert(engine=get_test_engine(), users_insert=get_user_insert(users))
    assert result is not None


def test_insert_addresses():
    metadata, users, addresses = Table()
    result = execute_insert_many_addresses(engine=get_test_engine(), address_table=addresses)
    assert result is not None
