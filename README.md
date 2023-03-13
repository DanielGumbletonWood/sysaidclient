
# SysAid Client

## Introduction 
SysAidClient is a Python library for interacting with the SysAid API (https://documentation.sysaid.com/docs/rest-api-guide). It provides an easy way to make requests to the API and handle authentication. 

## Installation 
To install SysAidClient, you can use `pip`: 
```bash pip install git+https://github.com/DanielGumbletonWood/sysaidclient.git 
``` 
Alternatively, you can download the source code from GitHub and install it manually. 

## Usage 
Using SysAidClient is simple. First, you need to create an instance of the `SysAidClient` class, passing in your account ID, username and password: 
```python 
from sysaidclient import SysAidClient 

sysaid_parameters = dict(
    account_id="my_account_id", 
    username="my_username", 
    password="my_password"
)

sysaid_client = SysAidClient(**sysaid_parameters)  
```  
Then, you need to log in with `sysaid_client.login()`. Once logged in, you can make requests using `sysaid_client.request_united()`, passing in the HTTP method, endpoint and any headers or payloads as necessary. For example:  
```python  
response = sysaid_client.request_united(method="GET", endpoint="/users")  
```  