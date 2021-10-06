from loginsystem import Loginsys

ls = Loginsys('config/config.json') #create an instance and set the config file


def main():
    print('start main func')


if __name__ == "__main__":
    username = input('Username: ')
    password = input('Password: ')
    if(ls.login(username, password) == True):
        main()
    quit()