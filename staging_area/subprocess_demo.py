import subprocess

subprocess.run('ls')
subprocess.run(['ping', 'google.com'])
subprocess.run('ping google.com', shell=True)