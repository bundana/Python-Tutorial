# This is a function
def find_max(max_list):
    numberslist = max_list
    max_number = numberslist[0]
    for number in numberslist:
        if number > max_number:
            max_number = number
    return max_number

