from app import greetings


def test_greet():
    assert greetings.greet("Ada") == "Hello, Ada! Welcome to the session."


def test_farewell():
    assert greetings.farewell("Ada") == "Goodbye, Ada — see you at the next session!"
