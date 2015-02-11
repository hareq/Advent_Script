from java.io import FileInputStream,FileOutputStream,IOException
from java.lang import Throwable,Exception,String,System
from jarray import zeros
from java.util.zip import GZIPOutputStream,ZipOutputStream,ZipFile,ZipEntry
from jarray import array
from java.lang import String
from java.lang import Thread
def ftp_config():
    f = open('C:\config.dcb','r')
    str = f.read()
    m = len(str)
    for n in range(0,m):
        f.seek(n)
        t = f.read(7)
        if t == "neaip='":
            n = f.tell()
            nn = 0
            while "'" != f.read(1):
                nn = nn+1
            f.seek(n)
            neaip = f.read(nn)
            mgrName = neaip
        f.seek(n)
        t = f.read(7)
        if t == "ftpip='":
            n = f.tell()
            nn = 0
            while "'" != f.read(1):
                nn = nn+1
            f.seek(n)
            ftpip = f.read(nn)
        f.seek(n)
        t = f.read(13)
        if t == "ftpuserName='":
            n = f.tell()
            nn = 0
            while "'" != f.read(1):
                nn = nn+1
            f.seek(n)
            ftpuserName = f.read(nn)
        f.seek(n)
        t = f.read(13)
        if t == "ftppassword='":            
            n = f.tell()
            nn = 0
            while "'" != f.read(1):
                nn = nn+1
            f.seek(n)
            ftppassword = f.read(nn)
    return mgrName,ftpip,ftpuserName,ftppassword

def gzip(src,dist):
    try:
        fin = FileInputStream(src);
        fout = FileOutputStream(dist);
        gzout = GZIPOutputStream(fout);
        buf = zeros(1024,'b')
        num = 0;
        num = fin.read(buf)
        while num != -1 :
            gzout.write(buf, 0, num);
            num = fin.read(buf)
        gzout.close();
        fout.close();
        fin.close();
    except Exception,ex:
        'This is Exception is %s' % ex

def zip2(src,dist):
    buf = zeros(32768,'b')
    try:
        out = ZipOutputStream(FileOutputStream(dist));	
        fin = FileInputStream(src);
        out.putNextEntry(ZipEntry(src));
        len = fin.read(buf);
        while len != -1:
            out.write(buf, 0, len);
            len = fin.read(buf);
        out.flush();	    
        out.closeEntry();
        fin.close();
        out.close();
    except Exception,ex:
        'This is Exception is %s' % ex

def write_dynamicDate(enodebid):
    enodebidiod = scriptinterface.getSnmpOidForNodeName(enodebip,161,'nodeBSysFunctionId')
    reenodebidiod = enodebidiod+'.0'+'</i><r>'

    nodeBGlobalIdoid = scriptinterface.getSnmpOidForNodeName(enodebip,161,'nodeBGlobalId')
    renodeBGlobalIdoid = nodeBGlobalIdoid+'.0'+'</i><r>'

    nodeBSysOMAddroid = scriptinterface.getSnmpOidForNodeName(enodebip,161,'nodeBSysOMAddr')
    renodeBSysOMAddroid = nodeBSysOMAddroid+'.0'+'</i><r>'

    print 'Start write_dynamicDate()'
    enodebidox = enodebid
    iienodebidox = int(enodebidox)    
    t = hex(iienodebidox)
    numt = len(t)
    
    if numt <= 6:
        t = t[2:numt]
        numt = len(t)
        numt = 4-numt
        o=1
        while o <= numt:
            t = '0'+t
            o = o+1
            enodebidox = t

    if numt > 6:
        numt1 = numt-4
        t1 = t[numt1:numt]
        numt = numt-4
        t = t[2:numt]
        numt = len(t)
        numt = 4-numt
        o = 1
        while o <= numt:
            o = o+1
        t = t+t1
        enodebidox = t    
    
    NodeBFunction = enodebidox
    nodeBSysFunctionId = enodebid
    nodeBGlobalId = enodebid



    f = open('C:\dynamicDate110.dcb','r+')
    dynamicDate110 = f.read()
    dynamicDate110 = dynamicDate110.replace('<sn>NodeBFunction=','<sn>NodeBFunction='+enodebidox)
    dynamicDate110 = dynamicDate110.replace('<nedn>NodeBFunction=','<nedn>NodeBFunction='+enodebidox)

    
    f.close()

    f1 = open(dcb,'w+')
    f1.write(dynamicDate110)
    f1.close()
    

     
    zipname = 'dynamicDate'+enodebid+'.gzip'
    gzip(dcb,zipname)
    print "jjjjjj",enodebid
    return zipname



def write_staticDate(enodebid):
    enodebidiod = scriptinterface.getSnmpOidForNodeName(enodebip,161,'nodeBSysFunctionId')
    reenodebidiod = enodebidiod+'.0'+'</i><r>'

    nodeBGlobalIdoid = scriptinterface.getSnmpOidForNodeName(enodebip,161,'nodeBGlobalId')
    renodeBGlobalIdoid = nodeBGlobalIdoid+'.0'+'</i><r>'

    nodeBSysOMAddroid = scriptinterface.getSnmpOidForNodeName(enodebip,161,'nodeBSysOMAddr')
    renodeBSysOMAddroid = nodeBSysOMAddroid+'.0'+'</i><r>'

    print 'Start write_staticDate()'
    enodebidox = enodebid
    iienodebidox = int(enodebidox)    
    t = hex(iienodebidox)
    numt = len(t)
    
    if numt <= 6:
        t = t[2:numt]
        numt = len(t)
        numt = 4-numt
        o=1
        while o <= numt:
            t = '0'+t
            o = o+1
            enodebidox = t

    if numt > 6:
        numt1 = numt-4
        t1 = t[numt1:numt]
        numt = numt-4
        t = t[2:numt]
        numt = len(t)
        numt = 4-numt
        o = 1
        while o <= numt:
            o = o+1
        t = t+t1
        enodebidox = t    
    
    NodeBFunction = enodebidox
    nodeBSysFunctionId = enodebid
    nodeBGlobalId = enodebid



    f = open('C:\staticDate110.dcb','r+')
    staticDate110 = f.read()

    staticDate110 = staticDate110.replace(reenodebidiod,reenodebidiod+enodebid)
    staticDate110 = staticDate110.replace(renodeBGlobalIdoid,renodeBGlobalIdoid+enodebid)
    staticDate110 = staticDate110.replace(renodeBSysOMAddroid,renodeBSysOMAddroid+enodebip)
    staticDate110 = staticDate110.replace('<sn>NodeBFunction=','<sn>NodeBFunction='+enodebidox)
    staticDate110 = staticDate110.replace('<nedn>NodeBFunction=','<nedn>NodeBFunction='+enodebidox)

    
    f.close()

    f1 = open(dcb,'w+')
    f1.write(staticDate110)
    f1.close()
    

    zipname = 'staticDate'+enodebid+'.gzip'
    gzip(dcb,zipname)
    return zipname

def from_filetrap_get_enodebid():
    fileTransDestoid = scriptinterface.getSnmpOidForNodeName(enodebip,161,'fileTransDest')
    enodebid = scriptinterface.getNodeValue(fileTransDestoid,FileInstance)
    enodebidlen = len(enodebid)
    for enodebidn in range(0,enodebidlen):
        if enodebid[enodebidn] == '/':
            enodebid1 = enodebid[7:enodebidn]
    enodebid = enodebid1
    return enodebid


def get_enodebip():
    enodebip = scriptinterface.getSnmpIPAddress()
    return enodebip
    
def get_FileInstance():
    FileoidInstance = scriptinterface.getCurrentOIDWithInstance()
    FileOID = scriptinterface.getCurrentOID()
    FileInstance = FileoidInstance.replace(FileOID,'')
    return FileInstance


def from_NodeName_get_enodebid():
    nodeBSysFunctionIdoid = scriptinterface.getSnmpOidForNodeName(enodebip,161,'nodeBSysFunctionId')
    enodebid = scriptinterface.getNodeValue(nodeBSysFunctionIdoid,'.0')
    return enodebid

def softdownload(softpathandname,fileTransFileName):
    print softpathandname
    print fileTransFileName
    scriptinterface.downloadFile(ftpconfigvlue[ftpip], 21, softpathandname, fileTransFileName,1, "ftp", ftpconfigvlue[ftpuserName], ftpconfigvlue[ftppassword]);
    


def getSoftwareVersion(localsoftpathandname):
    f = open(localsoftpathandname,'r')
    str = f.read(50)
    softname = str[16:46]
    f.close()
    print 'softname =',softname
    return softname

    

print 'Robotization Start'

mgrName = 0
ftpip = 1
ftpuserName = 2
ftppassword = 3


trapOID = ".1.3.6.1.4.1.5105.80.1.6.2.7"
eventtrapOID = ".1.3.6.1.4.1.5105.80.1.6.2.1"

enodebip = get_enodebip()
print 'enodebip =',enodebip

ftpconfigvlue = ftp_config()
FileInstance = get_FileInstance()

fileTransTrapNEIDoid = scriptinterface.getSnmpOidForNodeName(enodebip,161,'fileTransTrapNEID')
fileTransTrapTaskIDoid = scriptinterface.getSnmpOidForNodeName(enodebip,161,'fileTransTrapTaskID')
fileTransTrapTypeoid = scriptinterface.getSnmpOidForNodeName(enodebip,161,'fileTransTrapType')
fileTransTrapNameoid = scriptinterface.getSnmpOidForNodeName(enodebip,161,'fileTransTrapName')
fileTransTrapFlagoid = scriptinterface.getSnmpOidForNodeName(enodebip,161,'fileTransTrapFlag')
fileTransTrapResultoid = scriptinterface.getSnmpOidForNodeName(enodebip,161,'fileTransTrapResult')
fileTransTrapBytesoid = scriptinterface.getSnmpOidForNodeName(enodebip,161,'fileTransTrapBytes')
fileTransTrapTimeoid = scriptinterface.getSnmpOidForNodeName(enodebip,161,'fileTransTrapTime')
fileTransFileNameoid = scriptinterface.getSnmpOidForNodeName(enodebip,161,'fileTransFileName')
Filetaskidoid = scriptinterface.getSnmpOidForNodeName(enodebip,161,'fileTransID')

Filetaskid = scriptinterface.getNodeValue(Filetaskidoid,FileInstance)
fileTransFileName = scriptinterface.getNodeValue(fileTransFileNameoid,FileInstance)
fileTransDestoid = scriptinterface.getSnmpOidForNodeName(enodebip,161,'fileTransDest')
fileTransDest = scriptinterface.getNodeValue(fileTransDestoid,FileInstance)
softpathandname = fileTransDest + '/'+fileTransFileName

objectid = array([fileTransTrapNEIDoid+FileInstance,fileTransTrapTaskIDoid+FileInstance,fileTransTrapTypeoid+FileInstance,fileTransTrapNameoid+FileInstance,fileTransTrapFlagoid+FileInstance,fileTransTrapResultoid+FileInstance,fileTransTrapBytesoid+FileInstance,fileTransTrapTimeoid+FileInstance],String)
nodetypes = array(["Gauge","Gauge","Integer","String","Integer","Integer","Gauge","String"],String)


fileTransTypeoid = scriptinterface.getSnmpOidForNodeName(enodebip,161,'fileTransType')
value = scriptinterface.getNodeValue(fileTransTypeoid,FileInstance)
value = int(value)
##Filetaskid = FileInstance[1]



if (value == 15):
    print 'Start staticDate_fileupaaa'
    enodebid = from_filetrap_get_enodebid()
    dcb = 'staticDate'+enodebid+'.dcb'
    e = 'true';
    try:
        f = open(dcb,'r')
        f.close()
    except :
        e = 'false'
        
    if e == 'true':
        zipname = 'staticDate'+enodebid+'.gzip'
        gzip(dcb,zipname)  

    if e == 'false':
        print 'Have no file,goto write_staticDate()'
        zipname = write_staticDate(enodebid)
        
    fileTransTrapName = 'eNodeB='+enodebid+'/FullCfg/'+zipname
    scriptinterface.uploadFile(ftpconfigvlue[ftpip], 21, zipname, fileTransTrapName,1, "ftp", ftpconfigvlue[ftpuserName], ftpconfigvlue[ftppassword]);
    
    values = array([enodebid,Filetaskid,"15",fileTransTrapName,"1","0","1","2011-11-11 11:11:11"],String)
    scriptinterface.sendV2Trap(ftpconfigvlue[mgrName],162,"public",trapOID,objectid,nodetypes,values)
    enodebidiod = scriptinterface.getSnmpOidForNodeName(enodebip,161,'nodeBSysFunctionId')
    enodebidobjectId = enodebidiod
    instance = ".0"
    enodebvalue = enodebid
    scriptinterface.updateValue(enodebidobjectId,instance,enodebvalue,"CONST")

 
if (value == 13):
    print 'Start filedown'
    enodebid = from_filetrap_get_enodebid()    
    values =  array([enodebid,Filetaskid,"13",'nb.cfg',"2","0","1","2011-11-11 11:11:11"],String)
    scriptinterface.sendV2Trap(ftpconfigvlue[mgrName],162,"public",trapOID,objectid,nodetypes,values)
    values =  array([enodebid,"53","1","eventGeneralEventSource","eNB Static startup","2011-11-11 11:11:11"],String) 
    eventGeneralEventNodeBSysFunctionIdoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'eventGeneralEventNodeBSysFunctionId')
    eventGeneralEventTypeoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'eventGeneralEventType')
    eventGeneralEventResultoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'eventGeneralEventResult')
    eventGeneralEventSourceoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'eventGeneralEventSource')
    eventGeneralEventAdditionInfooid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'eventGeneralEventAdditionInfo')
    eventGeneralEventOccurTimeoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'eventGeneralEventOccurTime')
    eventobjectid = array([eventGeneralEventNodeBSysFunctionIdoid+FileInstance,eventGeneralEventTypeoid+FileInstance,eventGeneralEventResultoid+FileInstance,eventGeneralEventSourceoid+FileInstance,eventGeneralEventAdditionInfooid+FileInstance,eventGeneralEventOccurTimeoid+FileInstance],String)
    eventnodetypes = array(["Integer","Integer","Integer","String","String","String"],String)
    scriptinterface.sendV2Trap(ftpconfigvlue[mgrName],162,"public",eventtrapOID,eventobjectid,eventnodetypes,values)
    
if (value == 16):
    print 'Start dynamicDate_fileup '
    enodebid = from_filetrap_get_enodebid()
    dcb = 'dynamicDate'+enodebid+'.dcb'
    e = 'true';
    try:
        f = open(dcb,'r')
        f.close()
    except :
        e = 'false'
        
    if e == 'true':
        dynamicDate_zipname = 'dynamicDate'+enodebid+'.gzip'
        gzip(dcb,dynamicDate_zipname)
        
    if e == 'false':
        print 'Have no file,goto write_staticDate()'
        dynamicDate_zipname = write_dynamicDate(enodebid)

    fileTransTrapName = "eNodeB="+enodebid+"/Dynamic/"+dynamicDate_zipname
    print "kkkkkk",dynamicDate_zipname
    scriptinterface.uploadFile(ftpconfigvlue[ftpip], 21, dynamicDate_zipname, fileTransTrapName,1, "ftp", ftpconfigvlue[ftpuserName], ftpconfigvlue[ftppassword]);          
    values = array([enodebid,Filetaskid,"16",fileTransTrapName ,"1","0","1","2011-11-11 11:11:11"],String)
    scriptinterface.sendV2Trap(ftpconfigvlue[mgrName],162,"public",trapOID,objectid,nodetypes,values)

if (value == 6):
    print 'Start softfiledown'
    enodebid = from_NodeName_get_enodebid()
    values = array([enodebid,Filetaskid,"6",'fileTransTrapName',"2","0","1","2011-11-11 11:11:11"],String)
    trapOID = ".1.3.6.1.4.1.5105.80.1.6.2.7"
    objectid = array([fileTransTrapNEIDoid+FileInstance,fileTransTrapTaskIDoid+FileInstance,fileTransTrapTypeoid+FileInstance,fileTransTrapNameoid+FileInstance,fileTransTrapFlagoid+FileInstance,fileTransTrapResultoid+FileInstance,fileTransTrapBytesoid+FileInstance,fileTransTrapTimeoid+FileInstance],String)
    nodetypes = array(["Gauge","Gauge","Integer","String","Integer","Integer","Gauge","String"],String)
    Thread.currentThread().sleep(5*1000)
    scriptinterface.sendV2Trap(ftpconfigvlue[mgrName],162,"public",trapOID,objectid,nodetypes,values)
    
    softdownload(softpathandname,fileTransFileName)
    softname = getSoftwareVersion(fileTransFileName)

    
    configChgTrapOID = ".1.3.6.1.4.1.5105.80.1.6.1.3"
    configChgTrapNeTypeoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'configChgTrapNeType')
    configChgTrapNEIDoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'configChgTrapNEID')
    configChgTrapTimeoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'configChgTrapTime')
    configChgTrapValue1oid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'configChgTrapValue1')
    objectid = array([configChgTrapNeTypeoid+'.0',configChgTrapNEIDoid+'.0',configChgTrapTimeoid+'.0',configChgTrapValue1oid+'.0'],String)
    nodetypes = array(["Integer","Gauge","String","String"],String)
    softwarePackVersionoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'softwarePackVersion')
    print softwarePackVersionoid
    values = array(['0',enodebid,"2011-11-11 11:11:11",softwarePackVersionoid+'.1'+"|3|"+softname],String)
    scriptinterface.sendV2Trap(ftpconfigvlue[mgrName],162,"public",configChgTrapOID,objectid,nodetypes,values)
    scriptinterface.updateValue(softwarePackVersionoid,'.1',softname,"CONST")
    
    

