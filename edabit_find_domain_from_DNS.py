from socket import gethostbyaddr as domain_from_ip
def get_domain(ip_address):
    return domain_from_ip(ip_address)[0]

print(get_domain("38.242.217.83"))
print(type(get_domain("38.242.217.83")))