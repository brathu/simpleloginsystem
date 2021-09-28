# SimpleLoginSystem

A simple login system based on [pastebin.com](https://pastebin.com/) pastes as "database"

## Info
You need a [pastebin](https://pastebin.com/) account to create private pastes and to edit them (add or remove users). Its not recommended to use this for a commercially project!

## Usage
1. Import login and set_config from loginsystem and use the functions, here is an example:
```python
from loginsystem import login, set_config

set_config('config/config.json') #set the config file

def main():
    print('start main func')


if __name__ == "__main__":
    username = input('Username: ') #get username via input
    password = input('Password: ') #get password via input
    if(login(username, password) == True): #check them if true
        main() #run the main fucntion
    quit()
```
2. change the config.json to the raw of youre [pastebin](https://pastebin.com/) paste:
```json
{
    "url": "https://pastebin.com/raw/EG86YeBX"
}
```
