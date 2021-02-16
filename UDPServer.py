from socket import * # 导入套接字模块
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM) #创建套接字类型SOCK_DGRAM(UDP)
serverSocket.bind(('',serverPort)) # 将端口号12000与该服务器套接字绑定(即分配)在一起
print("The server is ready to receive")
while True:
  message, clientAddress = serverSocket.recvfrom(2048) # 等待分组到达，读UDP报文段
  modifiedMessage = message.decode().upper()
  serverSocket.sendto(modifiedMessage.encode(), clientAddress) # 写响应到指定客户地址
