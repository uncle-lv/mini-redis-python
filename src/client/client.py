import socket

from loguru import logger


class Client:
    
    def __init__(self, host: str = '127.0.0.1', port: int = 6379) -> None:
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        logger.info('The client has connected at {}:{}'.format(host, port))
        
    def send(self, msg: bytes) -> int:
        logger.info('Send message: {}'.format(msg))
        return self.sock.send(msg)
        
    def recv(self, buf_size: int = 1024) -> bytes:
        return self.sock.recv(buf_size)
    
    def close(self) -> None:
        self.sock.close()
        logger.info('Client has closed.')
        

client = Client()

client.send(b'*3\r\n$3\r\nSET\r\n$5\r\nHello\r\n$5\r\nWorld\r\n')
logger.info('Receive: {}'.format(client.recv()))
    
client.close()
