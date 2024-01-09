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
    
def cut_wire(wires: list[Wire], index: int, length: int) -> int:
    if index < 0 or index >= len(wires) or length <= 0:
        return 0

    current_length = wires[index].length

    if length >= current_length:
        return 0

    cut_length = current_length - length
    wires[index] = Wire(wires[index].color, length)

    for i in range(index, 0, -1):
        if wires[i].length < wires[i - 1].length:
            wires[i], wires[i - 1] = wires[i - 1], wires[i]
        else:
            break

    return cut_length

wires_list = [Wire("cerveny", 5), Wire("modry", 7), Wire("zluty", 12)]

length1 = cut_wire(wires_list, 1, 4)
print(f"length1: {length1}")
for wire in wires_list:
    print(wire)

length2 = cut_wire(wires_list, 2, 13)
print(f"length2: {length2}")
for wire in wires_list:
    print(wire)