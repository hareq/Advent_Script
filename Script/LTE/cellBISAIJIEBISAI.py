from java.io import FileInputStream,FileOutputStream,IOException
from java.lang import Throwable,Exception,String,System
from jarray import zeros
from java.util.zip import GZIPOutputStream,ZipOutputStream,ZipFile,ZipEntry
from jarray import array
from java.lang import String
from java.lang import Thread


lcCellBlockSwitchOIDWithInstance=scriptinterface.getCurrentOIDWithInstance()
lcCellBlockSwitchOID=scriptinterface.getCurrentOID()

lcCellBlockSwitchInstance=lcCellBlockSwitchOIDWithInstance.replace(lcCellBlockSwitchOID,'')

lcCellBlockSwitch = scriptinterface.getNodeValue(lcCellBlockSwitchOID,lcCellBlockSwitchInstance)
enodebip=scriptinterface.getSnmpIPAddress()

lcCellBlockStatusoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'lcCellBlockStatus')
lcCellOperationalStateoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'lcCellOperationalState')

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

configChgTrapNeTypeoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'configChgTrapNeType')
configChgTrapNEIDoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'configChgTrapNEID')
configChgTrapTimeoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'configChgTrapTime')
configChgTrapValue1oid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'configChgTrapValue1')

objectid = array([configChgTrapNeTypeoid+lcCellBlockSwitchInstance,configChgTrapNEIDoid+lcCellBlockSwitchInstance,configChgTrapTimeoid+lcCellBlockSwitchInstance,configChgTrapValue1oid+lcCellBlockSwitchInstance],String)
nodetypes = array(["Integer","Gauge","String","String"],String)



if lcCellBlockSwitch=='1':
    


    values = array(['0',enodebid,"2011-11-11 11:11:11",lcCellBlockStatusoid+lcCellBlockSwitchInstance+"|3|2"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)
    scriptinterface.updateNodeValue(enodebip,'161',lcCellBlockStatusoid,lcCellBlockSwitchInstance,'2')

    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",lcCellBlockStatusoid+lcCellBlockSwitchInstance+"|3|0"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)
    scriptinterface.updateNodeValue(enodebip,'161',lcCellBlockStatusoid,lcCellBlockSwitchInstance,'0')    

if lcCellBlockSwitch=='2':
    


    values = array(['0',enodebid,"2011-11-11 11:11:11",lcCellBlockStatusoid+lcCellBlockSwitchInstance+"|3|0"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)

    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",lcCellBlockStatusoid+lcCellBlockSwitchInstance+"|3|1"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)

    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",lcCellBlockStatusoid+lcCellBlockSwitchInstance+"|3|2"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)
    scriptinterface.updateNodeValue(enodebip,'161',lcCellBlockStatusoid,lcCellBlockSwitchInstance,'2')        

