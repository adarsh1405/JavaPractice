#palindrome program in py

string=input( "Enter the string ")
default = ""
for i in string:
    default = i + default

if ( default == string):
    print(" is palindrome ")
else:
    print(" is not palindrome ")       

