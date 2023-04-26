class CppHeader:
    __name: str
    
    def __init__(self, name: str) -> None:
        self.__name = name

    def __str__(self) -> str:
        guard_id = self.__name.upper() + "_H"
        return "\n".join([
            f"#ifndef {guard_id}",
            f"#define {guard_id}",
            f"#endif",
        ]) + "\n"


with open("primitives.hpp", "w") as f:
    f.write(str(CppHeader("primitives")))
