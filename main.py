import re
domain_list = []

with open("e-mails.txt", "r") as emails:
    input_string = emails.read()

all_domains = re.findall(r"@\w+\.\w+\b", input_string)
for domain in all_domains:
    if domain_list.count(domain) == 0:
        domain_list.append(domain)

domains = open("domains.txt", "w")

for domain in domain_list:
    domains.write(domain + "\n")

domains.close()
