from firebase.modules.firebaseExploit import *

def expofire():
	banner()
	print("{}[*]{} Input settings for exploit: ".format(BLUE, NORMAL))
	firebaseInstance = input("\t> Enter Firebase DB name : ")
	File = input("\t> Enter Your File Name: ")
	Name = input("\t> Enter Your Name: ")
	Nick_Name = input("\t> Enter Your Username: ")
	Email = input("\t> Enter Your Email: ")
	Message = input("\t> Enter Your Message : ")

	expofire= exploit(firebaseInstance, File, Name, Nick_Name, Email, Message)
	expofire.firebaseExploit()

if __name__ == '__main__':
	expofire()