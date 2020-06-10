from sqlalchemy.engine import ResultProxy

from tests.conftest import logger
from tutorial.core import (
    get_user_insert_string,
    create_tables,
    execute_insert,
    get_test_engine,
    get_user_insert,
    execute_insert_many_addresses,
    get_users,
    select_some_columns, )


def test_create_tables(conf_tables):
    metadata, users, addresses = conf_tables
    assert users is not None


def test_get_user_insert_string(conf_tables):
    metadata, users, addresses = conf_tables
    users_insert = get_user_insert_string(users)
    assert """INSERT INTO users (id, name, fullname) VALUES""" in users_insert


def test_insert_element(conf_tables):
    metadata, users, addresses = conf_tables
    result = execute_insert(
        engine=get_test_engine(), users_insert=get_user_insert(users)
    )
    assert result is not None


def test_insert_addresses(conf_tables):
    metadata, users, addresses = conf_tables
    result: ResultProxy = execute_insert_many_addresses(
        engine=get_test_engine(), address_table=addresses
    )
    logger.info(result.is_insert)
    assert result.is_insert
    assert result is not None


def test_select_users(conf_tables):
    metadata, users, addresses = conf_tables
    result = get_users(users)
    assert result.fetchall()[0][1] == "jack"
    row = get_users(users).fetchone()
    assert row["name"] == "jack"


def test_select_specific_columns(conf_tables):
    users, addresses = conf_tables[1:]
    result = select_some_columns(users, addresses)
    logger.info(result.fetchall())
    assert result is not None
