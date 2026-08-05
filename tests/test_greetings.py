from app import greetings


def test_greet():
    assert greetings.greet("Ada") == "Hello, Ada! Welcome to the session."
