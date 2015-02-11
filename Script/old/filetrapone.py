from java.io import FileInputStream,FileOutputStream,IOException
from java.lang import Throwable,Exception,String,System
from jarray import zeros
from java.util.zip import GZIPOutputStream,ZipOutputStream,ZipFile,ZipEntry
from jarray import array
from java.lang import String


FileoidInstance=scriptinterface.getCurrentOIDWithInstance()
FileOID=scriptinterface.getCurrentOID()
FileInstance=FileoidInstance.replace(FileOID,'')

enodebid = scriptinterface.getNodeValue(".1.3.6.1.4.1.5105.80.1.2.2.1.4",FileInstance)



enodebidlen=len(enodebid)

for enodebidn in range(0,enodebidlen):
    if enodebid[enodebidn]=='/':
        enodebid1=enodebid[7:enodebidn]
enodebid=enodebid1
dcb=enodebid+'.dcb'





e = 'true';
try:
    f = open(dcb,'r')
    f.close()
except :
    e = 'false'
    
if e == 'true':
    def gzip(src,dist):
        #print 'gzip start'
        try:
            #print 'gzip start1'
            fin = FileInputStream(src);
            fout = FileOutputStream(dist);
            gzout = GZIPOutputStream(fout);
            #print 'gzip start2'
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
        print 'zip start'
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
            

    dcb=enodebid+'.dcb'
    zipname=enodebid+'.gzip'
    gzip(dcb,zipname)
    
    f=open('C:\AdventNet\config.dcb','r')
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
      #print nn
      f.seek(n)
      neaip=f.read(nn)
      #print neaip
     f.seek(n)
     t=f.read(7)
     if t=="ftpip='":
      n=f.tell()
      #print n
      nn=0
      while "'"!=f.read(1):
       nn=nn+1
      #print nn
      f.seek(n)
      ftpip=f.read(nn)
      #print ftpip
     f.seek(n)
     t=f.read(13)
     if t=="ftpuserName='":
      n=f.tell()
      #print n
      nn=0
      while "'"!=f.read(1):
       nn=nn+1
      #print nn
      f.seek(n)
      ftpuserName=f.read(nn)
      #print ftpuserName
     f.seek(n)
     t=f.read(13)
     if t=="ftppassword='":
      n=f.tell()
      #print n
      nn=0
      while "'"!=f.read(1):
       nn=nn+1
      #print nn
      f.seek(n)
      ftppassword=f.read(nn)
      #print ftppassword


    lujing='eNodeB='+enodebid+'/FullCfg/'+zipname
    scriptinterface.uploadFile(ftpip, 21, zipname, lujing,1, "ftp", ftpuserName, ftppassword);


    mgrName = neaip
    mgrPort = 162
    community = "public"
    trapOID = ".1.3.6.1.4.1.5105.80.1.6.2.7"



     
    objectid = array([".1.3.6.1.4.1.5105.80.1.6.2.8.1.0",".1.3.6.1.4.1.5105.80.1.6.2.8.2.0",".1.3.6.1.4.1.5105.80.1.6.2.8.3.0",".1.3.6.1.4.1.5105.80.1.6.2.8.4.0",".1.3.6.1.4.1.5105.80.1.6.2.8.5.0",".1.3.6.1.4.1.5105.80.1.6.2.8.6.0",".1.3.6.1.4.1.5105.80.1.6.2.8.7.0",".1.3.6.1.4.1.5105.80.1.6.2.8.8.0"],String)
    nodetypes = array(["Gauge","Gauge","Integer","String","Integer","Integer","Gauge","String"],String)
     

    value = scriptinterface.getNodeValue(".1.3.6.1.4.1.5105.80.1.2.2.1.2",FileInstance)
    value = int(value)

    
    
    Filetaskid=FileInstance[1]


    if (value == 15):
     values = array([enodebid,Filetaskid,"15",lujing,"1","0","1","2011-11-11 11:11:11"],String)
     scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)
     
    if (value == 13):
     values =  array([enodebid,Filetaskid,"13",lujing,"2","0","1","2011-11-11 11:11:11"],String)
     scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)
     values =  array([enodebid,"53","1","eventGeneralEventSource","eNB Static startup","2011-11-11 11:11:11"],String)
     eventtrapOID=".1.3.6.1.4.1.5105.80.1.6.2.1"
     eventobjectid=array([".1.3.6.1.4.1.5105.80.1.6.2.2.1.0",".1.3.6.1.4.1.5105.80.1.6.2.2.2.0",".1.3.6.1.4.1.5105.80.1.6.2.2.3.0",".1.3.6.1.4.1.5105.80.1.6.2.2.4.0",".1.3.6.1.4.1.5105.80.1.6.2.2.5.0",".1.3.6.1.4.1.5105.80.1.6.2.2.6.0"],String)
     eventnodetypes=array(["Integer","Integer","Integer","String","String","String"],String)
     scriptinterface.sendV2Trap(mgrName,mgrPort,community,eventtrapOID,eventobjectid,eventnodetypes,values)     
          
    if (value == 16):
     values = array([enodebid,Filetaskid,"16",lujing,"1","0","1","2011-11-11 11:11:11"],String)
     scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)


if e == 'false':

    enodebidlen=len(enodebid)
    for enodebidn in range(0,enodebidlen):

     if enodebid[enodebidn]=='/':
      enodebid1=enodebid[7:enodebidn]
    enodebid=enodebid1

    enodebip=scriptinterface.getSnmpIPAddress()

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
     #print enodebidox
     


    
    NodeBFunction=enodebidox
    nodeBSysFunctionId=enodebid
    nodeBGlobalId=enodebid
    nodeBSysOMAddr=enodebip
    try:

     f=open('C:\AdventNet\moban.dcb','r+')
     str=f.read()
     m=len(str)
     try:
      for n in range(0,m):
       f.seek(n)
       t=f.read(18)
       if t=='<sn>NodeBFunction=':
        dcb=enodebid+'.dcb'
        f1=open(dcb,'w+')

        #f1.truncate()
        nm=f.tell()
        nn=0
        while '<'!=f.read(1):
         nn=nn+1
        f.seek(0,0)
        t=f.read(nm)
        f1.write(t)
        f1.write(NodeBFunction)
        f1.close()
        n1=nm
        #print '1'
       f.seek(n)
       t=f.read(20)
       if t=='<nedn>NodeBFunction=':
        f1=open(dcb,'a+')
        nm=f.tell()  
        n2=nm-n1-nn
        n1=n1+nn
        f.seek(n1,0)
        t=f.read(n2)
        f1.write(t)
        f1.write(NodeBFunction)
        f1.close()
        n1=nm
        f.seek(nm)
        nn=0
        while '<'!=f.read(1):
         nn=nn+1
        #print '2'
        
       f.seek(n)
       t=f.read(40)
       if t=='.1.3.6.1.4.1.5105.80.10.200.1.9.0</i><r>':
        f1=open(dcb,'a+')
        nm=f.tell()
        n2=nm-n1-nn
        n1=n1+nn
        f.seek(n1,0)
        t=f.read(n2)
        f1.write(t)
        f1.write(nodeBSysFunctionId)
        f1.close()
        n1=nm
        f.seek(nm)
        nn=0
        while '<'!=f.read(1):
         nn=nn+1
        #print '3'
        
       f.seek(n)
       t=f.read(41)
       if t=='.1.3.6.1.4.1.5105.80.10.200.1.11.0</i><r>':
        f1=open(dcb,'a+')
        nm=f.tell()
        n2=nm-n1-nn
        n1=n1+nn
        f.seek(n1,0)
        t=f.read(n2)
        f1.write(t)
        f1.write(nodeBGlobalId)
        f1.close()
        
        n1=nm
        f.seek(nm)
        nn=0
        while '<'!=f.read(1):
         nn=nn+1
        #print '4'
        
       f.seek(n) 
       t=f.read(41)
       if t=='.1.3.6.1.4.1.5105.80.10.200.1.23.0</i><r>':
        f1=open(dcb,'a+')
        nm=f.tell()
        n2=nm-n1-nn
        n1=n1+nn
        f.seek(n1,0)
        t=f.read(n2)
        f1.write(t)
        f1.write(nodeBSysOMAddr)        
        nn=0
        while '<'!=f.read(1):
         nn=nn+1
         
        nm=nm+nn
        f.seek(nm)
        
        n2=m-nm
        t=f.read(n2)
        f1.write(t)
        #print '5'
        f1.close()
        #print '6'
     finally:
      #print '7'
      f.close()
      #print '8'
    except IOError:
     pass
    #print 'y'
    #f1 = zipfile.ZipFile('123.zip','w',zipfile.ZIP_DEFLATED)
    #f1.write('moban1.dcb')
    #f1.close()
    def gzip(src,dist):
        #print 'gzip start'
        try:
            #print 'gzip start1'
            fin = FileInputStream(src);
            fout = FileOutputStream(dist);
            gzout = GZIPOutputStream(fout);
            #print 'gzip start2'
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
        print 'zip start'
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
            


    zipname=enodebid+'.gzip'
    gzip(dcb,zipname)






    f=open('C:\AdventNet\config.dcb','r')
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
      #print nn
      f.seek(n)
      neaip=f.read(nn)
      #print neaip
     f.seek(n)
     t=f.read(7)
     if t=="ftpip='":
      n=f.tell()
      #print n
      nn=0
      while "'"!=f.read(1):
       nn=nn+1
      #print nn
      f.seek(n)
      ftpip=f.read(nn)
      #print ftpip
     f.seek(n)
     t=f.read(13)
     if t=="ftpuserName='":
      n=f.tell()
      #print n
      nn=0
      while "'"!=f.read(1):
       nn=nn+1
      #print nn
      f.seek(n)
      ftpuserName=f.read(nn)
      #print ftpuserName
     f.seek(n)
     t=f.read(13)
     if t=="ftppassword='":
      n=f.tell()
      #print n
      nn=0
      while "'"!=f.read(1):
       nn=nn+1
      #print nn
      f.seek(n)
      ftppassword=f.read(nn)
      #print ftppassword


    lujing='eNodeB='+enodebid+'/FullCfg/'+zipname
    scriptinterface.uploadFile(ftpip, 21, zipname, lujing,1, "ftp", ftpuserName, ftppassword);


    mgrName = neaip
    mgrPort = 162
    community = "public"
    trapOID = ".1.3.6.1.4.1.5105.80.1.6.2.7"



     
    objectid = array([".1.3.6.1.4.1.5105.80.1.6.2.8.1.0",".1.3.6.1.4.1.5105.80.1.6.2.8.2.0",".1.3.6.1.4.1.5105.80.1.6.2.8.3.0",".1.3.6.1.4.1.5105.80.1.6.2.8.4.0",".1.3.6.1.4.1.5105.80.1.6.2.8.5.0",".1.3.6.1.4.1.5105.80.1.6.2.8.6.0",".1.3.6.1.4.1.5105.80.1.6.2.8.7.0",".1.3.6.1.4.1.5105.80.1.6.2.8.8.0"],String)
    nodetypes = array(["Gauge","Gauge","Integer","String","Integer","Integer","Gauge","String"],String)
     

    value = scriptinterface.getNodeValue(".1.3.6.1.4.1.5105.80.1.2.2.1.2",FileInstance)
    value = int(value)

    Filetaskid=FileInstance[1]



    if (value == 15):
     values = array([enodebid,Filetaskid,"15",lujing,"1","0","1","2011-11-11 11:11:11"],String)
     scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)
     
    if (value == 13):
     values =  array([enodebid,Filetaskid,"13",lujing,"2","0","1","2011-11-11 11:11:11"],String)
     scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)
     values =  array([enodebid,"53","1","eventGeneralEventSource","eNB Static startup","2011-11-11 11:11:11"],String)
     eventtrapOID=".1.3.6.1.4.1.5105.80.1.6.2.1"
     eventobjectid=array([".1.3.6.1.4.1.5105.80.1.6.2.2.1.0",".1.3.6.1.4.1.5105.80.1.6.2.2.2.0",".1.3.6.1.4.1.5105.80.1.6.2.2.3.0",".1.3.6.1.4.1.5105.80.1.6.2.2.4.0",".1.3.6.1.4.1.5105.80.1.6.2.2.5.0",".1.3.6.1.4.1.5105.80.1.6.2.2.6.0"],String)
     eventnodetypes=array(["Integer","Integer","Integer","String","String","String"],String)
     scriptinterface.sendV2Trap(mgrName,mgrPort,community,eventtrapOID,eventobjectid,eventnodetypes,values)     
          
    if (value == 16):
     values = array([enodebid,Filetaskid,"16",lujing,"1","0","1","2011-11-11 11:11:11"],String)
     scriptinterface.sendV2Trap(mgrName,mgrPort,community,trapOID,objectid,nodetypes,values)

                  
