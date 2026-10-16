import subprocess
def ping(ip):
    subprocess.run(["ping", "-c", "1", ip])
