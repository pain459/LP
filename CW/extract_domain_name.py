import urllib.parse
import re


def domain_name(url):
    # parsed_url = urllib.parse.urlparse(url)
    # ext = tldextract.extract(url)
    # print(ext.domain)
    # print(parsed_url)
    # print(parsed_url.netloc.split('.'))
    return url.split("www.")[-1].split("//")[-1].split(".")[0]


print(domain_name("http://github.com/carbonfive/raygun"))
print(domain_name('http://www.zombie-bites.com'))
