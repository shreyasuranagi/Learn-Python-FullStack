'''
#vowel or consonant
ch=input("Enter a character:")
if 'A'<=ch<='Z' or 'a'<=ch<='z':
    if ch in 'aeiouAEIOU':
        print("vowel")
    else:
        print("consonant")
else:
    print("not an alphabet")
'''

'''
#######
#wap to print the middle value of a list if it is a palindrome string
l=eval(input("Enter list:"))
if len(l)%2!=0:
    
    print("cond1 satisfied: middle value exists")
    
    if(type(l[len(l)//2])==type('')):
        
        print("cond2 satisifed: string present at middle")
        
        if( l[len(l)//2]==l[len(l)//2][::-1] ):
            
            print("all conditions satisfied palindrome")
        else:
            print("not a palindrome")
    else:
        print("cond2 not satisfied: not a string")
else:
    print("cond1 not satisfied: no middle value")
'''

'''
#wap to print the reversed string if it is starting with vowel and ending with special char
s=input("Enter a string:")
if s[0] in 'aeiouAEIOU':
    #if not('A'<=s[-1]<='Z' or 'a'<=s[-1]<='z' or '0'<=s[-1]<='9'):

    if not('A'<=s[-1]<='Z') and not('a'<=s[-1]<='z') and not('0'<=s[-1]<='9'):
        print(s[::-1], "starts with vowel and ends wth special character")
    else:
        print("last character is not special char")
else:
    print("not even starting with vowel")

'''   


