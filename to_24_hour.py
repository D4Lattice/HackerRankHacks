#read in some time as a string in the form '12:34:56AM'
import os
import sys

def timeConversion(s):
    #check the second from last character
    if s[-2] == "P":
        if s[0:2] == "12":
          #if a P is present and the hours = 12, no change is necessary other than to remove the 'PM' suffix
            return(s[:-2])
        else:
          #any other hours value will require +12 to switch to the 24hr format which we do and then reattach to the remaining string less 'PM'
            return(str((int(s[0:2]) + 12))+s[2:-2])
    elif s[-2] == "A":
      #if an 'AM' suffix is found simply return the value less the 'AM' or in the case of 12AM change 12 to 00
        if s[0:2] == "12":
            return("00"+s[2:-2])
        else:
            return(s[:-2])
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    fptr.write(result + '\n')
    fptr.close()
