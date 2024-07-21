import dns
import dns.exception
import dns.resolver
import socket

def reverse_dns(ip):
    try:
        result = socket.gethostbyaddr(ip)
    except:
        return []
    return [result[0]] + result[1]

def dns_request(domain):
    try:
        result = dns.resolver.resolve(domain, 'A')
        if result:
            print(domain)
            for answer in result:
                print(answer)
                print(f"Domain Names : {reverse_dns(answer.to_text())}")
    
    except (dns.resolver.NXDOMAIN, dns.exception.Timeout):
        return

def subdomain_search(domain, dictionary, nums):
    for word in dictionary:
        subdomain= word+"."+domain
        dns_request(subdomain)
        if nums:
            for i in range(0,10):
                s = word + str(i) + "." + domain  # example: mail[0-9].google.com
                dns_request(s)


domain = "google.com"
d = "subdomains.txt"
dictionary= []
with open(d,"r") as f:
    dictionary= f.read().splitlines()

subdomain_search(domain, dictionary, True)