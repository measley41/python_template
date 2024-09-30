from beings import Person
from pytest import fixture


@fixture
def person():
    return Person("Bob White", 21, jobs=["Baker"])


def test_init(person):
    assert person.name == "Bob White"
    assert person.age == 21
    assert person.jobs == ["Baker"]


def test_first_name(person):
    assert person.first_name == "Bob"


def test_last_name(person):
    assert person.last_name == "White"

