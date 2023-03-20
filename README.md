# SysAid Client

## Introduction

SysAidClient is a Python library for interacting with the SysAid API (https://documentation.sysaid.com/docs/rest-api-guide). It provides an easy way to make requests to the API and handle authentication.

## Installation

To install SysAidClient, you can use `pip` or `pipenv`:

```bash
pip install git+https://github.com/DanielGumbletonWood/sysaidclient.git#egg=sysaidclient
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

# Example

```python
# Import the client
from sysaidclient import SysAidClient, ServiceRequestField

# Define the SysAid login parameters
sysaid_parameters = dict(
    account_id="my_account_id",
    username="my_username",
    password="my_password"
)

# Instantiate the client
sysaid_client = SysAidClient(**sysaid_parameters)

# Log in, which will set the JSESSIONID cookie
sysaid_client.login()

# These are all the fields in a Service Request that get populated. To see all available fields, create a service request and print the output, the fields exist in response.info.
fields = [
    ServiceRequestField(
        key="title",
        value="This is a test summary",
        valueCaption="",
        keyCaption="Summary"
    ),
    ServiceRequestField(
        key="responsibility",
        value="4",
        keyCaption="Process Manager",
        valueCaption=""
    ),
    ServiceRequestField(
        key="urgency",
        value="2",
        valueCaption="Please select urgency",
        keyCaption="Urgency"
    ),
    ServiceRequestField(
        key="description",
        value="This is a test description",
        valueCaption="",
        keyCaption="Description"
    ),
    ServiceRequestField(
        key="assigned_group",
        value="10",
        valueCaption="",
        keyCaption="Admin group"
    ),
]

# Create the service request with the given fields, status (an integer in string form), assignee (user integer ID in string form)
sysaid_client.create_service_request(
    fields=fields,
    status="2",
    assignee="1"
)

```
