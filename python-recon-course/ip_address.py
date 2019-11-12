import subprocess


def get_ip_address(url):
    process = subprocess.Popen(
        ["nslookup", url], stdout=subprocess.PIPE)
    output = str(process.communicate()[0]).split('\\r\\n')
    address = output[5].replace('\\t ', '')
    return address


# print(get_ip_address('google.com'))
