# Search for domain names to find cool ones.
import os, sys

site_exists = lambda site: \
    os.system("whois %s.com | grep \"No match\" > /dev/null"%site) != 0

alphabet = map(chr, range(ord('a'), ord('z') + 1))

for i in alphabet:
    for j in alphabet:
        for k in alphabet:
            site_name = i + j + k
            print 'Trying', site_name
            if not site_exists(site_name):
                print '#################'
                print 'Winner!', site_name
                print '#################'
                sys.exit(0)
