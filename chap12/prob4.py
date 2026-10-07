#파일명: prob4.py
#작성자 : 강승균 , 학번 : 202611813
#작성일자 : 2026.10.07
#Programming 4. 주사위 게임 프로그램을 작성해보자. 정상적인 주사위를 나타내는 Dice를 먼저 작성한다. Dice 클래스는 roll() 메소드를 가진다. roll()은 주사위를 한번 던지는 동작을 구현한다. Dice 클래스를 상속받아서 이번에는 FraudDice 클래스를 작성한다. FraudDice 클래스는 가짜 주사위로서 원하는 숫자가 나올떄까지 주사위를 굴린다.

import random as r

class Dice(object):
    def __init__(self):
        pass

    def roll(self):
        return r.randint(1, 6)

class FraudDice(Dice):
    def __init__(self):
        super().__init__()

    def roll(self):
        if (r.randint(1, 6) != 3):
            return FraudDice.roll()
        else:
            return 3
