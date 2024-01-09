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
    
wires = [("cerveny", 5), ("modry", 7), ("zluty", 12)]
 
def cut_wire(wires:list[Wire], index:int, length:int) -> int:
    if index < 0 or index >= len(wires):
        return 0
    




length = cut_wire(wires, 1, 4)
print(length)


# new_list = []
#     for wire in wires:
#             if wires.index(("modry", 7)) == index:
#                 cut_length = int(wires[index].length) - length
#                 new_list.append(cut_length)
#             else:
#                 new_list.append(wire)
#     return new_list