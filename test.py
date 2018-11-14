import math
import re


class ManAndDag(object):

    def isNumReg(self, str):
        regInt = '\d+'  # 能匹配123、123.63、123eabd、abc236等所有包含了数字的字符串
        regInt2 = '\d+$'  # 能匹配123、123.63、abc236等所有以数字结尾的字符串
        regInt2 = '^\d+$'  # 只能匹配1、12、123等只包含数字的字符串
        regFloat = '\d+\.\d+'  # 能12.36、efa56.63、wwe56.56abc等字符串
        regFloat2 = '^\d+\.\d+$'  # 能匹配2.36、0.36、00069.63、0.0、263.25等

        # 以下是整数和小数正确的正则表达式
        regInt = '^0$|^[1-9]\d*$'  # 不接受09这样的为整数
        regFloat = '^0\.\d+$|^[1-9]\d*\.\d+$'
        # 接受0.00、0.360这样的为小数，不接受00.36，思路:若整数位为零,小数位可为任意整数，但小数位数至少为1位，若整数位为自然数打头，后面可添加任意多个整数，小数位至少1位

        regIntOrFloat = regInt + '|' + regFloat  # 整数或小数

        patternIntOrFloat = re.compile(regIntOrFloat)  # 创建pattern对象，以便后续可以复用
        if patternIntOrFloat.search(str):
            return True
        if re.search(patternIntOrFloat, str):
            return True
        if re.search(regIntOrFloat, str):
            return True
        else:
            return False

    def calculate(self):
        while True:
            inp = input("请输入你家狗狗的年龄: ")
            if not (self.isNumReg(inp)):
                print("格式有误，请重新输入")
                print("")
                continue
            age = float(inp)
            if age < 0:
                print("你是在逗我吧!")
            elif age < 1.0:
                print("相当小于 14 岁的人。")
            elif age == 1.0:
                print("相当于 14 岁的人。")
            elif 1.0 < age < 2.0:
                print("相当于 14~22 岁的人。")
            elif age == 2.0:
                print("相当于 22 岁的人。")
            elif age > 2.0:
                human = 22 + (age - 2) * 5
                print("对应人类年龄: ", math.floor(human))
            print("")


def main():
    # 初始化对象
    md = ManAndDag()
    md.calculate()


if __name__ == "__main__":
    main()
