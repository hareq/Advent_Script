from java.io import FileInputStream,FileOutputStream,File
from java.lang import Exception,String,Thread
from jarray import zeros,array
from java.util.zip import GZIPOutputStream,ZipOutputStream,ZipEntry
import time

def getAgentPort():
        return int(scriptinterface.getSnmpPort())

def getAgentIp():
        return scriptinterface.getSnmpIPAddress()

def get_FileInstance():
        return scriptinterface.getCurrentInstance()
    
def foFileTypevalue():
        print "start foFileTypevalue"
        foFileTypeoid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'foFileType')
        return scriptinterface.getNodeValue(foFileTypeoid,get_FileInstance())

def from_fileTransDest_get_enodebid():
    print "Start from_fileTransDest_get_enodebid"
    fileTransDestoid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'fileTransDest')
    enodebid = scriptinterface.getNodeValue(fileTransDestoid,get_FileInstance())
    enodebidlen = len(enodebid)
    for enodebidn in range(0,enodebidlen):
        if enodebid[enodebidn] == '/':
            enodebid = enodebid[7:enodebidn]
            return enodebid

def get_enodeb_version():
    print "Start get_enodeb_version"
    f = open('C:\AdventNet_config_file\config.dcb','r')
    str = f.read()
    m = len(str)
    for n in range(0,m):
        f.seek(n)
        t = f.read(16)
        if t == "enodeb_version='":
            n = f.tell()
            nn = 0
            while "'" != f.read(1):
                nn = nn+1
            f.seek(n)
            enodeb_version = f.read(nn)
    return enodeb_version

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

def zip(src,dist):
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


def switch_denary_to_octal_for_configdate(enodebid):
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
    return enodebidox

def write_staticDate():
    print 'Start write_staticDate()'
    enodebidiod = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'nodeBSysFunctionId')
    reenodebidiod = enodebidiod+'.0'+'</i><r>'
    nodeBGlobalIdoid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'nodeBGlobalId')
    renodeBGlobalIdoid = nodeBGlobalIdoid+'.0'+'</i><r>'
    nodeBSysOMAddroid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'nodeBSysOMAddr')
    renodeBSysOMAddroid = nodeBSysOMAddroid+'.0'+'</i><r>'

    f = open("C:\AdventNet_config_file\staticDate"+get_enodeb_version()+".dcb",'r+')
    staticDate = f.read()
    staticDate = staticDate.replace(reenodebidiod,reenodebidiod+from_fileTransDest_get_enodebid())
    staticDate = staticDate.replace(renodeBGlobalIdoid,renodeBGlobalIdoid+from_fileTransDest_get_enodebid())
    staticDate = staticDate.replace(renodeBSysOMAddroid,renodeBSysOMAddroid+getAgentIp())
    staticDate = staticDate.replace('<sn>NodeBFunction=','<sn>NodeBFunction='+switch_denary_to_octal_for_configdate(from_fileTransDest_get_enodebid()))
    staticDate = staticDate.replace('<nedn>NodeBFunction=','<nedn>NodeBFunction='+switch_denary_to_octal_for_configdate(from_fileTransDest_get_enodebid()))
    f.close()
    
    f = open('staticDate'+from_fileTransDest_get_enodebid()+'.dcb','w+')
    f.write(staticDate)
    f.close()

def write_dynamicDate():
    print 'Start write_dynamicDate()'
    enodebidiod = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'nodeBSysFunctionId')
    reenodebidiod = enodebidiod+'.0'+'</i><r>'
    nodeBGlobalIdoid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'nodeBGlobalId')
    renodeBGlobalIdoid = nodeBGlobalIdoid+'.0'+'</i><r>'
    nodeBSysOMAddroid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'nodeBSysOMAddr')
    renodeBSysOMAddroid = nodeBSysOMAddroid+'.0'+'</i><r>'

    f = open("C:\AdventNet_config_file\dynamicDate"+get_enodeb_version()+".dcb",'r+')
    dynamicDate = f.read()
    dynamicDate = dynamicDate.replace('<sn>NodeBFunction=','<sn>NodeBFunction='+switch_denary_to_octal_for_configdate(from_fileTransDest_get_enodebid()))
    dynamicDate = dynamicDate.replace('<nedn>NodeBFunction=','<nedn>NodeBFunction='+switch_denary_to_octal_for_configdate(from_fileTransDest_get_enodebid()))
    f.close()
    
    f = open('dynamicDate'+from_fileTransDest_get_enodebid()+'.dcb','w+')
    f.write(dynamicDate)
    f.close()

def write_alarmFile(enodebid):
    print 'Start write_alarmFile()'
    enodebidox = enodebid
    iienodebidox = int(enodebidox)  
    sixteen = hex(iienodebidox)
    numt = len(sixteen) - 2
    sixteen = sixteen[2:len(sixteen)]
    while numt<8:
        sixteen= '0' + sixteen
        numt  = numt + 1
    f = open("C:\\AdventNet_config_file\\alarm.adb",'r+')
    alarmOldFile = f.read()
    alarmOldFile = alarmOldFile.replace('NodeBFunction=','NodeBFunction='+sixteen)    
    f.close()

    f1 = open(get_fileTransFileName_vlue(),'w+')
    f1.write(alarmOldFile)
    f1.close()

def from_NodeName_get_alarmEnodebId():
    index = get_fileTransFileName_vlue().find('_')
    return get_fileTransFileName_vlue()[7:index]


def get_getAgentIp():
    return scriptinterface.getSnmpIPAddress()
    
def nowtime():
    print "Start nowtime"
    return time.strftime('%Y-%m-%d %X',time.localtime(time.time()))

def from_NodeName_get_enodebid():
    nodeBSysFunctionIdoid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'nodeBSysFunctionId')
    enodebid = scriptinterface.getNodeValue(nodeBSysFunctionIdoid,'.0')
    return enodebid

def softdownload(softpathandname,fileTransFileName):
    scriptinterface.downloadFile(ftp_config()[1], 21, softpathandname, fileTransFileName,1, "ftp", ftp_config()[2], ftp_config()[3]);
    
def getSoftwareVersion(localsoftpathandname):
    f = open(localsoftpathandname,'r')
    str = f.read(50)
    softname = str[16:46]
    f.close()
    print 'softname =',softname
    return softname

def fileTransTrap_objectid():
    print "start File_Trap_objectid"
    fileTransTrapNEIDoid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'fileTransTrapNEID')
    fileTransTrapTaskIDoid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'fileTransTrapTaskID')
    fileTransTrapTypeoid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'fileTransTrapType')
    fileTransTrapNameoid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'fileTransTrapName')
    fileTransTrapFlagoid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'fileTransTrapFlag')
    fileTransTrapResultoid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'fileTransTrapResult')
    fileTransTrapBytesoid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'fileTransTrapBytes')
    fileTransTrapTimeoid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'fileTransTrapTime')
    objectid = array([fileTransTrapNEIDoid+get_FileInstance(),fileTransTrapTaskIDoid+get_FileInstance(),fileTransTrapTypeoid+get_FileInstance(),fileTransTrapNameoid+get_FileInstance(),fileTransTrapFlagoid+get_FileInstance(),fileTransTrapResultoid+get_FileInstance(),fileTransTrapBytesoid+get_FileInstance(),fileTransTrapTimeoid+get_FileInstance()],String)
    return objectid

def fileTransTrap_nodetypes():
    nodetypes = array(["Gauge","Gauge","Integer","String","Integer","Integer","Gauge","String"],String)
    return nodetypes

def get_fileTransType_vlue():
    fileTransTypeoid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'fileTransType')
    fileTransType = scriptinterface.getNodeValue(fileTransTypeoid,get_FileInstance())    
    return fileTransType

def get_fileTransDest_vlue():
    fileTransDestoid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'fileTransDest')
    fileTransDest = scriptinterface.getNodeValue(fileTransDestoid,get_FileInstance())
    return fileTransDest

def get_fileTransFileName_vlue():
    fileTransFileNameoid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'fileTransFileName')
    fileTransFileName = scriptinterface.getNodeValue(fileTransFileNameoid,get_FileInstance())
    return fileTransFileName

def delete_file(filename):
        print "Start delete_file"
        if File(filename).exists():
            File(filename).delete()

def get_fileTransFlag_vlue():
    fileTransFlagoid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'fileTransFlag')
    fileTransFlag = scriptinterface.getNodeValue(fileTransFlagoid,get_FileInstance())
    return fileTransFlag
        
def fileTransTrap_nodetypes_vlues(enodebid,result):
        print "start File_Trap_vlue"
        values = array([enodebid,get_FileInstance()[1:],get_fileTransType_vlue(),get_fileTransDest_vlue()+"/"+get_fileTransFileName_vlue(),get_fileTransFlag_vlue(),result,"1",nowtime()],String)
        return values
    
def eventGeneralEvent_objectid():
        eventGeneralEventNodeBSysFunctionIdoid=scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'eventGeneralEventNodeBSysFunctionId')
        eventGeneralEventTypeoid=scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'eventGeneralEventType')
        eventGeneralEventResultoid=scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'eventGeneralEventResult')
        eventGeneralEventSourceoid=scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'eventGeneralEventSource')
        eventGeneralEventAdditionInfooid=scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'eventGeneralEventAdditionInfo')
        eventGeneralEventOccurTimeoid=scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'eventGeneralEventOccurTime')
        eventobjectid = array([eventGeneralEventNodeBSysFunctionIdoid+".0",eventGeneralEventTypeoid+".0",eventGeneralEventResultoid+".0",eventGeneralEventSourceoid+".0",eventGeneralEventAdditionInfooid+".0",eventGeneralEventOccurTimeoid+".0"],String)
        return eventobjectid

def configChgTrap_objectid():
        configChgTrapNeTypeoid=scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'configChgTrapNeType')
        configChgTrapNEIDoid=scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'configChgTrapNEID')
        configChgTrapTimeoid=scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'configChgTrapTime')
        configChgTrapValue1oid=scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'configChgTrapValue1')
        objectid = array([configChgTrapNeTypeoid+'.0',configChgTrapNEIDoid+'.0',configChgTrapTimeoid+'.0',configChgTrapValue1oid+'.0'],String)
        return objectid

    
def eventGeneralEvent_types():
        return array(["Integer","Integer","Integer","String","String","String"],String)
def configChgTrap_types():
        return array(["Integer","Gauge","String","String"],String)   
def enodebidiod():
    enodebidoid=scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'nodeBSysFunctionId')


def ftp_config():
    f = open('C:\AdventNet_config_file\config.dcb','r')
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
    f.close()

    
def main():    
    print 'Robotization Start'
    file_trapOID = ".1.3.6.1.4.1.5105.80.1.6.2.7"
    event_trapOID = ".1.3.6.1.4.1.5105.80.1.6.2.1"
    configChgTrapOID = ".1.3.6.1.4.1.5105.80.1.6.1.3"
    
    if (get_fileTransType_vlue() == "15"):
        print 'Start staticDate_fileup'
        e = 'true';
        try:
            f = open('staticDate'+from_fileTransDest_get_enodebid()+'.dcb','r')
            f.close()
        except :
            e = 'false'
            
        if e == 'true':
            gzip('staticDate'+from_fileTransDest_get_enodebid()+'.dcb',get_fileTransFileName_vlue())  

        if e == 'false':
            print 'Have no file,goto write_staticDate()'
            write_staticDate()            
            gzip('staticDate'+from_fileTransDest_get_enodebid()+'.dcb',get_fileTransFileName_vlue())  
        scriptinterface.uploadFile(ftp_config()[1], 21, get_fileTransFileName_vlue(),get_fileTransDest_vlue()+"/"+get_fileTransFileName_vlue(),1, "ftp", ftp_config()[2], ftp_config()[3]);
        scriptinterface.sendV2Trap(ftp_config()[0],162,"public",file_trapOID,fileTransTrap_objectid(),fileTransTrap_nodetypes(),fileTransTrap_nodetypes_vlues(from_fileTransDest_get_enodebid(),"0"))
        delete_file(get_fileTransFileName_vlue())
        scriptinterface.updateValue(enodebidiod(),get_FileInstance(),from_fileTransDest_get_enodebid(),"CONST")

     
    if (get_fileTransType_vlue() == "13"):
        print 'Start filedown'
        scriptinterface.sendV2Trap(ftp_config()[0],162,"public",file_trapOID,fileTransTrap_objectid(),fileTransTrap_nodetypes(),fileTransTrap_nodetypes_vlues(from_fileTransDest_get_enodebid(),"0"))
        values =  array([from_fileTransDest_get_enodebid(),"53","1","eventGeneralEventSource","eventGeneralEventAdditionInfo",nowtime()],String)
        scriptinterface.sendV2Trap(ftp_config()[0],162,"public",event_trapOID,eventGeneralEvent_objectid(),eventGeneralEvent_types(),values)

    if (get_fileTransType_vlue() == "16"):
        print 'Start dynamicDate_fileup'
        e = 'true';
        try:
            f = open('dynamicDate'+from_fileTransDest_get_enodebid()+'.dcb','r')
            f.close()
        except :
            e = 'false'
            
        if e == 'true':
            gzip('dynamicDate'+from_fileTransDest_get_enodebid()+'.dcb',get_fileTransFileName_vlue())  

        if e == 'false':
            print 'Have no file,goto write_dynamicDate()'
            write_dynamicDate()           
            gzip('dynamicDate'+from_fileTransDest_get_enodebid()+'.dcb',get_fileTransFileName_vlue())  
        scriptinterface.uploadFile(ftp_config()[1], 21, get_fileTransFileName_vlue(),get_fileTransDest_vlue()+"/"+get_fileTransFileName_vlue(),1, "ftp", ftp_config()[2], ftp_config()[3]);
        scriptinterface.sendV2Trap(ftp_config()[0],162,"public",file_trapOID,fileTransTrap_objectid(),fileTransTrap_nodetypes(),fileTransTrap_nodetypes_vlues(from_fileTransDest_get_enodebid(),"0"))
        delete_file(get_fileTransFileName_vlue())
        scriptinterface.updateValue(enodebidiod(),get_FileInstance(),from_fileTransDest_get_enodebid(),"CONST")        


    if (get_fileTransType_vlue() == "6"):
        print 'Start softfiledown'
        Thread.currentThread().sleep(5*1000)
        scriptinterface.sendV2Trap(ftp_config()[0],162,"public",file_trapOID,fileTransTrap_objectid(),fileTransTrap_nodetypes(),fileTransTrap_nodetypes_vlues(from_NodeName_get_enodebid(),"0"))           
        softdownload(get_fileTransDest_vlue()+'/'+get_fileTransFileName_vlue(),get_fileTransFileName_vlue())
        softwarePackVersionoid=scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'softwarePackVersion')
        values = array(['0',from_NodeName_get_enodebid(),nowtime(),softwarePackVersionoid+'.1'+'|3|'+getSoftwareVersion(get_fileTransFileName_vlue())],String)
        scriptinterface.sendV2Trap(ftp_config()[0],162,"public",configChgTrapOID,configChgTrap_objectid(),configChgTrap_types(),values)
        scriptinterface.updateValue(softwarePackVersionoid,'.1',getSoftwareVersion(get_fileTransFileName_vlue()),"CONST")
    
    if (get_fileTransType_vlue() == "12"):
        print 'Start alarm_fileup'
        if File(get_fileTransFileName_vlue()).exists():        
            File(get_fileTransFileName_vlue()).delete()
        write_alarmFile(from_NodeName_get_alarmEnodebId())
        scriptinterface.uploadFile(ftp_config()[1], 21, get_fileTransFileName_vlue(),get_fileTransDest_vlue()+"/"+get_fileTransFileName_vlue(),1, "ftp", ftp_config()[2], ftp_config()[3]);
        scriptinterface.sendV2Trap(ftp_config()[0],162,"public",file_trapOID,fileTransTrap_objectid(),fileTransTrap_nodetypes(),fileTransTrap_nodetypes_vlues(from_NodeName_get_alarmEnodebId(),"0"))
        File(get_fileTransFileName_vlue()).delete()

main()
