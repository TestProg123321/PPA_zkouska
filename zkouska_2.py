class Wire:
    def __init__(self, color):
        self.color = color

    def resistor(self, second):
        resistor = self.color
        self.color = second.color
        print(resistor) # breakpoint
        return resistor

    def swap(self, second):
        second.color = self.resistor(second)
    
a = Wire(2)
b = Wire(3)
a.swap(b)


# main             heap
# a         -->    color = 2
# b         -->    color = 3

