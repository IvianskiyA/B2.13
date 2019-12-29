FILENAME = 'dummy-access.log'

fp = open(FILENAME, encoding = 'UTF-8')
log_lines = fp.readlines()

fp.close

import collections # импортируем модуль collections
from operator import itemgetter


ip_cnt = collections.Counter()

for line in log_lines:
	for ipaddr in line.split(maxsplit=1):
		if ipaddr[0] != '-':
			ip_cnt[ipaddr] += 1

#sorted(ip_cnt, reverse = True)
min_key, min_count = min(ip_cnt.items(), key=itemgetter(1))

print('How many request from IP 79.136.245.135?', ' - ', ip_cnt['79.136.245.135'])
print('How many request from IP 127.0.0.1?', ' - ', ip_cnt['127.0.0.1'])
print('Maximum request',' - ', ip_cnt.most_common(1))
print('Minimum request',' - ', min_key, min_count)
print('Avarage count request',  sum(ip_cnt.values()) / len(ip_cnt))
