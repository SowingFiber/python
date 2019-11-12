import os


def get_nmap(options, ip):
    cmd = os.popen('nmap ' + options + ' ' + ip)
    res = str(cmd.read())
    print(res)


get_nmap('-F', '216.58.199.174')
