from socket import * # 引入socket模块
serverName = '127.0.0.1' # IP/hostname
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM) # 创建套接字。地址簇AF_INET底层网络使用IPv4，SOCK_DGRAM是一个UDP套接字，操作系统分配客户端端口号
message = input('Input lowercase sentence:')
# 将报文由字符串类型转换为字节类型，向套接字中发送字节。
clientSocket.sendto(message.encode(),(serverName, serverPort)) # 创建具有serverIP和port的数据报，经clientSocket发送
# 当一个来自因特网的分组到达该客户套接字时，该分组数据放到modifiedMessage，serverAddress包含IP和端口
modifiedMessage, serverAddress = clientSocket.recvfrom(2048) # 读数据报,缓存长度2048
print(modifiedMessage.decode()) # 将报文从字节转化为字符串
clientSocket.close() # 关闭

