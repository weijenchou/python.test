class Person:
    #self 是標記用，告訴別人有self的變數，函數屬於Person類別
    def __init__(self, name:str, age:int):
        self.person_name= name
        self.age= age
    
    def introduce(self):
        return f"""Hello, my name is {self.person_name} \nI'm {self.age} years old."""


"""
class的繼承
新的class 可以繼承原有class所有屬性、函數
"""

class Students(Person):
    def __init__(self, name, age, classroom:str, country='台灣'):
        super().__init__(name, age)
        #把Person的self.person_name和self.age功能繼承過來
        self.classroom= classroom
        self.country= country

    def where_class(self) -> str:
        return f'我在 {self.classroom}'
       

#實例化
#person = Person('John',19)
student1= Students('Peter',8,'二年二班','美國') #預設台灣，放美國就會是美國
print(student1.age)
print(student1.person_name)
print(student1.introduce()) #person的介紹函數
print(student1.where_class())