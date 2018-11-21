#1. Verify if an roman number is valid
#2. sort an array of roman numbers 
import re
import collections

#is it a valid Roman number
def isRoman(inputRoman):
    thousand = r'M{0,3}'
    hundred = r'(C[MD]|D?C{0,3})'
    ten = r'(X[CL]|L?X{0,3})'
    digit = r'(I[VX]|V?I{0,3})'
    result = bool(re.match(thousand+ hundred+ten+digit+'$', inputRoman.upper()))
    return result


def romanToint(roman_num):
    #print roman_num
    nums = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    while(isRoman(roman_num)):
        sum = 0
        for i in range(len(roman_num)):
            value = nums[roman_num[i]]
            if i+1 < len(roman_num) and nums[roman_num[i+1]] > value:
                sum -= value
            else: sum += value
        return sum
        
    

#sort roman numbers in an array 
def sortRoman(inputArray):
    intValue = []
    intdict = {}
    for roman in inputArray:
        integer = romanToint(roman)
        intdict[integer] = roman
    print intdict
    od = collections.OrderedDict(sorted(intdict.items()))
    print od
       
    
        
    


#inputArray = ["MMMDCCCLXXXVIII","IV","VII","X","CCD"]
inputArray = ["CDXXI", "X", "VIII", "XIII"]
sortRoman(inputArray)


#result = isRoman('vii')
#print result
