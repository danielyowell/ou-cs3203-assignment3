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

def reverse(numbers):
    list2 = []
    for x in numbers:
        list2.insert(0, x)
    return list2

def main():
    inputnum = input("input an integer (or any other symbol when done): ")
    list = []
    while inputnum.isdigit():
        inputnum = int(inputnum)
        list.append(inputnum)
        inputnum = input("input an integer (or any other symbol when done): ")
    print("sum: ", sum(list))
    print("product: ", product(list))
    print("reversed list: ", reverse(list))

if __name__ == '__main__':
    main()
   
# this comment was added at the third commit for part 10 of hw3
