import whois

def whoisQuery(target):
    query = whois.whois(target)
    print("[+]Domain: ", query.domain)
    print("[+]Update time: ", query.get('updated_date'))
    print("[+]Expiration time: ", query.get('expiration_date'))
    print("[+]Name server: ", query.get('name_servers'))
    print("[+]Email: ", query.get('emails'))