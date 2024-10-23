from math import sqrt
from os import system

class Exercise1:
    def __init__(self):
        self.a_0 = float(input("常数项>> "))
        print("\n")
        self.a_1 = float(input("一次项>> "))
        print("\n")
        self.a_2= float(input("二次项>> "))
        print("\n")
        self.culculate_and_print()

    def culculate_and_print(self):
        delta = self.a_1 ** 2 - 4 * self.a_0 * self.a_2
        if delta < 0:
            print("无实数根\n")
            return
        delta_sqrt = sqrt(delta)
        x1 = (-self.a_1 - delta_sqrt) / self.a_2 * 2
        x2 = (-self.a_1 + delta_sqrt) / self.a_2 * 2
        print("x1: ", str(x1), " x2: ", str(x2), "\n")

class Exercise2:
    def __init__(self):
        self.num = int(input("输入数>> "))
        print("\n")
        if self.num % 2 == 0:
            print("是偶数\n")
            return
        print("是奇数\n")

class Exercise3:
    def __init__(self):
        self.tem = int(input("输入温度>> "))
        print("\n")
        if self.tem > 25:
            print("适合晨练\n")
            return
        print("不适合晨练\n")

class Exercise4:
    def __init__(self):
        self.tem_us_f = 77.0
        self.tem_jp_c = 24.0
        self.culculate_and_print()
    
    def culculate_and_print(self):
        tem_us_c = (self.tem_us_f - 32) / 1.8
        if tem_us_c > self.tem_jp_c:
            print("美国温度高\n")
            return
        if tem_us_c < self.tem_jp_c:
            print("日本温度高\n")
            return
        print("温度一样高\n")
        
class Exercise5:
    def __init__(self):
        self.weight = float(input("请输入行李重量>> "))
        print("\n")
        self.culculate_and_print()

    def culculate_and_print(self):
        if self.weight <= 20.0:
            print("收费0元\n")
            return
        print("收费", str((self.weight - 20) * 1.5), "元\n")

class Exercise6:
    def __init__(self):
        self.score = float(input("请输入学生分数>> "))
        print("\n")
        self.culculate_and_print()
    
    def culculate_and_print(self):
        if self.score >= 85.0:
            print("优秀\n")
            return
        if self.score >= 60.0:
            print("及格\n")
            return
        print("不合格\n")
        

class Exercise7:
    def __init__(self):
        self.length = float(input("输入长>> "))
        print("\n")
        self.width = float(input("输入宽>> "))
        print("\n")
        self.culculate_and_print()

    def culculate_and_print(self):
        if self.length == self.width:
            print("正方形\n")
            return
        print("矩形\n")

class Exercise8:
    def __init__(self):
        self.command = input("输入命令>> ")
        print("\n")
        self.execute()
    
    def execute(self):
        match self.command:
            case "计算器":
                system("start calc")
            case "记事本":
                system("start notepad")
            case "画图":
                system("start mspaint")
            case "控制台":
                system("start cmd")
        