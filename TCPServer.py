from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
# 将服务器的端口号与该套接字关联,serverSocket是欢迎套接字
serverSocket.bind(('',serverPort))
# 监听TCP连接请求，参数定义了请求连接的最大数(至少为1)
serverSocket.listen(1)
print('The server is ready to receive')
while True:
  # 有客户连接，创建connectionSocket新套接字，由此特定客户专用，完成三次握手
  connectionSocket, addr = serverSocket.accept()
  sentence = connectionSocket.recv(1024).decode()
  capitalizedSentence = sentence.upper()
  connectionSocket.send(capitalizedSentence.encode())
  connectionSocket.close()
