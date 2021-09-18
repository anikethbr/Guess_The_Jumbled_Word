import random
import time
def picked_word():
    words=['analog','bandwidth','bluetooth','broadband','browser','cache','cybersecurity','domain','encryption','ethernet','firewall','malware','authentication','virtual','application','router']
    word_picked=random.choice(words)
    words.remove(word_picked)
    return word_picked
def jumble(word_picked):
    random.sample(word_picked,len(word_picked))
    return "".join(random.sample(word_picked,len(word_picked)))
def thank(p1n,p2n,p1,p2):
    print()
    print("".center(90,'/'))
    print(p1n,"Your Score is:",p1)
    print(p2n,"Your Score is:",p2)
    if(p1>0 and p2>0):
        if(p1>p2):
            time.sleep(2)
            print("".center(90,'-'))
            print("Congratulations..",p1n,"is the winner!")
            print("".center(90,'-'))
            time.sleep(2)
        elif(p2>p1):
            time.sleep(2)
            print("".center(90,'-'))
            print("Congratulations..",p2n,"is the winner!")
            print("".center(90,'-'))
            time.sleep(2)
        else:
            time.sleep(2)
            print("".center(90,'-'))
            print("Match Ended up in a Tie")
            print("".center(90,'-'))
    time.sleep(2)
    print("Thanks For Playing".center(100,' '))
    print("Have a nice day".center(100,' '))
    print("".center(90,'/'))
def welcome():
    print("".center(90,'-'))
    print()
    print("Welcome to Guess The Jumbled Word Game!".center(100,' '))
    print("".center(90,'-'))
    time.sleep(2)
    print("".center(90,'*'))
    print("Game Rules:".center(100,' '))
    print("=>Guess The Jumbled Word is a multiplayer game.")
    print("=>A jumbled word would be displayed on screen.")
    print("=>For each correct guess player point gets incremented by one.")
    print("".center(90,'*'))
    time.sleep(2)
    print("Lets Begin...".center(100,' '))
    print("".center(90,'_'))
    time.sleep(2)
def play():
    pp1=0
    pp2=0
    turn=0
    p1_name=input("Enter Player One Name: \n")
    p2_name=input("Enter Player Two Name: \n")
    print("".center(90,'_'))
    while(1):
        word=picked_word()
        qn =jumble(word)
        print("".center(90,'#'))
        print("The Jumbled World is:".center(100,' '))
        print(qn.center(100,' '))
        print("".center(90,'#'))
        time.sleep(2)
        if turn%2==0:
            print(p1_name,"your turn.")
            ans=input("What's on your mind?\n")
            if ans==word:
                pp1=pp1+1
                time.sleep(1)
                print("Hurrah your guess was right!!!")
                print(p1_name,"Your Score is:",pp1)
            else:
                time.sleep(1)
                print("Better Luck next time!, I thought the word:",word)
            turn+=1
            print("".center(90,'\\'))
            time.sleep(2)
            print("Do you wish to continue playing?")
            print("Press 1 to continue")
            print("Press 0 to exit")
            c=int(input())
            if(c==0):
                thank(p1_name,p2_name,pp1,pp2)
                break
        else:
            print(p2_name,"your turn.")
            ans=input("What's on your mind?\n")
            if ans==word:
                pp2=pp2+1
                time.sleep(1)
                print("Hurrah your guess was right!!!")
                print(p2_name,"Your Score is:",pp2)
            else:
                time.sleep(1)
                print("Better Luck next time!, I thought the word:",word)
            turn+=1
            print("".center(90,'\\'))
            time.sleep(2)
            print("Do you wish to continue playing?")
            print("Press 1 to continue")
            print("Press 0 to exit")
            c=int(input())
            if(c==0):
                thank(p1_name,p2_name,pp1,pp2)
                break
welcome()
play()

