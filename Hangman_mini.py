import random
import time

def get_word():
    s = ['battery','correct','horse','staple','apple','mango','orange','banana','chicken','mutton','fish','winter','summer','monsoon','japan','india','china','america','africa']
    return random.choice(s)

def take_input():
    print("\nEnter a letter or the whole word ")
    return input()

def check_for_match(s,ch):
    s1=''
    for i in range(0,len(s)):
        if ch==s[i]:
            s1 += ch
        else:
            s1 += '_'
    return s1

def display(s):
    for i in range(0,len(s)):
        print(s[i],end=" ")
    print()
    
def hang(s):
    s1=''
    k=0
    a =['']
    print("YOU NEED TO GUESS A %d LETTER WORD" %len(s))
    for i in range(0,len(s)):
        s1+= '_'
        
    while s1!=s:
        ch = take_input()
        if ch==s:
            k+=1
            break
        elif 1 <len(ch) < len(s):
            print("INVALID ENTRY!! \nPLEASE")
            continue
                
        try:
            if a.index(ch):
                print("You have already guessed '%s' PLEASE TRY SOMETHING NEW!! " %ch)
        except:
            a.append(ch)
            s2 = check_for_match(s,ch)
            k+=1
            s3 =''
            for i in range(0,len(s)):
                if s1[i]!='_' or s2[i]!='_':
                    s3 += s[i]
                else:
                    s3 +='_'

            if s1 != s3:
                print("Yes! The word contains the letter '%s' " %ch)
                s1 = s3
            else:
                print("No! The word doesn't contain the letter '%s' " %ch)
            time.sleep(.5)
            display(s1)
            
    print("CONGRATULATIONS...!!! ")
    time.sleep(1)
    print("YOU DID THAT IN %d ATTEMPT(S) "%k)
    time.sleep(1)
    print("DO YOU WANT TO PLAY THE GAME AGAIN?? \nPRESS Y FOR YES AND N FOR NO ")
    if input().upper() == 'Y':
        main()
    
        
            
        
        
def main():
    print("WELCOME TO THE GAME!!! /nHANGMAN MINI IS ABOUT TO BEGIN" )
    time.sleep(.5)
    print("press any KEY to continue or E to exit")
    if input().upper() != 'E':
        hang(get_word())
    print("THANK YOU!!")

main()
