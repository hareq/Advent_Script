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

trapOID = ".1.3.6.1.4.1.5105.80.1.6.1.3"
mgrName = neaip
mgrPort = 162
community = "public"



lcCellActiveTriggerOIDWithInstance=scriptinterface.getCurrentOIDWithInstance()
lcCellActiveTriggerOID=scriptinterface.getCurrentOID()

lcCellActiveTriggerInstance=lcCellActiveTriggerOIDWithInstance.replace(lcCellActiveTriggerOID,'')

lcCellActiveTrigger = scriptinterface.getNodeValue(lcCellActiveTriggerOID,lcCellActiveTriggerInstance)
enodebip=scriptinterface.getSnmpIPAddress()

lcCellAvailbilityStatusoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'lcCellAvailbilityStatus')
lcCellOperationalStateoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'lcCellOperationalState')

enodebip=scriptinterface.getSnmpIPAddress()
enodebidiod=scriptinterface.getSnmpOidForNodeName(enodebip,161,'nodeBSysFunctionId')
enodebid = scriptinterface.getNodeValue(enodebidiod,".0")







configChgTrapNeTypeoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'configChgTrapNeType')
configChgTrapNEIDoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'configChgTrapNEID')
configChgTrapTimeoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'configChgTrapTime')
configChgTrapValue1oid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'configChgTrapValue1')

objectid = array([configChgTrapNeTypeoid+lcCellActiveTriggerInstance,configChgTrapNEIDoid+lcCellActiveTriggerInstance,configChgTrapTimeoid+lcCellActiveTriggerInstance,configChgTrapValue1oid+lcCellActiveTriggerInstance],String)
nodetypes = array(["Integer","Gauge","String","String"],String)


if lcCellActiveTrigger=='0':
    


    values = array(['0',enodebid,"2011-11-11 11:11:11",lcCellAvailbilityStatusoid+lcCellActiveTriggerInstance+"|3|7"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)

    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",lcCellAvailbilityStatusoid+lcCellActiveTriggerInstance+"|3|6"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)

    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",lcCellAvailbilityStatusoid+lcCellActiveTriggerInstance+"|3|5"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)
    
    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",lcCellAvailbilityStatusoid+lcCellActiveTriggerInstance+"|3|4"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)

    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",lcCellAvailbilityStatusoid+lcCellActiveTriggerInstance+"|3|3"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)

    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",lcCellAvailbilityStatusoid+lcCellActiveTriggerInstance+"|3|2"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)

    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",lcCellAvailbilityStatusoid+lcCellActiveTriggerInstance+"|3|1"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)
    
    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",lcCellAvailbilityStatusoid+lcCellActiveTriggerInstance+"|3|0"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)
    scriptinterface.updateNodeValue(enodebip,'161',lcCellAvailbilityStatusoid,lcCellActiveTriggerInstance,'0')
    
    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",lcCellOperationalStateoid+lcCellActiveTriggerInstance+"|3|2"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)
    
    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",lcCellOperationalStateoid+lcCellActiveTriggerInstance+"|3|1"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)
    
    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",lcCellOperationalStateoid+lcCellActiveTriggerInstance+"|3|0"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)
    scriptinterface.updateNodeValue(enodebip,'161',lcCellOperationalStateoid,lcCellActiveTriggerInstance,'0')
   


if lcCellActiveTrigger=='1':
    


    values = array(['0',enodebid,"2011-11-11 11:11:11",lcCellAvailbilityStatusoid+lcCellActiveTriggerInstance+"|3|0"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)

    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",lcCellAvailbilityStatusoid+lcCellActiveTriggerInstance+"|3|1"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)

    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",lcCellAvailbilityStatusoid+lcCellActiveTriggerInstance+"|3|3"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)
    
    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",lcCellAvailbilityStatusoid+lcCellActiveTriggerInstance+"|3|4"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)

    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",lcCellAvailbilityStatusoid+lcCellActiveTriggerInstance+"|3|5"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)

    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",lcCellAvailbilityStatusoid+lcCellActiveTriggerInstance+"|3|6"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)

    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",lcCellAvailbilityStatusoid+lcCellActiveTriggerInstance+"|3|7"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)
    
    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",lcCellAvailbilityStatusoid+lcCellActiveTriggerInstance+"|3|2"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)
    scriptinterface.updateNodeValue(enodebip,'161',lcCellAvailbilityStatusoid,lcCellActiveTriggerInstance,'2')    
    
    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",lcCellOperationalStateoid+lcCellActiveTriggerInstance+"|3|0"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)
    
    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",lcCellOperationalStateoid+lcCellActiveTriggerInstance+"|3|2"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)
    
    Thread.currentThread().sleep(1*1000)
    values = array(['0',enodebid,"2011-11-11 11:11:11",lcCellOperationalStateoid+lcCellActiveTriggerInstance+"|3|1"],String)
    scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)
    scriptinterface.updateNodeValue(enodebip,'161',lcCellOperationalStateoid,lcCellActiveTriggerInstance,'2')







    
