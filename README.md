## Introduction

Package c2d_api provide tools to interact with API of Chat2Desk. You can simply use this tools to:
- Send messages to clients
- Assign chats to different operators
- Assign tags to clients
- Get statistics
- And more actions

Full description of API you can find on the [official site](https://chat2desk.com/)

## Installation
To install package open your terminal and use command:
```sh
pip install c2d-api
```

## Getting started

After package installation you need to do import:
```sh
from c2d_api.api import *
```

Then create API object using your Chat2Desk access token:
```sh
api = Chat2DeskApi(access_token='YOUR_ACCESS_TOKEN')
```
Now you can use this object to interact with ChatToDesk API.

## Using methods
To create client you need to use code:
```sh
api.clients_post(phone='7XXXXXXXXXX', transport='YOUR_TRANSPORT', channel_id='YOUR_CHANNEL_ID', nickname='ExampleClient')
```
After client created you can send message to him:
```sh
message = 'This is example message!'
api.messages_post(client_id='CLIENT_ID', text=message)
```
You can get messages from chats. For example, if you need to get 500 messages from 'YOUR_TRANSPORT', you can use code:
```sh
api.messages_get(transport='YOUR_TRANSPORT', limit=500)
```

All methods copy the structure of API requests, so you can use the official documentation of Chat2Desk API to get them all.