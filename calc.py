'''
given_list = ["apple", "banana", "mango", "sweets"]
total = 0
for a in given_list:
    #for j in range(a + 1):
        print(a)
'''
print("Calculator is starting")
value_1, operation ,value_2 = input("Enter the two values: ").split()
value_1 = int(value_1)
value_2 = int(value_2)
#if operation == ("+"):
#    print("{} + {} = {}".format(value_1, value_2, value_1+value_2))
#elif operation == ("-"):
#    print("{} - {} = {}".format(value_1, value_2, value_1-value_2))
#elif operation == ("*"):
#    print("{} * {} = {}".format(value_1, value_2, value_1*value_2))
#elif operation == ("/"):
#    print("{} / {} = {}".format(value_1, value_2, value_1/value_2))
#elif operation == ("%"):
#    print("{} % {} = {}".format(value_1, value_2, value_1%value_2))
#else :
#    print("type a valid calculation")
# sum of value
Sum = value_1 + value_2
#difference of value
difference = value_1 - value_2
# quotient of value
quotient = value_1 / value_2
# remainder of value
remainder = value_1 % value_2
#product of value
product = value_1 * value_2
# print values
if operation == ("+"):
    print("{} + {} = {}".format(value_1, value_2, Sum))
elif operation == ("-"):
    print("{} - {} = {}".format(value_1, value_2, difference))
elif operation == ("/"):
    print("{} / {} = {}".format(value_1, value_2, quotient))
elif operation == ("%"):
    print("{] % {} = {}".format(value_1, value_2, remainder))
elif operation == ("*"):
    print("{} * {} = {}".format(value_1, value_2, product))
else :
    print("type a valid calculation")
