import requests, json

def set_config(FileName):
    global config
    config = json.load(open(FileName))

url = config['url']

def login(username,password):
	login_data = requests.get(url).text
	account = f'{username}:{password}'
	if(account in login_data):
		print(f'Welcome {username}!') #user was successfully logged in
		return True
	elif(username in login_data):
		print('Wrong password') #wrong password
		return False
	else:
		print('User does not exist!') #user doesnt exist
		return False

if __name__ == "__main__":
	login('jaja','dwsd') #login with the example pastebin url
