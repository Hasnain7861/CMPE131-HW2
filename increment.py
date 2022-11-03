def increment_int_a(someval):
    someval += 1
def increment_int_b(someval):
    someval[0] += 1
def main():
    a = 32
    print(increment_int_a(a))
    b = [32]
    increment_int_b(b)

    print(a)
main()