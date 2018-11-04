import pexpect
import sys, os
import argparse
import datetime
date          = datetime.datetime.now().strftime("%Y-%m-%d")
time          = datetime.datetime.now().strftime("%H:%M:%S")
folderName    = date # + '_' + time
print date
print time

path_beegfs   = '/beegfs/desy/user/hezhiyua/' 
path_2bBacked = '2bBacked/'
path_BU       = '/nfs/dust/cms/user/hezhiyua/BACKUP/BEE/'
comm          = 'scp -r max-wgs:'


pars = argparse.ArgumentParser()
pars.add_argument('-i',action='store',type=str)
pars.add_argument('-o',action='store',type=str)
args    = pars.parse_args()
inPath  = args.i
outPath = args.o

if inPath:  path_2bBacked = inPath  + '/'
if outPath: path_BU       = outPath + '/' 


os.system('mkdir ' + path_BU + folderName + ' \n')

process = pexpect.spawn( comm + path_beegfs + path_2bBacked + '*' + ' ' + path_BU + folderName)
process.expect(pexpect.EOF)#('bash')#('hezhiyua')#(pexpect.EOF)
process.kill(0)
print 'Back up finished.'


#process = pexpect.spawn('ssh max-wgs', timeout=60)
#process.sendline('ls')
#process.expect('hezhiyua')
#process.interact()

