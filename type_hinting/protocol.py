import json
from typing import Protocol, Iterable


class Serializable(Protocol):
    def serialize(self) -> str:
        ...


class Person:
    __slots__ = ('first_name', 'last_name', 'age')

    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def serialize(self) -> str:
        return json.dumps([self.first_name, self.last_name, self.age])


def store_data(data_points: Iterable[Serializable]) -> None:
    with open('data', 'w') as file:
        file.writelines([data_point.serialize() for data_point in data_points])


store_data(
    [Person(first_name='timber', last_name='kerkvliet', age=33)]
)
