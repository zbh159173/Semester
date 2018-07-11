from socket import *
import os
import struct
import sys
if __name__=="__main__":
	if len(sys.argv) != 4:
		print "usage:[this program] ip port file"
		exit()
	ip = sys.argv[1]
	port = int(sys.argv[2])
	filename = sys.argv[3]
	print ip,port,filename
	ADDR = (ip,port)
	BUFSIZE = 1024
	FILEINFO_SIZE=struct.calcsize('128s32sI8s')
	sendSock = socket(AF_INET,SOCK_STREAM)
	sendSock.connect(ADDR)
	fhead=struct.pack('128s11I',filename,0,0,0,0,0,0,0,0,os.stat(filename).st_size,0,0)
	sendSock.send(fhead)
	fp = open(filename,'rb')
	while 1:
		filedata = fp.read(BUFSIZE)
		if not filedata: break
		sendSock.send(filedata)
	print "Finished Closing Connection"
	fp.close()
	sendSock.close()
	print "Connection Closed"