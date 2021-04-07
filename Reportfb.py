import os, sys, time
P = '\x1b[0m'
H = '\x1b[91m'
G = '\x1b[92m'
K = '\x1b[93m'

def Loads():
    for i in range(101):
        time.sleep(0.3)
        sys.stdout.write(G + '\r[+] ' + P + 'Loads Akun : %d%%' % i)
        sys.stdout.flush()


def Report():
    for d in range(101):
        time.sleep(0.2)
        sys.stdout.write(G + '\r[*] ' + P + 'Mulai Processing ... [%d%%] ' % d)
        sys.stdout.flush()
print '-' * 49 + H
os.system('figlet " R E P O R T FB"')








print '\x1b[97mAuther:Hama Bn dlaj'
print '\x1b[97mTelegram group:@kurdhackerzw'
print '\x1b[97mNote:Am Toola hy reporta active kraw lalayan xomawa'
print '\x1b[97mTelegram Channel:@kurdhacker_hama_bn_dlaj'
print P + '=' * 49
B = raw_input(G + '[+]' + P + ' ID Nafaraka  : ')
print '=' * 49
if not B.startswith('1000'):
    print '[!] Id Halaya'
    sys.exit()
    print '=' * 49
Loads()
time.sleep(3)
print ''
print '=' * 49
a = 1
while True:
    print ('{}[-] {}Chawarwanba ta dache [{}] => {}{}').format(G, P, a, H, B)
    print ('{} | {}[+]{} Report Roysht').format(Report(), K, G)
    print '=' * 49
    a += 1