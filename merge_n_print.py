#given string s and factor k split s in to k-many substrings
#e.g. s=Hello, k=2   - >      He, ll, o
#then reduce each substring so that each character only appears once
#He , ll , o   - >  He, l, o

def merge_the_tools(string, k):
    set_subs = []  
            
    for x in range(0,len(string)//k):
        #appends each subset of length k but first converting
        #to a dictionary to remove any repeated figures
        set_subs.append(list(dict.fromkeys(string[x*k:(x*k)+k])))
        
    for y in set_subs:  
        print("".join(y))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
