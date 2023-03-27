from typing import Any, NamedTuple, Generic, TypeVar, Optional


T = TypeVar("T")


class SlotID(NamedTuple, Generic[T]):
    solver: "Solver"
    slot: str

class InputID(SlotID[T]):
    pass

class OutputID(SlotID[T]):
    pass


class Solver:
    __id: str
    __inputs: dict[str, Any]
    __outputs: dict[str, Any]
    __parent: Optional["Solver"]

    def __init__(self, id: str) -> None:
        self.__id = id
        self.__inputs = dict()
        self.__outputs = dict()

    def __str__(self) -> str:
        return f"{self.__class__.__qualname__}('{self.__id}')"
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def add_input(self, name: str, value: Any) -> None:
        self.__inputs[name] = value

    def add_output(self, name: str, value: Any) -> None:
        self.__outputs[name] = value

    def set_parent(self, parent: "Solver") -> None:
        self.__parent = parent


class Slot(Generic[T]):
    _name: str

    def __set_name__(self, owner: type, name: str) -> None:
        self._name = name


class Input(Slot[T]):
    
    def __get__(self, solver: Solver, obj_type: type) -> InputID[T]:
        return InputID(solver, self._name)
    
    def __set__(self, solver: Solver, value: T | InputID[T] | OutputID[T]) -> None:
        if isinstance(value, InputID):
            
        solver.add_input(self._name, value)


class Output(Slot[T]):
    pass


class Divmod(Solver):
    left = Input[int]()
    right = Input[int]()
    quotient = Output[int]()
    remainder = Output[int]()

dm1 = Divmod("foo")
dm2 = Divmod("foo")
dm1.left = 10
dm1.right = 3
dm2.left = dm1.quotient
