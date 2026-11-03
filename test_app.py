
from app import hello_world, welcome_message

def test_hello_world():
    assert hello_world() == "Hello, DevOps!"

def test_hello_world_type():
    assert isinstance(hello_world(), str)

def test_welcome_message_rachit():
    assert welcome_message("Rachit") == "Welcome to DevOps, Rachit!"

def test_welcome_message_rahul():
    assert welcome_message("Rahul") == "Welcome to DevOps, Rahul!"
