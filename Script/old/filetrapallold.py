from java.io import FileInputStream,FileOutputStream,IOException
from java.lang import Throwable,Exception,String,System
from jarray import zeros
from java.util.zip import GZIPOutputStream,ZipOutputStream,ZipFile,ZipEntry
from jarray import array
from java.lang import String


mgrPort = 162
community = "public"
trapOID = ".1.3.6.1.4.1.5105.80.1.6.2.7"
eventtrapOID=".1.3.6.1.4.1.5105.80.1.6.2.1"


enodebip=scriptinterface.getSnmpIPAddress()

f=open('C:\config.dcb','r')
str=f.read()
m=len(str)
for n in range(0,m):
 f.seek(n)
 t=f.read(7)
 if t=="neaip='":
  n=f.tell()

  nn=0
  while "'"!=f.read(1):
   nn=nn+1
  f.seek(n)
  neaip=f.read(nn)
 f.seek(n)
 t=f.read(7)
 if t=="ftpip='":
  n=f.tell()
  nn=0
  while "'"!=f.read(1):
   nn=nn+1
  f.seek(n)
  ftpip=f.read(nn)
 f.seek(n)
 t=f.read(13)
 if t=="ftpuserName='":
  n=f.tell()
  nn=0
  while "'"!=f.read(1):
   nn=nn+1
  f.seek(n)
  ftpuserName=f.read(nn)
 f.seek(n)
 t=f.read(13)
 if t=="ftppassword='":
  n=f.tell()
  nn=0
  while "'"!=f.read(1):
   nn=nn+1
  f.seek(n)
  ftppassword=f.read(nn)

mgrName = neaip




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


FileoidInstance=scriptinterface.getCurrentOIDWithInstance()
FileOID=scriptinterface.getCurrentOID()
FileInstance=FileoidInstance.replace(FileOID,'')

fileTransDestoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'fileTransDest')
enodebid = scriptinterface.getNodeValue(fileTransDestoid,FileInstance)
enodebidlen=len(enodebid)
for enodebidn in range(0,enodebidlen):
    if enodebid[enodebidn]=='/':
        enodebid1=enodebid[7:enodebidn]
enodebid=enodebid1
dcb=enodebid+'.dcb'


enodebidiod=scriptinterface.getSnmpOidForNodeName(enodebip,161,'nodeBSysFunctionId')
reenodebidiod=enodebidiod+'.0'+'</i><r>'

nodeBGlobalIdoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'nodeBGlobalId')
renodeBGlobalIdoid=nodeBGlobalIdoid+'.0'+'</i><r>'

nodeBSysOMAddroid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'nodeBSysOMAddr')
renodeBSysOMAddroid=nodeBSysOMAddroid+'.0'+'</i><r>'

            
e = 'true';
try:
    f = open(dcb,'r')
    f.close()
except :
    e = 'false'
    
if e == 'true':
    zipname=enodebid+'.gzip'
    gzip(dcb,zipname)






if e == 'false':

    enodebidlen=len(enodebid)
    for enodebidn in range(0,enodebidlen):

     if enodebid[enodebidn]=='/':
      enodebid1=enodebid[7:enodebidn]
    enodebid=enodebid1


    enodebidox=enodebid
    iienodebidox=int(enodebidox)
    t=hex(iienodebidox)
    

    
    numt=len(t)
    if numt<=6:
     t=t[2:numt]
     numt=len(t)
     numt=4-numt
     o=1
     while o<=numt:
      t='0'+t
      o=o+1
      enodebidox=t

    
    if numt>6:
     numt1=numt-4
     t1=t[numt1:numt]
     numt=numt-4
     t=t[2:numt]
     numt=len(t)
     numt=4-numt
     o=1
     while o<=numt:
      o=o+1
     t=t+t1
     enodebidox=t

     


    
    NodeBFunction=enodebidox
    nodeBSysFunctionId=enodebid
    nodeBGlobalId=enodebid
    nodeBSysOMAddr=enodebip

    antArrayVendorNameoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'antArrayVendorName')


    if antArrayVendorNameoid==None:

        f=open('C:\moban100.dcb','r+')
        moban100=f.read()

        moban100=moban100.replace(reenodebidiod,reenodebidiod+enodebid)
        moban100=moban100.replace(renodeBGlobalIdoid,renodeBGlobalIdoid+enodebid)
        moban100=moban100.replace(renodeBSysOMAddroid,renodeBSysOMAddroid+enodebip)
        moban100=moban100.replace('<sn>NodeBFunction=','<sn>NodeBFunction='+enodebidox)
        moban100=moban100.replace('<nedn>NodeBFunction=','<nedn>NodeBFunction='+enodebidox)

        
        f.close()

        f1=open(dcb,'w+')
        f1.write(moban100)
        f1.close()
        
    if antArrayVendorNameoid!=None:
    
        f=open('C:\moban200.dcb','r+')
        moban200=f.read()

        moban200=moban200.replace(reenodebidiod,reenodebidiod+enodebid)
        moban200=moban200.replace(renodeBGlobalIdoid,renodeBGlobalIdoid+enodebid)
        moban200=moban200.replace(renodeBSysOMAddroid,renodeBSysOMAddroid+enodebip)
        moban200=moban200.replace('<sn>NodeBFunction=','<sn>NodeBFunction='+enodebidox)
        moban200=moban200.replace('<nedn>NodeBFunction=','<nedn>NodeBFunction='+enodebidox)

        
        f.close()

        f1=open(dcb,'w+')
        f1.write(moban200)
        f1.close()



    zipname=enodebid+'.gzip'
    gzip(dcb,zipname)


lujing='eNodeB='+enodebid+'/FullCfg/'+zipname
scriptinterface.uploadFile(ftpip, 21, zipname, lujing,1, "ftp", ftpuserName, ftppassword);


fileTransTrapNEIDoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'fileTransTrapNEID')
fileTransTrapTaskIDoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'fileTransTrapTaskID')
fileTransTrapTypeoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'fileTransTrapType')
fileTransTrapNameoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'fileTransTrapName')
fileTransTrapFlagoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'fileTransTrapFlag')
fileTransTrapResultoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'fileTransTrapResult')
fileTransTrapBytesoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'fileTransTrapBytes')
fileTransTrapTimeoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'fileTransTrapTime')

objectid = array([fileTransTrapNEIDoid+FileInstance,fileTransTrapTaskIDoid+FileInstance,fileTransTrapTypeoid+FileInstance,fileTransTrapNameoid+FileInstance,fileTransTrapFlagoid+FileInstance,fileTransTrapResultoid+FileInstance,fileTransTrapBytesoid+FileInstance,fileTransTrapTimeoid+FileInstance],String)
nodetypes = array(["Gauge","Gauge","Integer","String","Integer","Integer","Gauge","String"],String)
fileTransTypeoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'fileTransType')

value = scriptinterface.getNodeValue(fileTransTypeoid,FileInstance)
value = int(value)
Filetaskid=FileInstance[1]



if (value == 15):
 values = array([enodebid,Filetaskid,"15",lujing,"1","0","1","2011-11-11 11:11:11"],String)
 scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)


 
 enodebidobjectId = enodebidiod
 instance=".0"
 enodebvalue = enodebid
 print enodebidobjectId
 scriptinterface.updateValue(enodebidobjectId,instance,enodebvalue,"CONST")

 
if (value == 13):

 values =  array([enodebid,Filetaskid,"13",lujing,"2","0","1","2011-11-11 11:11:11"],String)
 scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)

 values =  array([enodebid,"53","1","eventGeneralEventSource","eNB Static startup","2011-11-11 11:11:11"],String)

 
 eventGeneralEventNodeBSysFunctionIdoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'eventGeneralEventNodeBSysFunctionId')
 eventGeneralEventTypeoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'eventGeneralEventType')
 eventGeneralEventResultoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'eventGeneralEventResult')
 eventGeneralEventSourceoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'eventGeneralEventSource')
 eventGeneralEventAdditionInfooid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'eventGeneralEventAdditionInfo')
 eventGeneralEventOccurTimeoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'eventGeneralEventOccurTime')
 
 eventobjectid=array([eventGeneralEventNodeBSysFunctionIdoid+FileInstance,eventGeneralEventTypeoid+FileInstance,eventGeneralEventResultoid+FileInstance,eventGeneralEventSourceoid+FileInstance,eventGeneralEventAdditionInfooid+FileInstance,eventGeneralEventOccurTimeoid+FileInstance],String)
 eventnodetypes=array(["Integer","Integer","Integer","String","String","String"],String)
 scriptinterface.sendV2Trap(mgrName,mgrPort,community,eventtrapOID,eventobjectid,eventnodetypes,values)     
 
if (value == 16):
 
 #values = array([enodebid,Filetaskid,"16","eNodeB="+enodebid+"/Dynamic"+dynamicDatezipname,"1","0","1","2011-11-11 11:11:11"],String)
 values = array([enodebid,Filetaskid,"16",lujing,"1","0","1","2011-11-11 11:11:11"],String)
 scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)








