#return an input string with all cases swapped
#i.e. "Hello" becomes "hELLO"

def swap_case(s):
    swapped = []
    for x in s:
        if x.isalpha() and x.isupper():
            swapped.append(x.lower())
        elif x.isalpha() and x.islower():
            swapped.append(x.upper())
        else:
            swapped.append(x)
            
    swapped_string = "".join([str(item) for item in swapped])
    return swapped_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
