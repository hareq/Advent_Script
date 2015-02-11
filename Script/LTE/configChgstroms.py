from java.io import FileInputStream,FileOutputStream,IOException
from java.lang import Throwable,Exception,String,System
from jarray import zeros
from java.util.zip import GZIPOutputStream,ZipOutputStream,ZipFile,ZipEntry
from jarray import array
from java.lang import String
from java.lang import Thread
from time import time
import time

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

enodebip=scriptinterface.getSnmpIPAddress()
print enodebip
configChgTrapOID = ".1.3.6.1.4.1.5105.80.1.6.1.3"
nodeBSysFunctionIdoid = scriptinterface.getSnmpOidForNodeName(enodebip,161,'nodeBSysFunctionId')
enodebid = scriptinterface.getNodeValue(nodeBSysFunctionIdoid,'.0')
nodeBDestCfgFileVersionoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'nodeBDestCfgFileVersion')
configChgTrapNeTypeoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'configChgTrapNeType')
configChgTrapNEIDoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'configChgTrapNEID')
configChgTrapTimeoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'configChgTrapTime')
configChgTrapValue1oid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'configChgTrapValue1')
print configChgTrapValue1oid
objectid = array([configChgTrapNeTypeoid+'.0',configChgTrapNEIDoid+'.0',configChgTrapTimeoid+'.0',configChgTrapValue1oid+'.0'],String)
nodetypes = array(["Integer","Gauge","String","String"],String)
starttime = time.time()
print time.strftime('%Y-%m-%d %X',time.localtime(time.time()))

n = 0
while n < 1:
    nodeBSysSkipDlTriggerOIDWithInstance=scriptinterface.getCurrentOIDWithInstance()
    nodeBSysSkipDlTriggerOID=scriptinterface.getCurrentOID()
    nodeBSysSkipDlTriggerInstance=nodeBSysSkipDlTriggerOIDWithInstance.replace(nodeBSysSkipDlTriggerOID,'')
    nodeBSysSkipDlTrigger = scriptinterface.getNodeValue(nodeBSysSkipDlTriggerOID,nodeBSysSkipDlTriggerInstance)
    if nodeBSysSkipDlTrigger == "1":
        values = array(['0',enodebid,"2011-11-11 11:11:11",nodeBDestCfgFileVersionoid+'.0'+"|3|"+time.strftime('%Y-%m-%d %X',time.localtime(time.time()))],String)
        for m in range(0,1):
            scriptinterface.sendV2Trap(mgrName,162,"public",configChgTrapOID,objectid,nodetypes,values)
        time.sleep(1)
        n = 0
    if  nodeBSysSkipDlTrigger =="0":
        print "off"
        n = 1
        
