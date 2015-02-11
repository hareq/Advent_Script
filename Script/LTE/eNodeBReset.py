from java.lang import Thread

enodebip=scriptinterface.getSnmpIPAddress()
nodeBSysResetTriggeroid=scriptinterface.getSnmpOidForNodeName(enodebip,161,'nodeBSysResetTrigger')
nodeBSysResetTrigger = scriptinterface.getNodeValue(nodeBSysResetTriggeroid,".0")

if nodeBSysResetTrigger=='1':
    scriptinterface.stopAgent(enodebip,"161","")
    Thread.currentThread().sleep(60*1000)
    scriptinterface.startAgent(enodebip,"161","")

