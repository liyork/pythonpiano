from socket import *
serverName = '127.0.0.1'
serverPort = 12000
# 创建客户套接字，AF_INET指示底层网络使用IPv4，SOCK_STREAM指示该套接字类型，表明是一个TCP套接字，操作系统为客户套接字指定端口
clientSocket = socket(AF_INET, SOCK_STREAM)
# 执行三次握手，创建TCP连接
clientSocket.connect((serverName, serverPort))
sentence = input('Input lowercase sentence:')
# 并未向UDP显示地创建一个分组并为该分组附上目的地址
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From Server: ', modifiedSentence.decode())
# 关闭连接，引起客户中的TCP向服务器中的TCP发送一条TCP报文
clientSocket.close()
