import os

import paramiko

host = os.environ['R510HOST']
script_path = os.environ.get('R510SCRIPTPATH')
key = paramiko.RSAKey.from_private_key_file(os.environ.get('R510KEYPATH'))


def set_auto():
	conn = paramiko.SSHClient()
	conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	print("connecting")
	conn.connect(hostname=host, username=os.environ.get('R510USERNAME'), pkey=key)
	print("connected")
	command = "sudo bash " + script_path + " auto"
	print("Executing {}".format(command))
	stdin, stdout, stderr = conn.exec_command(command)
	output = stdout.read()
	print(stdout.read())
	print("Errors")
	print(stderr.read())
	errors = stderr.read()

	conn.close()
	print("Disconnected")

	return output


def set_manual(value):
	conn = paramiko.SSHClient()
	conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	print("connecting")
	conn.connect(hostname=host, username=os.environ.get('R510USERNAME'), pkey=key)
	print("connected")
	commands = "sudo bash " + script_path + " manual && sudo bash " + script_path + " set " + str(value)
	print("Executing {}".format(commands))
	stdin, stdout, stderr = conn.exec_command(commands)
	output = stdout.read()
	print(stdout.read())
	print("Errors")
	print(stderr.read())
	errors = stderr.read()

	conn.close()
	print("Disconnected")
	return output


def get_status():
	conn = paramiko.SSHClient()
	conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	print("connecting")
	conn.connect(hostname=host, username=os.environ.get('R510USERNAME'), pkey=key)
	print("connected")
	commands = "sudo bash " + script_path + " status"
	print("Executing {}".format(commands))
	stdin, stdout, stderr = conn.exec_command(commands)
	output = stdout.read()
	errors = stderr.read()
	cleanoutput = []
	for line in output.splitlines():
		line = line.strip()
		if not line: continue
		cleanoutput.append(line.decode('UTF-8'))
	conn.close()
	print("Disconnected")
	return cleanoutput
