from typing import Generic, TypeVar, List

T = TypeVar('T')


class Stack(Generic[T]):
    __slots__ = ('_things',)

    def __init__(self):
        self._things = []  # type: List[T]

    def push(self, thing):
        # type: (T) -> None
        self._things.append(thing)

    def pop(self):
        # self: () -> T
        return self._things.pop()


integer_stack = Stack()  # type: Stack[int]

integer_stack.push(5)


string_stack = Stack()  # type: Stack[str]
string_stack.push('7')



