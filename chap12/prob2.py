#파일명: prob2.py
#작성자 : 강승균 , 학번 : 202611813
#작성일자 : 2026.10.07
#Programming 2. 주소를 나타내는 Address와 사람을 나타내는 Person 클래스를 정의한다. Address와 Person을 동시에 상속받아서 Contact 클래스를 정의해보자. Contact 클래스는 연락처를 나타낸다.

class Address:
    def __init__(self, street, city):
        self.street, self.city = str(street), str(city)

class Person:
    def __init__(self, name, email):
        self.name, self.email = name, email

class Contact(Address, Person):
    def __init__(self, street, city, name, email):
        Address().__init__(street, city)
        Person().__init__(name, email)
