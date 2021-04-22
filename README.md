# party-at-home
Based on [django channels](https://channels.readthedocs.io/en/stable/) [chatroom example](https://channels.readthedocs.io/en/stable/tutorial/index.html).
#### To run 
Python needs to be installed together with virtualenv.
```
$ virtualenv thorparty
$ pip install -r python\_virtualenv\_requirements.txt
```
To start the application in on a specific port and ip address, make sure the external port is fowarded to the internal one:
```
$ source bin/activate #activate virtualenv
$ python3 manage.py runserver ip-address:port
```
Also start a redis server using a docker container as a channel layer to let different websocket consumers talk to eachother.
```
$ docker run -p 6379:6379 -d redis:5
```

