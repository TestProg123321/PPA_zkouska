class Wire:
    def __init__(self, color: str, length: int):
        self._color = color
        self._length = length

    @property
    def color(self) -> str:
        return self._color

    @property
    def length(self) -> int:
        return self._length


    def __str__(self) -> str:
        return f"{self._color} [{self._length}]"


def get_shorter(wires: list[Wire], length: int, not_color: str) -> list[Wire]:
    result = []
    for wire in wires:
        if wire.length > length and wire.color != not_color:
            result.append(wire)
    return result


wires_list = [Wire("zluty", 16), Wire("cerveny", 20), Wire("modry", 10), Wire("zluty", 12)]

shorter_wires = get_shorter(wires_list, 21, "zluty")



for wire in shorter_wires:
    print(wire)