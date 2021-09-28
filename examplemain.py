from loginsystem import login, set_config

set_config('config/config.json')

def main():
    print('start main func')


if __name__ == "__main__":
    username = input('Username: ')
    password = input('Password: ')
    if(login(username, password) == True):
        main()
    quit()