import os, sys
path_tier      = '/pnfs/desy.de/cms/tier2/store/user/zhiyuan/'
folderName     = sys.argv[1]#'Brian_ntuples_v0'
delComm_file   = 'lcg-del -b -l -T srmv2 "srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN='
delComm_folder = 'lcg-del -b -d -l -T srmv2 "srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN='
print 'Address: '
print os.system('ls ' + path_tier + folderName)

path_0000 = path_tier + folderName
pathDict  = {} 
for i in range(4):
    if '0000' in path_0000:
        pass
    else:
        tm = os.popen('ls ' + path_0000).read()
        tn = tm.split('\n') 
        if tn[0]:
            path_0000 += '/' + tn[0]
            pathDict[i] = path_0000 
print path_0000
#print pathDict
path_log = path_0000 + '/log'

#"""
#--------------------------------------deleting log files:
lf       = os.popen('ls ' + path_log).read()
logFiles = lf.split('\n')
print lf

for i in logFiles:
    os.system(delComm_file + path_log + '/' + i + '"')    
os.system(delComm_folder + path_0000 + '/log"')
#"""

#"""
#--------------------------------------deleting root files:
rf        = os.popen('ls ' + path_0000).read()
rootFiles = rf.split('\n')
print rf 

for i in rootFiles:
    os.system(delComm_file + path_0000 + '/' + i + '"')
#"""

#"""
#--------------------------------------deleting empty folders:
ii = len(pathDict) 
print ii
while ii != 0:
    print pathDict[ii-1]
    os.system(delComm_folder + pathDict[ii-1] + '"')
    ii -= 1
#"""
os.system(delComm_folder + path_tier + folderName + '"')




