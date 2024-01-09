from trida import Wire

def cut_wire(wires:list[Wire], index:int, length:int) -> int:
    if index >= len(wires) or index < 0 or length < 0:
        return 0
    
    current_length = wires[index].length

    if current_length <= length:
        return 0 
    
    cut_length = current_length - length
    
    wires[index] = Wire(wires[index].color, length)

    for i in range(index, 0, -1):
        if wires[i].length < wires[i - 1].length:
            wires[i], wires[i - 1] = wires[i - 1], wires[i]
        else:
            break
    
    return cut_length


wires = [Wire("cerveny", 5), Wire("modry", 7), Wire("zluty", 12)]


length = cut_wire(wires, 1, 4)
print(f"length: {length}")
for wire in wires:
    print(wire)