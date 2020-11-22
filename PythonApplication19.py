class Dog:
    def __init__(self,name, age) :
        self.Name=name
        self.Age=age


happy=Dog('happy', 6)
print("이름은 ", happy.Name,"이고, 나이는 ", happy.Age, "살입니다.", sep="")
