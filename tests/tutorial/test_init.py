import tutorial


def test_get_version():
    assert tutorial.__version__ == "0.1.0"


def test_get_name():
    assert tutorial.__package_name__ == "sqlalchemy-expression-language-tutorial"
