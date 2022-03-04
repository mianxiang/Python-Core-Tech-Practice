from socket import socket
import time
import zmq

def run():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind('tcp://*:17000')

    cnt = 1

    while True:
        time.sleep(1)
        socket.send_string('Server hello {}'.format(cnt))
        print('Send hello {}'.format(cnt))
        cnt += 1

if __name__ == '__main__':
    run()