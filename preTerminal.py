import os, sys

print 'running..'

try:
    print 'processing folder ' + sys.argv[1] + '..'
except:
    print 'please type in folder name ..'
    exit()
else:
    pass
#finally:
#    exit()

folderName = sys.argv[1]

path_tier2       = '/pnfs/desy.de/cms/tier2/store/user/zhiyuan/' 
path_preTerminal = '/nfs/dust/cms/user/hezhiyua/pre_terminal/'

#print os.path.join(path_tier2,'abc/')
#exit()

s1 = os.popen('ls ' + path_tier2 + folderName).read()
c1 = s1.split('\n')

s2 = os.popen('ls ' + path_preTerminal + folderName).read()
c2 = s2.split('\n')

for i in c2:
    print i

addDict     = {}
path_folder = {}
for i in c1:
    #print i
    tempStr = path_tier2 + folderName + '/' + i
    for j in range(4):
        if '0000' in tempStr:
            pass
        else:
            tt = os.popen('ls ' + tempStr).read()  
            ttt = tt.split('\n') 
            tempStr = tempStr + '/' + ttt[0]
    addDict[i] = tempStr
    print 'Address: '
    print addDict[i]
    path_folder[i] = path_preTerminal + folderName + '/' + i    
    if i in c2:
        print i + ' already exists..'
    else:
        os.system('mkdir ' + path_folder)
        os.system('cp -r ' + addDict[i] + ' ' + path_folder) 



for i in c1:
    if 'QCD' in i:
        outName = i[:14] + '_' + folderName[4:] + '.root'
        if 'HT50' in i:
            outName = i[:13] + '_' + folderName[4:] + '.root'
    elif 'VBFH' in i:
        outName = i[:-45] + '_' + folderName[4:] + '.root'
    print path_folder[i]
    strr     = os.popen('ls ' + path_folder[i] + '/0000' + '/*.root').read()
    fs       = strr.split('\n')
    inString = ''
    for j in fs:
        print j
        inString = inString + j + ' '
    print inString
    os.system('hadd -f ' + path_preTerminal + folderName + '/' + outName + ' ' + inString)
        
         




