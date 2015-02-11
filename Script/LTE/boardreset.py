from java.io import FileInputStream,FileOutputStream,IOException
from java.lang import Throwable,Exception,String,System
from jarray import zeros
from java.util.zip import GZIPOutputStream,ZipOutputStream,ZipFile,ZipEntry
from jarray import array
from java.lang import String
from java.lang import Thread

f=open('C:\AdventNet_config_file\config.dcb','r')
str=f.read()
m=len(str)
for n in range(0,m):
 f.seek(n)
 t=f.read(7)
 if t=="neaip='":
  n=f.tell()
  print n
  nn=0
  while "'"!=f.read(1):
   nn=nn+1
  f.seek(n)
  neaip=f.read(nn)
f.close()

mgrName = neaip
mgrPort = 162
community = "public"
trapOID = ".1.3.6.1.4.1.5105.80.1.6.1.3"


enodebip=scriptinterface.getSnmpIPAddress()
print enodebip

CurrentOIDWithInstance=scriptinterface.getCurrentOIDWithInstance()
CurrentOID=scriptinterface.getCurrentOID()
boardResetTriggeroid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'boardResetTrigger')
print boardResetTriggeroid

Instance=CurrentOIDWithInstance.replace(boardResetTriggeroid,'')
print Instance

enodebidiod=scriptinterface.getSnmpOidForNodeName(enodebip,161,'nodeBSysFunctionId')
enodebid = scriptinterface.getNodeValue(enodebidiod,".0")


boardResetTrigger = scriptinterface.getNodeValue(CurrentOID,Instance)

boardProceduralStatusoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'boardProceduralStatus')
boardOperationalStateoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'boardOperationalState')
boardMasterSlaveStateoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'boardMasterSlaveState')
boardExistStatusoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'boardExistStatus')

if boardResetTrigger=='1':

    configChgTrapNeTypeoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'configChgTrapNeType')
    configChgTrapNEIDoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'configChgTrapNEID')
    configChgTrapTimeoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'configChgTrapTime')
    configChgTrapValue1oid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'configChgTrapValue1')
    
    objectid = array([configChgTrapNeTypeoid+Instance,configChgTrapNEIDoid+Instance,configChgTrapTimeoid+Instance,configChgTrapValue1oid+Instance],String)
    nodetypes = array(["Integer","Gauge","String","String"],String)

    values = array(['0',enodebid,"2011-11-11 11:11:11",boardProceduralStatusoid+Instance+"|3|0"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)
    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",boardProceduralStatusoid+Instance+"|3|1"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)
    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",boardProceduralStatusoid+Instance+"|3|2"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)
    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",boardProceduralStatusoid+Instance+"|3|3"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)
    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",boardProceduralStatusoid+Instance+"|3|4"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)
    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",boardOperationalStateoid+Instance+"|3|2"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)
    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",boardOperationalStateoid+Instance+"|3|0"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)
    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",boardOperationalStateoid+Instance+"|3|1"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)
    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",boardMasterSlaveStateoid+Instance+"|3|2"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)
    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",boardMasterSlaveStateoid+Instance+"|3|1"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)
    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",boardMasterSlaveStateoid+Instance+"|3|0"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)
    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",boardExistStatusoid+Instance+"|3|0"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)
    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",boardExistStatusoid+Instance+"|3|1"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)


    
