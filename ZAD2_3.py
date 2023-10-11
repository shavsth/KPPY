def intSum (list_var):
    sum = 0
    for element in list_var:
        if type(element) == int:
            sum += element
    return sum

list_a = ['a', 34, 5.6, "abcd", 5, 23, 12.234, 'h']

print("Suma elementów typu int w tablicy to: {}".format(intSum(list_a)))
