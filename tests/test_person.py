from people.person import Person
from pytest import fixture


@fixture
def person():
    return Person("Bob White", 21, job="Baker")


def test_init(person):
    assert person.name == "Bob White"
    assert person.age == 21
    assert person.job == "Baker"


def test_first_name(person):
    assert person.first_name == "Bob"


def test_last_name(person):
    assert person.last_name == "White"


def test_age(person):
    assert person.age == 21
