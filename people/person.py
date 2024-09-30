from typing import Optional
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    job: str

    @property
    def first_name(self) -> str:
        return self.name.split(" ")[0]

    @property
    def last_name(self) -> Optional[str]:
        name = self.name.split(" ")[-1]
        return name if name != self.first_name else None
