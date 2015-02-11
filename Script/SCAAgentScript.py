

from jarray import array
from java.lang import String

import threading
from time import localtime, strftime, sleep
import gzip
import os
import re

#
# AbstractSim.py
#

class AbstractSim:
	
	community = "public"
	port = 162
	
	'''all Trap/Inform nitifcations definition.
	eventGeneralEventTrap
	fileTransTrap
	configChgTrap(inform)
	
	These are common of enodeb mib definition.
'''
	
	#fileTran
	fTTrapOid               = ".1.2.156.112566.1.1.1.13"
	foCorrelationNoOid      = ".1.2.156.112566.1.1.1.11.1.1"
	foResultOid = ".1.2.156.112566.1.1.1.12"
	
	#oid array
	fTOidArray = [foCorrelationNoOid,
	foResultOid]
		
#
# CfgInfo.py
#


class FtpInfo:
	
	ip = None
	port = 21
	user = None
	pass1 = None
	managerip = None
	
	def __init__(self,ip,port,user,pass1,managerip):
		self.ip = ip
		self.port = port
		self.user = user
		self.pass1 = pass1
		self.managerip = managerip


#
# Logger.py
#

class Logger:

	enbUtil = None
	classname = None
	
	def __init__(self,classname):
		self.enbUtil = EnbUtil()
		self.classname = classname


	def getLogPre(self):
		return self.enbUtil.getCurrentTime() + ' [' + self.classname + '] '


class LoggerFactory:
	
	def getLogger(aclass):
		return Logger(aclass)
	
	getLogger = staticmethod(getLogger)


#
# FileParse.py
#

class FileParse:

	def parseFtpInfo(self, ftpfile):
		log = LoggerFactory.getLogger('FileParse')
		fh = None
		try:
			fh = open(ftpfile, 'r+')
			data = []

			for lino, line in enumerate(fh):
				line = line.rstrip()
				if not line:
					print 'invalid line'
					continue
				
				data.append(line)
			
			ip = None
			port = -1
			user = None
			pass1 = None
			managerip = None

			for v in data:
				if(v.find('=',0,len(v)) == -1):
					continue
				
				indx = v.index('=',0,len(v)) + 1
				if(v.find('ftpip',0,indx) >= 0):
					ip = v[indx:]
				elif(v.find('port',0,indx) >= 0):
					port = int(v[indx:]);		
				elif(v.find('user',0,indx) >= 0):
					user = v[indx:]
				elif(v.find('pass',0,indx) >= 0):
					pass1 = v[indx:]
				elif(v.find('managerip',0,indx) >= 0):
					managerip = v[indx:]
			
			if(ip == None or port == 0 or user == None or pass1 == None or managerip == None):
				return
			else:
					return FtpInfo(ip,port,user,pass1,managerip)
	
		except Exception, err:
			print 'read ftpinfo file failed'
			print str(err)
			return None
		finally:
			if fh is not None:
				fh.close()

#
# EnbUtil.py
#
#
class EnbUtil:
	
	def getCurrentTime(self):
		return strftime("%Y-%m-%d %H:%M:%S", localtime())

	def enbSleep(self,nsec):
		sleep(nsec)

#
# EnbFileManager.py
#
#

class FileManager:
	basicfile = None
	
	def __init__(self,basicfile):
		self.basicfile = basicfile
		self.log = LoggerFactory.getLogger(__name__)


	def genSCAInfo(self, enodebid, enodebip):
		f=open(self.basicfile,'r+')
		bytes_in = f.read()
		moban = bytes_in.decode('utf-8')	  
		f.close()
	
		dcb = str(enodebid) + '.dcb'
		f1=open(dcb,'w+')
		bytes_out = moban.encode('utf-8')
		f1.write(bytes_out)
		f1.close()
		return dcb


#
#
# SnmpSimLib.py 
#

class SnmpSim(AbstractSim):

	enbUtil = EnbUtil()
	log = LoggerFactory.getLogger('SnmpSim')

	#fileTransTrap
	ftObjectid = array(AbstractSim.fTOidArray,String)
	ftNodeTypes = array(["Gauge","Integer"],String)

	def sendFT(self, mgrName, neid, result):
		taskid = scriptinterface.getCurrentInstance()
		taskid = taskid[1:]
		values = [taskid,result]
		scriptinterface.sendV2Trap(mgrName,162,"public",AbstractSim.fTTrapOid,self.ftObjectid,self.ftNodeTypes,values)
		print self.log.getLogPre() + " send FT trap to " + mgrName
		i = 0
		for v in values:
			print self.log.getLogPre() + " sendFT value" + str(i) + " is " + v
			i = i + 1

	def getNeId(self):
		neid = scriptinterface.getNodeValue(".1.2.156.112566.1.1.1.3.2",".0")
		if(neid is not None):
			return int(neid)		
		return None


	def getAgentIp(self):
		return scriptinterface.getSnmpIPAddress()


	def getAgentPort(self):
		return int(scriptinterface.getSnmpPort())


	def startAgent(self,ip,port):
		scriptinterface.startAgent(ip, str(port), "");

		
	def stopAgent(self,ip,port):
		scriptinterface.stopAgent(ip, str(port), "");

	#When the filename was set, other properties should all be set.
	def isFileTransferTask(self):
		currentOid = scriptinterface.getCurrentOID()
		if(currentOid.find('.1.2.156.112566.1.1.1.11.1.2',0,len(currentOid)) == -1):
			print "not find the oid"
			return False
		else:
			return "1"
		


	def uploadCfgFile(self, neId, ip, ftpInfo, taskId):				
		destdir = scriptinterface.getNodeValue(".1.2.156.112566.1.1.1.11.1.3",taskId)
		if(destdir is None):
			print "Not upload, the destdir is none."
			return

		filename = scriptinterface.getNodeValue(".1.2.156.112566.1.1.1.11.1.4",taskId)
		print "filename:" + filename
		if(filename is None):
			print "Not upload, the filename is none."
			return

		cfileCreator = None
		src = str(neId) + ".dcb"
		if(os.path.exists(src)):
			os.remove(src)
	
		cfileCreator = FileManager("moban_sca.dcb")
		src = cfileCreator.genSCAInfo(neId,ip)
		
		if(src == None):
			print self.log.getLogPre() + "upload failed as create cfg file failed."
			return
		
		ddist = str(neId)
		fin = None
		fout = None
		try:
			fin=open(src, 'r+')
			fout=gzip.open(ddist, 'w+b')
			  
			content = fin.read()
			fout.write(content)

		except Exception, err:
			print self.log.getLogPre() + 'This is Exception is %s' % err
			return
		finally:
			if(fin != None):
				fin.close()
			if(fout != None):
				fout.close()

		try:
			if(os.path.exists(filename)):
				os.remove(filename)

			os.rename(ddist, filename)
		except Exception, err:
			print self.log.getLogPre() + 'This is Exception is ' + str(err)
			return

		filepath = destdir +'/' + filename
		print self.log.getLogPre() + "begin uploading file " + filename + " to " + ftpInfo.ip
		print self.log.getLogPre() + "the filepath is " + filepath
		scriptinterface.uploadFile(ftpInfo.ip, ftpInfo.port, filename, filepath,1, "ftp", ftpInfo.user, ftpInfo.pass1);		
		return filepath

	def uploadAlarmFile(self, neId, ip, ftpInfo, taskId):
		#same with above, get the file directory and file name.
		destdir = scriptinterface.getNodeValue(".1.2.156.112566.1.1.1.11.1.3",taskId)
		if(destdir is None):
			print "Not upload, the destdir is none."
			return

		filename = scriptinterface.getNodeValue(".1.2.156.112566.1.1.1.11.1.4",taskId)
		print "filename:" + filename
		if(filename is None):
			print "Not upload, the filename is none."
			return
		
		#Copy only, no modification
		f=open('alarmSCA.xml','r+')
		bytes_in = f.read()
		moban = bytes_in.decode('utf-8')	  
		f.close()
		
		f1=open(filename,'w+')
		bytes_out = moban.encode('utf-8')
		f1.write(bytes_out)
		f1.close()
		
		filepath = destdir +'/' + filename
		print self.log.getLogPre() + "begin uploading file " + filename + " to " + ftpInfo.ip
		print self.log.getLogPre() + "the filepath is " + filepath
		scriptinterface.uploadFile(ftpInfo.ip, ftpInfo.port, filename, filepath,1, "ftp", ftpInfo.user, ftpInfo.pass1);		
		return filepath
		
#
#
# SCA.py
#

class SCA:
	
	ip = None
	port = -1
	managerIp = None
	community = "public"
	neId = None
	currentVersion = None
	backupVersion = None
	cfgVersion = None
	ftpInfo = None	
	snmpSimulator = None
	enbUtil = None


	def __init__(self,ip,port,ftpInfo,neId, simulator):
		self.ip = ip
		self.port = port
		self.ftpInfo = ftpInfo
		self.managerIp = ftpInfo.managerip
		self.neId = neId
		self.snmpSimulator = simulator
		self.enbUtil = EnbUtil()
		self.log = LoggerFactory.getLogger(__name__)

	#
	def dealCfgUpload(self):
		taskId = scriptinterface.getCurrentInstance()
		ftype = scriptinterface.getNodeValue(".1.2.156.112566.1.1.1.11.1.2",taskId)
		print "ftype:" + ftype
		if(int(ftype) != 1):
			print self.log.getLogPre() + "Not to upload the cfg file to omc, the ftype is " + ftype
			return

		result = self.snmpSimulator.uploadCfgFile(self.neId,self.ip,self.ftpInfo,taskId)
		if(result == None):
			print self.log.getLogPre() + "Upload cfg file failed"
			self.snmpSimulator.sendFT(self.managerIp, self.neId, "1")
			return False
		else:
			self.snmpSimulator.sendFT(self.managerIp, self.neId, "0")
			return "1"
	
	def dealAlarmUpload(self):
		taskId = scriptinterface.getCurrentInstance()
		ftype = scriptinterface.getNodeValue(".1.2.156.112566.1.1.1.11.1.2",taskId)
		print "ftype:" + ftype
		if(int(ftype) != 2):
			print self.log.getLogPre() + "Not to upload the alarm file to omc, the ftype is " + ftype
			return
		
		result = self.snmpSimulator.uploadAlarmFile(self.neId,self.ip,self.ftpInfo,taskId)
		if(result == None):
			print self.log.getLogPre() + "Upload alarm file failed"
			self.snmpSimulator.sendFT(self.managerIp, self.neId, "1")
			return False
		else:
			self.snmpSimulator.sendFT(self.managerIp, self.neId, "0")
			return "1"

	def dealReboot(self):
		print self.log.getLogPre() + "Begin to reboot the agent:" + self.ip
		self.snmpSimulator.stopAgent(self.ip,self.port)
		self.enbUtil.enbSleep(15)		
		self.snmpSimulator.startAgent(self.ip,self.port)
		print self.log.getLogPre() + "Agent reboot end:" + self.ip

		
#End


#
# Run script
#

# Init Enb

def main():
	try:
		print "hello SCA agent is ok"
		snmpSimulator = SnmpSim()
		agentIp = snmpSimulator.getAgentIp()
		port = snmpSimulator.getAgentPort()
		neId = snmpSimulator.getNeId()
		
		if(neId is None):
			print 'Can not get the neId'
			return

		fileparser = FileParse()		

		ftpInfo = fileparser.parseFtpInfo("ftp.txt")
		if(ftpInfo == None):
			print 'please configure the ftpinfo into file ftp.txt'
			return
	
		sca = SCA(agentIp,port,ftpInfo,neId,snmpSimulator)	
	
		if(snmpSimulator.isFileTransferTask()):
			if(sca.dealCfgUpload()):
				print "FileTransfer: cfg file upload"
			elif(sca.dealAlarmUpload()):
				print "FileTransfer: alarm file upload"
		else:
			print "Not a cfg file upload task"
		
	except Exception, err:
		print str(err)

main()
