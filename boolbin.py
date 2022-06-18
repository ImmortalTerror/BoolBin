class boolbin:
    def __init__(self, boolList):
        self.boolList = boolList
        output = ""
        for i in boolList:
            if i == True:
                output += "1"
            else:
                output += "0"
        output = bin(int(output, 2))
        self.binary = output[2:]
        self.decimal = int(output, 2)

    def add(self, add):
        output = self.decimal + add
        self.binary = bin(output)[2:]
        self.decimal = output
        self.boolList = binToList(self.binary)

    def sub(self, sub):
        output = self.decimal - sub
        self.binary = bin(output)[2:]
        self.decimal = output
        self.boolList = binToList(self.binary)

    def multiply(self, multiply):
        output = self.decimal * multiply
        self.binary = bin(output)[2:]
        self.decimal = output
        self.boolList = binToList(self.binary)

    def divide(self, divide):
        output = round(self.decimal / divide)
        self.binary = bin(int(output))[2:]
        self.decimal = int(output)
        self.boolList = binToList(self.binary)


def binToList(binary):
    output = []
    binary = str(binary)[2:]
    for i in binary:
        if i == "1":
            output.append(True)
        elif i == "0":
            output.append(False)
    return output


def listToBin(list):
    output = ""
    for i in list:
        if i == True:
            output += "1"
        else:
            output += "0"
    return bin(int(output, 2))
