import subprocess

job_names = ['ping google.com', 'ls']

for i in job_names:
    print(i)
    output = subprocess.run(i, capture_output=True, text=True)
    print(output.stdout)