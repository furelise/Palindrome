__author__ = 'URVASHI'
str1 = input("Enter a word..we will tell whether its a palindrome or not")
str1=str1.casefold();
rev = reversed(str1)


if list(str1) == list(rev):
    print("palindrome")

else:
    print("not palindrome")