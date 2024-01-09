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
    
def load(filename: str) -> list[Wire]:
    wires = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 2):
            color = lines[i].strip()
            length = int(lines[i + 1].strip())
            wires.append(Wire(color, length))
    return wires

def save(wires: list[Wire], filename: str):
    with open(filename, 'w') as file:
        for wire in wires:
            file.write(str(wire) + '\n')
