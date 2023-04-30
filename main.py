import importlib

required_packages = ['os', 'sys', 'random', 'time', 'platform', 'tqdm', 'emoji']
for package in required_packages:
    try:
        importlib.import_module(package)
    except ImportError:
        
        print(f"{package} is not installed.")
        os.system(f"pip install ",package)
        sys.exit()

import sys
import os
import random 
import time
import platform
import tqdm
import emoji
from tqdm import tqdm
import platform
import time
import random
import sys
import os
import emoji

platforms = platform.system()


def check_git_clone():
    result = os.system("git --version")
    return result == 0


def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
        print("Only for linux or other")
        sys.exit()
    else:
        os.system("clear")


def jailbreak():
    os.system("git clone https://github.com/GiuCoder/ChatGPT-JAILBREAK-CAN-.git")


def hide():
    # Run git clone command
    os.system("git clone https://github.com/GiuCoder/HideYourSelf.git")

    # Change directory to HideYourSelf
    os.chdir("HideYourSelf")

    # Set execute permission on hidemyip.sh
    os.system("chmod +x hidemyip.sh")
    
    # Move hidemyip.sh to /usr/bin/
    os.system("sudo mv hidemyip.sh /usr/bin/")
    
    


def secure():

    # Clone the SecureTheLinux repository
    os.system("git clone https://github.com/GiuCoder/SecureTheLinux.git")

    # Change to the SecureTheLinux directory
    os.chdir("SecureTheLinux")

    # Set the execute permission for the securethelinux.sh script
    os.system("chmod +x securethelinux.sh")

    # Run the securethelinux.sh script
    os.system("./securethelinux.sh")


def ddos():

    # Install required packages
    os.system("sudo apt-get install git python3 python3-pip")

    # Clone the DDoS-Tools-GOLDER-ATTACK repository
    os.system("git clone https://github.com/GiuCoder/DDoS-Tools-GOLDER-ATTACK.git")

    # Navigate to the cloned repository
    os.chdir("DDoS-Tools-GOLDER-ATTACK")

    # Install required Python packages
    os.system("sudo pip3 install -r requirements.txt")

    # Run the ddos_web.py script with the -h flag to show help information
    os.system("python3 ddos_web.py -h")


def ipscanner():

    # Install dependencies
    os.system("apt-get install git python3 python3-pip")

    # Clone the repository
    os.system("git clone https://github.com/GiuCoder/Advance-IP-Scanner.git")

    # Change to the cloned directory
    os.chdir("Advance-IP-Scanner")

    # Run the scanner
    os.system("python3 scanner.py")


def installer():
    try:
        os.system("sudo apt-get update")
        result = os.system("wine --version")
        if result != 0:
            print("Wine not found, installing...")
            os.system("sudo apt-get install git python3-pip python3")
            os.system(
                "sudo apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ hirsute main'")
            os.system("wget -nc https://dl.winehq.org/wine-builds/winehq.key")
            os.system("sudo apt-key add winehq.key")
            os.system("sudo apt-get install --install-recommends winehq-stable")
            os.system("sudo apt-get install --install-recommends winehq-stable")
        else:
            # Install required packages
            os.system('sudo apt-get install git python3')

            # Clone the repository
            os.system(
                'git clone https://github.com/GiuCoder/Python3-Java-Git-NodeJS-Installer.git')

            # Change directory to the cloned repository
            os.chdir('Python3-Java-Git-NodeJS-Installer')

            # Run the installer script
            os.system('wine installer.bat')
    except Exception as e:
        print("Error: ", e)


def gatherinformationweb():
    os.system("apt-get install git")
    os.system(
        "git clone https://github.com/GiuCoder/WebsiteGatheringInformation.git")
    os.system("cd WebsiteGatheringInformation")
    os.system("apt-get install python3")
    os.system("clear")
    os.system("pip install emoji termcolor emojize validators")
    os.system("clear")
    os.system("python3 main.py")


def ipinfo():
    os.system('clear')
    os.system('apt-get update && upgrade')
    os.system('sudo apt-get install git python3 python3-pip')
    os.system('clear')
    os.system('git clone https://github.com/GiuCoder/INFORMATION-IP-GATHERING.git')
    os.system('clear')
    os.chdir('INFORMATION-IP-GATHERING')
    os.system('clear')
    os.system('pip install -r requirements.txt')
    os.system('clear')
    os.system('python3 main.py')


# Map user input to corresponding function
function_map = {
    "1": jailbreak,
    "2": hide,
    "3": secure,
    "4": ddos,
    "5": ipscanner,
    "6": installer,
    "7": gatherinformationweb,
    "8": ipinfo
}

# Define the main function


def main():
    clear_screen()
    print(f"\033[1;36;40mWelcome to GiuCoder tool downloader on Github\033[0m\n\n\033[1;33;40m1. ChatGPT-JAILBREAK-CAN\n2. HideYourSelf\n3. SecureTheLinux\n4. DDoS-Tools-GOLDER-ATTACK\n5. Advance-IP-Scanner\n6. Python3-Java-Git-NodeJS-Installer\n7. WebsiteGatheringInformation\n8. INFORMATION-IP-GATHERING\n\033[0m")

    choice = input("\033[1;32;40m>> \033[0m")
    if choice in function_map:
        clear_screen()
        function_map[choice]()
    else:
        print(f"{emoji.emojize(':exploding_head:')} \033[1;31;40mInvalid choice!\033[0m")
        input("\033[1;32;40mPress ENTER to continue ...\033[0m")


# Start the program
while True:
    try:
        clear_screen()
        if check_git_clone():
            print("\033[1;34;40mChecking GitHub ... \033[0m")
            for _ in tqdm(range(100), desc="\033[1;34;40mLoading\033[0m", leave=False):
                time.sleep(random.uniform(0.01, 0.1))
            main()
        else:
            print(
                f"{emoji.emojize(':exploding_head:')}\033[1;31;40mCan't run Git\nPlease download or check your internet connection and try again!\033[0m")
            sys.exit()
    except KeyboardInterrupt:
        clear_screen()
        print(f"{emoji.emojize(':exploding_head:')}\033[1;32;40mGoodbye!\033[0m")
        sys.exit()
    except Exception as e:
        print(f"{emoji.emojize(':exploding_head:')}Error: ", e)
