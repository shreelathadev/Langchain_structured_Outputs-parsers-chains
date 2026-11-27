from typing import TypedDict

class Person(TypedDict):
    name : str
    age : int

new_person: Person = {'name':'nitish','age':35}

new_person: list[Person] = [ {'name': 'nitish', 'age':35},
                      {'name':"shree",'age':23}]

print(new_person)