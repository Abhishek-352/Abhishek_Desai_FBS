# Write a program to input any alphabet and check whether it is vowel or consonant. 

val=(input("Enter your alphabet: "))

if(val in ['a','e','i','o','u','A','E','I','O','U']):
    print("Alphabet is Vowel: ", val)
else:
    print("Alphabet is Consonant: ", val)
