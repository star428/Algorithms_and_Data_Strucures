'''
Author: star428
Date: 2020-08-05 14:54:31
LastEditTime: 2020-08-06 15:07:53
LastEditors: Please set LastEditors
Description: 描述电路门的各种类继承
FilePath: \Algorithms_and_Data_Strucures\chapter_1\Electrical_network.py
扁平胜于嵌套，相对而言嵌套三次不太明确
'''


class LogicGate:  # 逻辑门
    """
        描述逻辑门总体的类，只包括标签和输出
    """
    def __init__(self, label):
        self.label = label
        self.output = None

    def getlabel(self):
        return self.label

    def getoutput(self):
        self.output = self.performGateLogic()  # 未定义实现函数，每一个实现都不相同
        return self.output

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source  # 这个时候的pinA已经变成connector类对象
        else:
            if self.pinB == None:
                self.pinB = source  # 同理pinB已经变成connector类对象
            else:
                raise RuntimeError("error: no empty pins")


class BinaryGate(LogicGate):
    """描述双输入逻辑门的类，新增了两个输入

    Args:
        LogicGate ([type]): 继承父类逻辑门，包括标签和输出
    """
    def __init__(self, label):
        super().__init__(label)
        # 两个引脚
        self.pinA = None
        self.pinB = None

    def get_pinA(self):
        if self.pinA == None:
            return int(input('Enter pin A input for gate ' + \
                self.getlabel() + "--->"))
        else:
            return self.pinA.getFrom().getoutput()  # 此时已经时connector对象调用相关函数

    def get_pinB(self):
        if self.pinB == None:
            return int(input("Enter pin B input for gate " + \
                self.getlabel() + "--->"))
        else:
            return self.pinB.getFrom().getoutput()


class UnaryGate(LogicGate):
    """描述单输入的类新增了一个输入

    Args:
        LogicGate ([type]): 继承父类逻辑门，包含标签和输出
    """
    def __init__(self, label) -> None:
        super().__init__(label)
        self.pinA = None

    def get_pin(self):
        if self.pinA == None:
            return int(input("Enter pin input for gate " + \
                self.getlabel() + "--->"))
        else:
            return self.pinA.getFrom().getoutput()


class NotGate(UnaryGate):
    """单输入门非门实现，完善了标签类中的输入方法

    Args:
        UnaryGate ([type]): 继承了单输入类
    """
    def __init__(self, label) -> None:
        super().__init__(label)

    def performGateLogic(self):
        pinA = self.get_pin()

        if pinA == 1:
            return 0
        else:
            return 1


class Addgate(BinaryGate):
    """与门实现，完善了标签类中的输入方法

    Args:
        BinaryGate ([type]): [description]
    """
    def __init__(self, label) -> None:
        super().__init__(label)

    def performGateLogic(self):
        pinA = self.get_pinA()
        pinB = self.get_pinB()

        if pinA == 1 and pinB == 1:
            return 1
        else:
            return 0


class Orgate(BinaryGate):
    """或门实现

    Args:
        BinaryGate ([type]): [description]
    """
    def __init__(self, label) -> None:
        super().__init__(label)

    def performGateLogic(self):
        pinA = self.get_pinA()
        pinB = self.get_pinB()

        if pinA == 0 and pinB == 0:
            return 0
        else:
            return 1


class And_Not_Gate(BinaryGate):
    def __init__(self, label) -> None:
        super().__init__(label)

    def performGateLogic(self):
        pinA = self.get_pinA()
        pinB = self.get_pinB()

        if pinA == 1 and pinB == 1:
            return 0
        else:
            return 1


class Connector:
    """连接器类实现，此时不但内部调用逻辑门类（has A），同时逻辑门类调用connector类本身，
    从而使逻辑门类中的pinA等编程连接器类
    """
    def __init__(self, fromgate, togate) -> None:
        self.fromgate = fromgate
        self.togate = togate

        togate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate
