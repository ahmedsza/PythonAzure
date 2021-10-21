import socketio


socket_io = socketio.Client()


def connect_to_server(url):
    assert isinstance(url, str), 'URL should be a string --> http://localhost:3000'
    socket_io.connect(url)
# 

@socket_io.event
def connect():
    print("line 19")
    print('Connected to node.js server!')
#

@socket_io.event
def connect_error(data):
    print('Failed to connect to server.')
#

@socket_io.event
def disconnect():
    print('Disconnected from server.')
#

@socket_io.on('new transaction')
def new_transaction(new_transaction):
    print('new transactions')
    user_id = new_transaction['_id']
    print(user_id)
    
#


print("connecting to server")
connect_to_server('https://kuundahackathonapi.azurewebsites.net')
#