list_a = ['a', 34, 5.6, "abcd", 5, 23, 12.234, 'h']

def intSum (list_var):
    sum = 0
    for element in list_a:
        if type(element) == int:
            sum += element
    return sum

print("Suma elementów typu int w tablicy to: {}".format(intSum(list_a)))
