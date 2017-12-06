import paramiko
import os
import subprocess

hostname = "Avaya-EPDEV-APP01"
password = "tomcat1"
command = "ls /tmp/"
username = "tomcat"
port = 22

source = "C:/bin/test_outage.wav"
dest = "/home/tomcat/apache-tomcat-6.0.37/webapps/audio/custom/english/test_outage.wav"
mylocaldest = "bin"

def comp(list1, list2):
    mylist = []
    for val in list1:
        val = val.strip()
        if val in list2:
            mylist.append(val)
    return mylist


try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy( paramiko.AutoAddPolicy )

    client.connect( hostname, port=port, username=username, password=password )

    stdin, stdout, stderr = client.exec_command( command )

    output = stdout.readlines()

    client.close()

    # t = paramiko.Transport( (hostname, port) )
    # t.connect( username=username, password=password )
    # sftp = paramiko.SFTPClient.from_transport(t)
    # if os.path.isfile( source ):
    #     sftp.put( source, dest )
    # else:
    #     raise IOError( 'Could not find localFile %s !!' % source )
    #
    # sftp.close()
    #
    # stdin, stdout, stderr = client.exec_command( command )
    # output = stdout.read()
    # print( "<<<<<<< After >>>>>>>" )
    # print(output)

finally:

    shell_output = os.listdir( "C:/" + mylocaldest + "/" )
    print( mylocaldest )
    print( comp( output, shell_output ) )

    # t.close()
