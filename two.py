import paramiko

transport = paramiko.Transport(("172.168.1.1", 22))
transport.connect(username="root")
transport.auth_none('root')
# transport.connect(username="root", password="口令", hostkey="密钥")

# 创建SSH对象,SSHClient是定义怎么传输命令、怎么交互文件
# 实例化SSHClient

client = paramiko.SSHClient()
client._transport = transport
# 打开一个Channel并执行命令


stdin, stdout, stderr = client.exec_command('df -h;cd /home;ls;sh /home/103.sh ')  # stdout 为正确输出，stderr为错误输出，同时是有1个变量有值

#文件传输
sftp = paramiko.SFTPClient.from_transport(transport)  # 如果连接需要密钥，则要加上一个参数，hostkey="密钥"

sftp.put('F:/network', '/home/101.txt')  # 将本地的Windows.txt文件上传至服务器/root/Windows.txt
#文件传输

#自加代码
f_out = open('F:/num.txt', 'r+')
a = f_out.read()
a = int(a) + 1
print(a)
f_out.seek(0)
f_out.truncate()
f_out.write(str(a))
f_out.close()
#自加结束

b=str(a)#整型转字符型
b= b.zfill(2)#不足两位前加0
print(b)
#替换字符串
infile = open("F:/network", "r+",encoding='utf-8')  #打开文件
outfile = open("F:/network1", "w",encoding='utf-8') # 内容输出
for line in infile:  #按行读文件，可避免文件过大，内存消耗
      outfile.write(line.replace('01', b))#first is old ,second is new
infile.close()    #文件关闭
outfile.close()
#替换字符串结束



# 打印执行结果
print(stdout.read().decode('utf-8'))

# 关闭服务器连接
transport.close()