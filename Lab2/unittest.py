with open("Algorithm\\LAB\\testdivide.txt", "r") as f:
    line = f.readline()
    a, b = line.split('    ')
    print(type(a))
    print(a)
    print(type(b))
    print(b)
    a = eval(a)
    b = eval(b)
