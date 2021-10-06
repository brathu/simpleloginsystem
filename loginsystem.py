import requests, json

class Loginsys:
	def __init__(self, file_name):
		self.config = json.load(open(file_name))
		self.url = self.config['url']

	def login(self, username, password):
		login_data = requests.get(self.url).text
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
	ls = Loginsys('config/config.json') #create an instance and set the config file
	ls.login('mara','123') #login with the example pastebin url
