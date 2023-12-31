# BlockDef
A Blockchain Based Web-Client For Secured Defence File Management Concept

[![Python](http://forthebadge.com/images/badges/made-with-python.svg)](https://python.org)
[![GitHub](https://forthebadge.com/images/badges/built-by-developers.svg)](https://github.com/)

[![Issues](https://img.shields.io/github/issues/AsmSafone/SafoneAPI?style=for-the-badge&color=orange)](https://github.com/adnansami1992sami/BlockDef/issues)
[![Forks](https://img.shields.io/github/forks/AsmSafone/SafoneAPI?style=for-the-badge&color=orange)](https://github.com/adnansami1992sami/BlockDef/fork)
[![Stars](https://img.shields.io/github/stars/AsmSafone/SafoneAPI?style=for-the-badge&color=orange)](https://github.com/adnansami1992sami/BlockDef/)
[![LICENSE](https://img.shields.io/github/license/AsmSafone/SafoneAPI?color=orange&style=for-the-badge)](https://github.com/adnansami1992sami/BlockDef)
[![Contributors](https://img.shields.io/github/contributors/AsmSafone/SafoneAPI?style=for-the-badge&color=orange)](https://github.com/adnansami1992sami/BlockDef)

## Installation system:

### Activate python virtual env:
```sh
$ 'virtualenv -p python3 env'
```
Write 'cd env' to enter the env. Now in env folder install the files.

### Install required libraries:

```sh
1) go def folder
2)pip install -r requirements.txt 
```

## Running process:
```sh
1) config the database in "config/settings.py"
2) in terminal give command "python main.py makemigrations"
3) "python main.py migrate"
4) "python main.py collectstatic"
4) Create superuser by "python main.py createsuperuser"
5)"python main.py runserver"
```

## IPFS MANAGEMENT

```sh
1) Go to defence/views.py
2) Create a account in "https://www.infura.io/"
3) Now Enter the App Secrets And App Keys into "api_secrets" and in "api_keys" in views.py
```

## Usage
```sh
1) Enter into "http://localhost:8080/admin"
2) Login with Administrator account.
3) Add new User wuth Role militarypersonnal and controlcenter
```
