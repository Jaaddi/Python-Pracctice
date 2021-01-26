def fib_generator(n):
    a = 0
    b = 1
    c = 0
    print(c)
    for i in range(0, n - 1):
        a = b
        b = c
        c = a + b
        print(c)
n = int(input("Enter How many Fibconacci Number You Want?"))
fib_generator(n)
