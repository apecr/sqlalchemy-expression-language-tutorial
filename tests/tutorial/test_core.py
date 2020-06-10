from tutorial.core import get_user_insert_string, create_tables, execute_insert, get_test_engine, get_user_insert, \
    execute_insert_many_addresses


def create_tables_test():
    tables = None

    def create_tab():
        nonlocal tables
        if tables is None:
            print('Creating tables')
            tables = create_tables()
        return tables
    return create_tab


setup = create_tables_test()


def test_create_tables():
    metadata, users, addresses = setup()
    assert users is not None


def test_get_user_insert_string():
    metadata, users, addresses = setup()
    users_insert = get_user_insert_string(users)
    assert """INSERT INTO users (id, name, fullname) VALUES""" in users_insert


def test_insert_element():
    metadata, users, addresses = setup()
    result = execute_insert(engine=get_test_engine(), users_insert=get_user_insert(users))
    assert result is not None


def test_insert_addresses():
    metadata, users, addresses = setup()
    result = execute_insert_many_addresses(engine=get_test_engine(), address_table=addresses)
    assert result is not None
