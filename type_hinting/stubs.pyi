class Vector:
    __slots__ = ('x', 'y')

    def __init__(self, x: float, y: float):
        ...

    def __str__(self) -> str:
        ...

    def __add__(self, other: Vector) -> Vector:
        ...

    def __sub__(self, other: Vector) -> Vector:
        ...

    def __mul__(self, scalar: float) -> Vector:
        ...

    def __len__(self) -> float:
        ...
