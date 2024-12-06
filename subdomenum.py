import dns.zone
import dns.node
import dns.query

domain = str(input('Enter domain name for which to find subdomains '))
dns_server = str(input('Enter dns server ip address '))

def zone_transfer_check (domain, dns_server):
  try:
    print (f"Checking {dns_server} for zone transfer on {domain}...")
    zone = dns.zone.from_xfr(dns.query.xfr(dns_server, domain))
    if zone:
      print (f"Zone transfer available on {dns_server} !!")
      
