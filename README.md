~~~~{.python}
import ipahttp

host = 'ipamaster.example.com'
user = 'user'
passwd = 'passwd'
ipa = ipahttp.ipa(host)
ipa.login(user, passwd)
print(ipa.dnsrecord_show(dns_zone,dns_name))
~~~~
