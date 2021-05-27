# This is simple utility program.
def is_greatest(*params): 
    greatest_number = 0
    greater_number = 0
    for number_list in params:
        for number in number_list:
            for counter in range(0,len(number_list)):
                if int(number) <= int(number_list[counter]):
                    number = greater_number = number_list[counter]
            break
        break
    greatest_number = greater_number
    return greatest_number
print(is_greatest(input('Enter space separated numbers: ').split()))
