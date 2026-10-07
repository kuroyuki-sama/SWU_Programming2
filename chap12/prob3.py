#파일명: prob3.py
#작성자 : 강승균 , 학번 : 202611813
#작성일자 : 2026.10.07
#Programming 3. 일반적인 함수를 나타내는 Function 클래스를 정의한다. Function 클래스의 value() 는 아직 정의되지 않았다.Function 클래스를 상속받아서 2차 방정식을 나타내는 클래스 Quadratic를 정의한다. 여기서 a, b, c는 모두 멤버 변수가 된다. value() 메소드를 오버라이딩하라. 다음과 같은 메소드들을 정의한다.

class Function(object):
    def __init__(self):
        pass

    def value(self):
        pass

class Quadratic(Function):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def value(self, x):
        return self.a * x ** 2 + self.b * x + self.c

    def get_roots(self):
        return (-self.b + (self.b ** 2 - 4 * self.a * self.c) * 1/2) / 2 * self.a, (-self.b - (self.b ** 2 - 4 * self.a * self.c) * 1/2) / 2 * self.a 

