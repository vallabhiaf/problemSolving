import socket
#socket is a endpoint much like a file where can we send data and recieve data from
#telnet is like socket
#Create a socket and socket lives in a computer 
#socket.socket=Make a phone 
mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#mysock.connect- dial the phone to the domain and port it may blow up if the server does not exist
mysock.connect(('data.pr4e.org',80))
#fist one is \r\n enter to new line  then we have space for any headers and then \r\n goes for execution 
#enconde to convert this to UTF-8 from python that used Unicode 
cmd='GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
#we can simulataneously send and recieve but the protocol is the that we(browser)first send(talk)
mysock.send(cmd)
#THe server now has to return soemthing 
#retrieivng thing 
while True:
    #recv is blocking/waiting operation that waits for  defined time until 512(defined characters).The delay maybe because of netowrk issue 

    data=mysock.recv(512)
    #if not data then it braks
    if len(data)< 1:
        break

    #decode from utf8 to unicode
    print(data.decode(),end='')

#u get meta data and main data 
#socket is already closed from server but we also close to not be in a state of hung
mysock.close()