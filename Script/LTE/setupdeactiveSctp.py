from java.io import FileInputStream,FileOutputStream,IOException
from java.lang import Throwable,Exception,String,System
from jarray import zeros
from java.util.zip import GZIPOutputStream,ZipOutputStream,ZipFile,ZipEntry
from jarray import array
from java.lang import String
from java.lang import Thread


sctpActiveSwitchOIDWithInstance=scriptinterface.getCurrentOIDWithInstance()
sctpActiveSwitchOID=scriptinterface.getCurrentOID()

sctpActiveSwitchInstance=sctpActiveSwitchOIDWithInstance.replace(sctpActiveSwitchOID,'')

sctpActiveSwitch = scriptinterface.getNodeValue(sctpActiveSwitchOID,sctpActiveSwitchInstance)
enodebip=scriptinterface.getSnmpIPAddress()

sctpSetupStatusoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'sctpSetupStatus')

enodebip=scriptinterface.getSnmpIPAddress()
enodebidiod=scriptinterface.getSnmpOidForNodeName(enodebip,161,'nodeBSysFunctionId')
enodebid = scriptinterface.getNodeValue(enodebidiod,".0")


f=open('C:\AdventNet_config_file\config.dcb','r')
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
f.close()


mgrName = neaip
mgrPort = 162
community = "public"
trapOID = ".1.3.6.1.4.1.5105.80.1.6.1.3"

configChgTrapNeTypeoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'configChgTrapNeType')
configChgTrapNEIDoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'configChgTrapNEID')
configChgTrapTimeoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'configChgTrapTime')
configChgTrapValue1oid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'configChgTrapValue1')

objectid = array([configChgTrapNeTypeoid+sctpActiveSwitchInstance,configChgTrapNEIDoid+sctpActiveSwitchInstance,configChgTrapTimeoid+sctpActiveSwitchInstance,configChgTrapValue1oid+sctpActiveSwitchInstance],String)
nodetypes = array(["Integer","Gauge","String","String"],String)

if sctpActiveSwitch=='0':
    
    values = array(['0',enodebid,"2011-11-11 11:11:11",sctpSetupStatusoid+sctpActiveSwitchInstance+"|3|0"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)
    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",sctpSetupStatusoid+sctpActiveSwitchInstance+"|3|1"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)
    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",sctpSetupStatusoid+sctpActiveSwitchInstance+"|3|3"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)
    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",sctpSetupStatusoid+sctpActiveSwitchInstance+"|3|7"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)
    
    scriptinterface.updateNodeValue(enodebip,'161',sctpSetupStatusoid,sctpActiveSwitchInstance,'7')
    
if sctpActiveSwitch=='1':
    values = array(['0',enodebid,"2011-11-11 11:11:11",sctpSetupStatusoid+sctpActiveSwitchInstance+"|3|7"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)
    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",sctpSetupStatusoid+sctpActiveSwitchInstance+"|3|3"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)
    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",sctpSetupStatusoid+sctpActiveSwitchInstance+"|3|1"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)
    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",sctpSetupStatusoid+sctpActiveSwitchInstance+"|3|0"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)
    
    scriptinterface.updateNodeValue(enodebip,'161',sctpSetupStatusoid,sctpActiveSwitchInstance,'0')


