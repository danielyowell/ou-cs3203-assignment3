def sum(numbers):
    sum = 0
    for x in numbers:
        sum = sum + x
    return sum

def product(numbers):
    product = numbers[0]
    for x in range(1, len(numbers)):
        product = product * numbers[x]
    return product

def main():
    inputnum = input("input an integer (or any other symbol when done): ")
    list = []
    while inputnum.isdigit():
        inputnum = int(inputnum)
        list.append(inputnum)
        inputnum = input("input an integer (or any other symbol when done): ")
    print(sum(list))
    print(product(list))

if __name__ == '__main__':
    main()