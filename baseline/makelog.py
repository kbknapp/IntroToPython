import random
import datetime

basedate = datetime.datetime.strptime('2014-01-01', '%Y-%m-%d')
randbyte = lambda: random.randint(0,255)
today = datetime.datetime.strptime('2014-10-14', '%Y-%m-%d')

with open('fake-log.txt','w') as log:
    while basedate <= today:
        delta = datetime.timedelta(seconds=random.randint(0,301))
        basedate = basedate + delta 
        mac = ':'.join('{:02X}'.format(randbyte()) for _ in range(6))
        ip = '.'.join('{}'.format(randbyte()) for _ in range(4))
        log.write('{},{},{}\n'.format(basedate,ip,mac))


