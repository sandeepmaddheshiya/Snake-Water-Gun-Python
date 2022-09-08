import random


print("___________________________________________________________")
print("|                        WELCOME                           |")
print("|                          TO                              |")
print("|               SNAKE, WATER & GUN GAME                    |")
print("|             MADE BY SANDEEP MADDHESHIYA                  |")
print("------------------------------------------------------------")


l1=["Snake","Water","Gun"]


while(True):
    i = 0
    s = 0
    c = 0
    t = 0
    while(i<5):
     r=random.choice(l1)
     n=int(input("ENTER: \n"
                 "1 FOR SNAKE \n"
                 "2 FOR WATER \n"
                 "3 FOR GUN \n"))

     if n==1 and r=="Water":
         print(f"YOU-Snake              COMPUTER-{r}")
         print("CONGRATULATIONS! YOU'VE WON")
         s+=1

     elif n==2 and r=="Gun":
        print(f"YOU-Water              COMPUTER-{r}")
        print("CONGRATULATIONS! YOU'VE WON")
        s += 1

     elif n==3 and r=="Snake":
        print(f"YOU-Gun              COMPUTER-{r}")
        print("CONGRATULATIONS! YOU'VE WON")
        s += 1

     elif n==1 and r=="Snake" or n==2 and r=="Water" or n==3 and r=="Gun":
         print(f"YOU-{r}              COMPUTER-{r}")
         print("TIE")
         t +=1

     elif n>3 or n<1:
         print("PLEASE ENTER A VALID INPUT")
         continue

     else:
        if n==1:
            print(f"YOU-Snake              COMPUTER-{r}")
        elif n==2:
            print(f"YOU-Water              COMPUTER-{r}")
        elif n==3:
            print(f"YOU-Gun              COMPUTER-{r}")

        print("YOU'VE LOSE")
        c+=1
     i+=1
     print("-------------------------------------------------")
     print("                   SCOREBOARD                    ")
     print(f"COMPUTER SCORE:{c}    TIE:{t}     YOUR SCORE:{s}")
     print("-------------------------------------------------")

    if s>c:
        print("CONGRATULATIONS! YOU'VE WON THE GAME ")
    elif s==c:
        print("GAME DRAW")
    else:
        print("BETTER TRY NEXT TIME")
    print("----------------GAME OVER---------------------")

    p=int(input("DO YOU WANT TO PLAY AGAIN? \n"
                "1 FOR YES \n"
                "2 FOR NO \n"))
    if p==1:
        continue
    elif p==2:
        break
    else:
        print("Please Enter a valid input")

print("-----------THANKS FOR PLAYING-----------")