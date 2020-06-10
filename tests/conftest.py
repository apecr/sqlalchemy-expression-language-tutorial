import logging

import pytest

from tutorial.core import delete_tables, create_tables

FORMAT = "%(asctime)-15s %(levelname)s %(message)s"
logging.basicConfig(level=logging.DEBUG, format=FORMAT)
logger = logging.getLogger()


@pytest.fixture(scope="module")
def conf_tables():
    #setup = create_tables_test()
    yield create_tables()
    logger.info("Teardown tests")
    delete_tables()


def create_tables_test():
    tables = None

    def create_tab():
        nonlocal tables
        if tables is None:
            logger.info("Creating tables")
            tables = create_tables()
        logger.info("Hello")
        return tables

    return create_tab
