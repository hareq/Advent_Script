from java.io import FileInputStream,FileOutputStream,IOException
from java.lang import Throwable,Exception,String,System
from jarray import zeros
from java.util.zip import GZIPOutputStream,ZipOutputStream,ZipFile,ZipEntry
from jarray import array
from java.lang import String
from java.lang import Thread


enodebip = scriptinterface.getSnmpIPAddress()

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

configChgTrapOID = ".1.3.6.1.4.1.5105.80.1.6.1.3"
mgrName = neaip
nodeBSysFunctionIdoid = scriptinterface.getSnmpOidForNodeName(enodebip,161,'nodeBSysFunctionId')
enodebid = scriptinterface.getNodeValue(nodeBSysFunctionIdoid,'.0')


softwarePackVersionoid = scriptinterface.getSnmpOidForNodeName(enodebip,161,'softwarePackVersion')

mainsoftwarePackVersionvlue = scriptinterface.getNodeValue(softwarePackVersionoid,".0")
standbysoftwarePackVersionvlue = scriptinterface.getNodeValue(softwarePackVersionoid,".1")

print mainsoftwarePackVersionvlue
print standbysoftwarePackVersionvlue

configChgTrapNeTypeoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'configChgTrapNeType')
configChgTrapNEIDoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'configChgTrapNEID')
configChgTrapTimeoid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'configChgTrapTime')
configChgTrapValue1oid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'configChgTrapValue1')

objectid = array([configChgTrapNeTypeoid+'.0',configChgTrapNEIDoid+'.0',configChgTrapTimeoid+'.0',configChgTrapValue1oid+'.0'],String)
nodetypes = array(["Integer","Gauge","String","String"],String)

Thread.currentThread().sleep(5*1000)

values = array(['0',enodebid,"2011-11-11 11:11:11",softwarePackVersionoid+'.0'+"|3|"+standbysoftwarePackVersionvlue],String)
scriptinterface.sendV2Trap(mgrName,162,"public",configChgTrapOID,objectid,nodetypes,values)

values = array(['0',enodebid,"2011-11-11 11:11:11",softwarePackVersionoid+'.1'+"|3|"+mainsoftwarePackVersionvlue],String)
scriptinterface.sendV2Trap(mgrName,162,"public",configChgTrapOID,objectid,nodetypes,values)

Thread.currentThread().sleep(3*1000)
scriptinterface.stopAgent(enodebip,"161","")

Thread.currentThread().sleep(120*1000)
scriptinterface.startAgent(enodebip,"161","")



