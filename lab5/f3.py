class Name:
    def __init__(self, name, hobby='') -> None:
        if name not in ["Богдан", "Анонім", "Анастасія"]:
            raise ValueError("Дозволені імена: Богдан, Анонім")
        if hobby == '':
            raise ValueError("Хобі не може бути пустим")

        self.name = name
        self.hobby = hobby

a = Name("Анастасія", "Читання")
b = Name("Анастасія")