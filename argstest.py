import sys
import time
import configparser
import re
#print(sys.argv[1])

#test = sys.argv[1]

#for i in range(1, len(sys.argv)):
#	print(sys.argv[i])

timestamp = "1451036965"

#转换成localtime
time_local = time.localtime(int(timestamp))
#转换成新的时间格式(2016-05-05 20:28:54)
dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
print(dt)

config = configparser.ConfigParser(allow_no_value=False)
config.read('wanteduserinfo.ini')
username =config.get('qq_info','qq_number')
print(username)
x = username.split(",")
print(x)
for i in x:
	print(i)
