from math import sqrt
from typing import Iterable, List, Tuple, Union, Set, Optional, Callable


class Vector(object):
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        # type: (float, float) -> None
        self.x = x
        self.y = y

    def __str__(self):
        # type: () -> str
        return '({x}, {y})'.format(x=self.x, y=self.y)

    def __add__(self, other):
        # type: (Vector) -> Vector
        return Vector(x=self.x + other.x, y=self.x + other.x)

    def __sub__(self, other):
        # type: (Vector) -> Vector
        return self + other*-1

    def __mul__(self, scalar):
        # type: (float) -> Vector
        return Vector(x=self.x*scalar, y=self.y*scalar)

    def length(self):
        # type: () -> float
        return sqrt(self.x**2 + self.y**2)


def sort_vectors_by_length(vectors):
    # type: (Iterable[Vector]) -> List[Vector]
    return sorted(vectors, key=lambda v: v.length())


def print_vectors(vectors, sort=True):
    # type: (Iterable[Vector], bool) -> None
    if sort:
        vectors = sort_vectors_by_length(vectors)
    for vector in vectors:
        print(vector)


print_vectors(
    {Vector(3, 2), Vector(0, 0), Vector(3, 5), Vector(2, 2)}
)


NamedVectorList = List[Tuple[str, Vector]]


def print_named_vectors(named_vectors):
    # type: (NamedVectorList) -> None
    for name, vector in named_vectors:
        print('Vector {vector} with name {name}'.format(vector=vector, name=name))


print_named_vectors(
    [
        ('naam_1', Vector(9, 7)),
        ('naam_2', Vector(8, 8))
    ]
)


def print_named_or_unnamed_vectors(vectors):
    # type: (Union[Set[Vector], NamedVectorList]) -> None
    if isinstance(vectors, set):
        print_vectors(vectors=vectors)

        return

    print_named_vectors(named_vectors=vectors)


print_named_or_unnamed_vectors([('naam', Vector(9, 9))])

print_named_or_unnamed_vectors({Vector(10, 15)})


def find_small_vector(vectors, threshold):
    # type: (Iterable[Vector], float) -> Optional[Vector]
    for vector in vectors:
        if vector.length() <= threshold:
            return vector

    return None


find_small_vector(vectors=[Vector(3, 4), Vector(10, 10)], threshold=10)
find_small_vector(vectors=[Vector(10, 10), Vector(15, 15)], threshold=10)


def write_vectors_to_file(vectors, serializer):
    # type: (List[Vector], Callable[[Vector], str]) -> None
    with open('vectors', 'w') as f:
        f.writelines([serializer(vector) for vector in vectors])


write_vectors_to_file(
    vectors=[Vector(1, 3), Vector(9, 9)],
    serializer=lambda vector: str(vector)
)
