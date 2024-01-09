class Wire:
    def __init__(self, color:str, length:int):
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