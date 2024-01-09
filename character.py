class Character:
    def __init__(self, name:str, attack:int, defence:int, hp:int):
        self._name = name
        self.attack = attack
        self._defence = defence
        self._hp = hp 


    @property
    def name(self) -> str:
        return self._name
    
    @property
    def defence(self) -> int:
        return self._defence
    
    @property
    def hp(self) -> int:
        return self._hp
    
    def __str__(self) -> str:
        return f"{self._name} [{self.attack}/{self._defence}, {self._hp}]"
    
