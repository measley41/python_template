from typing import Optional


class Person:
    def __init__(self, name: str, age: int, jobs: Optional[list[str]] = None) -> None:
        self.name = name
        self.age = age
        self.jobs = jobs or []

    @property
    def first_name(self) -> str:
        return self.name.split(" ")[0]

    @property
    def last_name(self) -> Optional[str]:
        name = self.name.split(" ")[-1]
        return name if name != self.first_name else None
