# SimpleLoginSystem

A simple login system based on [pastebin.com](https://pastebin.com/) pastes as "database"

## Info
You need a [pastebin](https://pastebin.com/) account to create private pastes and to edit them (add or remove users). Its not recommended to use this for a commercially project!

## Usage
1. Import Loginsys, create an instance and set the config file, Then just use it like here:
```python
from loginsystem import Loginsys

ls = Loginsys('config/config.json') #create an instance and set the config file


def main():
    print('start main func')


if __name__ == "__main__":
    username = input('Username: ')
    password = input('Password: ')
    if(ls.login(username, password)):
        main()
    quit()
```
2. change the config.json to the raw of youre [pastebin](https://pastebin.com/) paste:
```json
{
    "url": "https://pastebin.com/raw/EG86YeBX"
}
```
