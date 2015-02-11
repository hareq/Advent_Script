from java.io import FileInputStream,FileOutputStream,File
from java.lang import Exception,String,Thread
from jarray import zeros,array
from java.util.zip import GZIPOutputStream,ZipOutputStream,ZipEntry
import time

def ftp_config():
        f = open('C:\AdventNet_config_file_cn\config.dcb','r')
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

def nowtime():
    return time.strftime('%Y-%m-%d %X',time.localtime(time.time()))


def zipfile(src,dist):
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

def write_pcrffile():
        f = open("C:\AdventNet_config_file_cn\pcrf_staticDate.xml",'r+')
        pcrfdate = f.read()
        pcrfdate = pcrfdate.replace('DraManagedElementIdvlue',from_filetrap_get_DraManagedElementId())
        pcrfdate = pcrfdate.replace('SctpAssocLocalAddrvlue',getAgentIp())
        pcrfdate = pcrfdate.replace('IpAddressListvlue',getAgentIp())
        f.close()
        f1 = open("PCRF-NRM"+from_filetrap_get_DraManagedElementId()+".xml",'w+')
        f1.write(pcrfdate)
        f1.close()

def write_draalarmfile():
        f = open("C:\AdventNet_config_file_cn\pcrf_alarm.adb",'r+')
        dradate = f.read()
        dradate = dradate.replace('pcrfid',from_alarmfiletrap_get_DraManagedElementId())       
        f.close()
        f1 = open(get_fileTransferFileName_vlue(),'w+')
        f1.write(dradate)
        f1.close()

def from_filetrap_get_DraManagedElementId():
        fileTransferDestination = get_fileTransferDestination_vlue()
        if (fileTransferDestination.find('pcrf=') != 0):
           fileTransferDestinationlen = len(fileTransferDestination)
           for n in range(0,fileTransferDestinationlen):
               if fileTransferDestination[n] == '/':
                    pcrfid = fileTransferDestination[5:n]
                    pcrfidoid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'ManagedElementId')
                    scriptinterface.updateValue(pcrfidoid,'.0',pcrfid,"CONST")

        if (get_fileTransferFileName_vlue().find('pcrf=') != 0):
            fileTransferDestinationlen = len(get_fileTransferFileName_vlue())
            for n in range(0,fileTransferDestinationlen):
                if get_fileTransferFileName_vlue()[n] == '#':
                    pcrfid = get_fileTransferFileName_vlue()[5:n]
        else:
            pcrfidoid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'ManagedElementId')
            pcrfid = scriptinterface.getNodeValue(pcrfidoid,get_FileInstance())

        return pcrfid



def from_alarmfiletrap_get_DraManagedElementId():
        fileTransferDestination = get_fileTransferFileName_vlue()
        fileTransferDestinationlen = len(fileTransferDestination)
        for n in range(0,fileTransferDestinationlen):
                if fileTransferDestination[n] == '_':
                    draid = fileTransferDestination[5:n]
                    break
        return draid

def getAgentPort():
        return int(scriptinterface.getSnmpPort())

def getAgentIp():
        AgentIp = scriptinterface.getSnmpIPAddress()
        return AgentIp

def get_FileInstance():
        FileoidInstance = scriptinterface.getCurrentInstance()
        return FileoidInstance


def fileTransTrap_objectid():
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


def fileTransTrap_vlues(result):
        values = array([from_filetrap_get_DraManagedElementId(),get_FileInstance()[1:],get_fileTransferType_vlue(),get_fileTransferDestination_vlue()+"/"+get_fileTransferFileName_vlue(),get_fileTransferFlag_vlue(),result,"1",nowtime()],String)
        return values

def armfileTransTrap_vlues(result):
    values = array([from_alarmfiletrap_get_DraManagedElementId(),get_FileInstance()[1:],get_fileTransferType_vlue(),get_fileTransferDestination_vlue()+"/"+get_fileTransferFileName_vlue(),get_fileTransferFlag_vlue(),result,"1",nowtime()],String)
    return values

def get_fileTransferType_vlue():
        foFileTypeoid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'fileTransferType')
        foFileTypevalue = scriptinterface.getNodeValue(foFileTypeoid,get_FileInstance())
        return foFileTypevalue

def get_fileTransferFileName_vlue():
        foFileNameoid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'fileTransferFileName')
        foFileNamevalue = scriptinterface.getNodeValue(foFileNameoid,get_FileInstance())
        return foFileNamevalue

def get_fileTransferDestination_vlue():
        foFilePathoid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'fileTransferDestination')
        foFilePathvalue = scriptinterface.getNodeValue(foFilePathoid,get_FileInstance())
        return foFilePathvalue

def get_fileTransferFlag_vlue():
        fileTransFlagoid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'fileTransferFlag')
        fileTransFlag = scriptinterface.getNodeValue(fileTransFlagoid,get_FileInstance())
        return fileTransFlag
                
def update_pcrfid_into_adventnet():
        enodebidiod = scriptinterface.getSnmpOidForNodeName(getAgentIp(),161,'nodeBSysFunctionId')
        enodebidobjectId = enodebidiod
        enodebvalue = enodebid
        scriptinterface.updateValue(enodebidobjectId,instance,enodebvalue,"CONST")

def delete_file(filename):
        if File(filename).exists():        
                File(filename).delete()

def isHeartBeat(currentOid):
        hbOid = scriptinterface.getSnmpOidForNodeName("PcrfSystemOmcrActive")
        if(hbOid is not None):
                if(currentOid.find(hbOid, 0, len(currentOid)) == -1):
                        return 0
                else:
                        return 1
        return 0

def isconfig(currentOid):
        hbOid='.1.3.6.1.4.1.777.2.3'
        if(hbOid is not None):
                if(currentOid.find(hbOid, 0, len(currentOid)) == -1):
                        return 0
                else:
                        return 1
        return 0



def main():
        mgrName = 0
        ftpip = 1
        ftpuserName = 2
        ftppassword = 3
        trapOID = ".1.3.6.1.4.1.777.2.2.3.1.1"
        enodebip = getAgentIp()
        ftpconfigvlue = ftp_config()
        AgentPort = getAgentPort()
        FileoidInstance = scriptinterface.getCurrentInstance()
        currentOid = scriptinterface.getCurrentOID()
        
        if (isHeartBeat(currentOid) == 1 ):
            return
            
        elif (currentOid == scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'fileTransferType')):
                if (get_fileTransferType_vlue() == "1" and get_fileTransferFlag_vlue() =="1"):
                        e = 'true';
                        try:
                                f = open("PCRF-NRM"+from_filetrap_get_DraManagedElementId()+".xml",'r')
                                f.close()
                        except :
                                e = 'false'
                                
                        if e == 'true':
                                zipfile("PCRF-NRM"+from_filetrap_get_DraManagedElementId()+".xml",get_fileTransferFileName_vlue())

                        if e == 'false':
                                write_pcrffile()
                                zipfile('PCRF-NRM'+from_filetrap_get_DraManagedElementId()+'.xml',get_fileTransferFileName_vlue())
                        scriptinterface.uploadFile(ftpconfigvlue[ftpip], 21, get_fileTransferFileName_vlue(), get_fileTransferDestination_vlue()+"/"+get_fileTransferFileName_vlue(),1, "ftp", ftpconfigvlue[ftpuserName], ftpconfigvlue[ftppassword]);
                        delete_file(get_fileTransferFileName_vlue())
                        scriptinterface.sendV2Trap(ftpconfigvlue[mgrName],162,"public",trapOID,fileTransTrap_objectid(),fileTransTrap_nodetypes(),fileTransTrap_vlues("0"))
                if (get_fileTransferType_vlue() == "1" and get_fileTransferFlag_vlue() =="2"):
                        scriptinterface.downloadFile(ftpconfigvlue[ftpip], 21, get_fileTransferDestination_vlue()+"/"+get_fileTransferFileName_vlue(), get_fileTransferFileName_vlue(),2, "ftp", ftpconfigvlue[ftpuserName], ftpconfigvlue[ftppassword]);
                        delete_file(get_fileTransferFileName_vlue())
                        scriptinterface.sendV2Trap(ftpconfigvlue[mgrName],162,"public",trapOID,fileTransTrap_objectid(),fileTransTrap_nodetypes(),fileTransTrap_vlues("0"))
                if (get_fileTransferType_vlue() == "12" and get_fileTransferFlag_vlue() =="1"):
                        write_draalarmfile()
                        scriptinterface.uploadFile(ftpconfigvlue[ftpip], 21, get_fileTransferFileName_vlue(), get_fileTransferDestination_vlue()+"/"+get_fileTransferFileName_vlue(),1, "ftp", ftpconfigvlue[ftpuserName], ftpconfigvlue[ftppassword]);
                        delete_file(get_fileTransferFileName_vlue())
                        scriptinterface.sendV2Trap(ftpconfigvlue[mgrName],162,"public",trapOID,fileTransTrap_objectid(),fileTransTrap_nodetypes(),armfileTransTrap_vlues("0"))

        elif (isconfig(currentOid)==1):
                pcrfidoid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'ManagedElementId')
                pcrfid = scriptinterface.getNodeValue(pcrfidoid,get_FileInstance())              
                currentOid = ''
##                while ((File('test.dcb').exists()) == 1):
##                Thread.currentThread().sleep(1)
##                f = open('test.dcb','w+')
##                f.close()
##                f = open('staticDate228.dcb','r+')
##                staticDate = f.read()                    
##                f.close()
##                start = staticDate.find(scriptinterface.getCurrentOIDWithInstance()+"</i><r>")           
##                if not(start == -1):
##                     end = staticDate.find('</r></dcv>',start)+10
##                     y = staticDate[start:end]
##                     h = scriptinterface.getCurrentOIDWithInstance()+"</i><r>"+scriptinterface.getCurrentValue()+"</r></dcv>"
##                     staticDate = staticDate.replace(y,h)                    
##                     f = open('staticDate228.dcb','w+')
##                     f.write(staticDate)
##                     f.close()
##                File('test.dcb').delete()       
main()
