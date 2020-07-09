import numpy as np
def Q1_sum_of_numbers_below_1000():  
    sum_three = 3 * ((999//3)  *  ((999//3)+1))/2 # sum of all numbers less than 1000 that divides 3 
    sum_five  = 5 * ((999//5)  *  ((999//5)+1))/2 # sum of all numbers less than 1000 that divides 5
    gcd_three_and_five = -15 * ((999//15) * ((999//15)+1))/2 # sum of all numbers less than 1000 with gcd(3,5)
    total_sum = sum_three + sum_five + gcd_three_and_five
    return total_sum

def Q2_Palindrome_permutation(input_string):
    input_string = input_string.replace(" ", "")
    input_string = input_string.lower()
    d = dict()
    for i in input_string:
        if i in d:
            d[i] +=1
        else:
            d[i] =1
    odd_count = 0
    for k,v in d.items():
        if v % 2 != 0:
            if odd_count == 0: 
                odd_count += 1
            else: 
                return False
    return True

def Q3_unique_characters(input_string):
    if len(input_string) > 128:
        return False
    data = 0
    for c in input_string:
        offset_tmp = ord(c) - ord('a') # returns unicode of character
        mask = 1 << offset_tmp
        if mask & data:
            return False
        else:
            data = data | mask
    return True
def Q4_count_possible_ways(n):
    number_of_ways = [0] * (n + 1) 
    number_of_ways[0] = 1
    number_of_ways[1] = 1
    number_of_ways[2] = 2
    for i in range(3, n + 1) : 
        number_of_ways[i] = number_of_ways[i - 1] + number_of_ways[i - 2] + number_of_ways[i - 3] 
      
    return number_of_ways[n] 




def main():
    print(Q1_sum_of_numbers_below_1000())
    print(Q2_Palindrome_permutation("This is not a palindrome permuatation"))
    print(Q3_unique_characters("Banana"))
    print(Q4_count_possible_ways(3))

if __name__== "__main__" :
    main()
