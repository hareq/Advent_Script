from java.io import FileInputStream,FileOutputStream,File
from java.lang import Exception,String,Thread
from jarray import zeros,array
from java.util.zip import GZIPOutputStream,ZipOutputStream

def ftp_config():
        print "Strat ftp_config"
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

def gzip(src,dist):
    print "Strat gzip"
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

def write_scafile():
        print 'Start write_scafile()'
        sysDeviceIdoid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'sysDeviceId')
        sysDeviceIdoid = sysDeviceIdoid[1:]+'.0'+'</i>\n<t>I</t>\n<r>'
        print "sysDeviceIdoid =",sysDeviceIdoid
        f = open("C:\AdventNet_config_file\sca_staticDate.dcb",'r+')
        scadate = f.read()
        scadate = scadate.replace(sysDeviceIdoid,sysDeviceIdoid+from_filetrap_get_scaid())
        f.close()
        f1 = open("sca"+from_filetrap_get_scaid()+".dcb",'w+')
        f1.write(scadate)
        f1.close()

def from_filetrap_get_scaid():
        print "start from_filetrap_get_scaid"
        foFilePathoid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'foFilePath')
        foFilePath = scriptinterface.getNodeValue(foFilePathoid,get_FileInstance())
        foFilePathlen = len(foFilePath)
        for n in range(0,foFilePathlen):
                if foFilePath[n] == '/':
                    scaid = foFilePath[11:n]
        return scaid

def getAgentPort():
        return int(scriptinterface.getSnmpPort())

def getAgentIp():
        AgentIp = scriptinterface.getSnmpIPAddress()
        return AgentIp

def get_FileInstance():
        FileoidInstance = scriptinterface.getCurrentInstance()
        return FileoidInstance


def File_Trap_objectid():
        print "start File_Trap_objectid"
        foCorrelationNooid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'foCorrelationNo')
        foFileTypeoid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'foFileType')
        foFilePathoid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'foFilePath')
        foFileNameoid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'foFileName')
        foResultoid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'foResult')
        objectid = array([foCorrelationNooid+get_FileInstance(),foFileTypeoid+get_FileInstance(),foFilePathoid+get_FileInstance(),foFileNameoid+get_FileInstance(),foResultoid+get_FileInstance()],String)
        return objectid

def File_Trap_vlue(result):
        print "start File_Trap_vlue"
        foCorrelationNooid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'foCorrelationNo')
        foFileTypeoid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'foFileType')
        foFilePathoid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'foFilePath')
        foFileNameoid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'foFileName')
        foCorrelationNovlue = scriptinterface.getNodeValue(foCorrelationNooid,get_FileInstance())
        foFileTypevalue = scriptinterface.getNodeValue(foFileTypeoid,get_FileInstance())
        foFilePathvalue = scriptinterface.getNodeValue(foFilePathoid,get_FileInstance())
        foFileNamevalue = scriptinterface.getNodeValue(foFileNameoid,get_FileInstance())        
        values = array([foCorrelationNovlue,foFileTypevalue,foFilePathvalue,foFileNamevalue,result],String)
        return values


def foFileTypevalue():
        print "start foFileTypevalue"
        foFileTypeoid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'foFileType')
        foFileTypevalue = scriptinterface.getNodeValue(foFileTypeoid,get_FileInstance())
        return foFileTypevalue

def foFileNamevalue():
        print "start foFileNamevalue"
        foFileNameoid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'foFileName')
        foFileNamevalue = scriptinterface.getNodeValue(foFileNameoid,get_FileInstance())
        return foFileNamevalue

def foFilePathvalue():
        print "start foFilePathvalue"
        foFilePathoid = scriptinterface.getSnmpOidForNodeName(getAgentIp(),getAgentPort(),'foFilePath')
        foFilePathvalue = scriptinterface.getNodeValue(foFilePathoid,get_FileInstance())
        return foFilePathvalue
                
def update_scaid_into_adventnet():
        print "start update_scaid_into_adventnet"
        enodebidiod = scriptinterface.getSnmpOidForNodeName(getAgentIp(),161,'nodeBSysFunctionId')
        enodebidobjectId = enodebidiod
        enodebvalue = enodebid
        scriptinterface.updateValue(enodebidobjectId,instance,enodebvalue,"CONST")

def delete_file(filename):
        print "Start delete_file"
        if File(filename).exists():        
                File(filename).delete()

def main():
        print 'Robotization Start'
        mgrName = 0
        ftpip = 1
        ftpuserName = 2
        ftppassword = 3
        trapOID = ".1.2.156.112566.1.1.1.13"
        enodebip = getAgentIp()
        ftpconfigvlue = ftp_config()
        AgentPort = getAgentPort()
        nodetypes = array(["Integer","Gauge","String","String","Integer",],String)
        if (foFileTypevalue() == "1"):
                print 'Start sca_file_trap'
                e = 'true';
                try:
                        f = open("sca"+from_filetrap_get_scaid()+".dcb",'r')
                        f.close()
                except :
                        e = 'false'
                if e == 'true':
                        gzip("sca"+from_filetrap_get_scaid()+".dcb",foFileNamevalue())  

                if e == 'false':
                        print 'Have no file,goto write_scafile()'
                        write_scafile()
                        gzip('sca'+from_filetrap_get_scaid()+'.dcb',foFileNamevalue())
                scriptinterface.uploadFile(ftpconfigvlue[ftpip], 21, foFileNamevalue(), foFilePathvalue()+"/"+foFileNamevalue(),1, "ftp", ftpconfigvlue[ftpuserName], ftpconfigvlue[ftppassword]);
                print foFileNamevalue()
                delete_file(foFileNamevalue())
                scriptinterface.sendV2Trap(ftpconfigvlue[mgrName],162,"public",trapOID,File_Trap_objectid(),nodetypes,File_Trap_vlue("0"))
        
main()
