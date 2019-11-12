from tld import get_tld

# for more formats visit: @link[https://pypi.org/project/tld/]


def get_domain_name(url):
    domain_name = get_tld(url, as_object=True)
    return domain_name.fld


# print(get_domain_name('http://www.mumbaimovementacademy.com/'))
