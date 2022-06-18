import boolbin


def main():
    stuff = boolbin.binToList(bin(3825))
    stuff = boolbin.boolbin(stuff)
    print(stuff.binary)
    print(stuff.decimal)
    print(stuff.boolList)
    print("\n")

    stuff.add(284)
    print(stuff.binary)
    print(stuff.decimal)
    print(stuff.boolList)
    print("\n")

    stuff.sub(25)
    print(stuff.binary)
    print(stuff.decimal)
    print(stuff.boolList)
    print("\n")

    stuff.multiply(2)
    print(stuff.binary)
    print(stuff.decimal)
    print(stuff.boolList)
    print("\n")

    stuff.divide(4)
    print(stuff.binary)
    print(stuff.decimal)
    print(stuff.boolList)


if __name__ == "__main__":
    main()
