@echo off


call .\SetEnv.bat

cd ..


%JAVA_HOME%\bin\java -mx200M -Djava.net.preferIPv4Stack=false -DEnbAgentScript=%STKT_HOME%\\EnbAgentScript.py -Dpython.home=.\jython -Djython.jar=.\jars\jython.jar -Dpython.packages.paths=jython.jar,sun.boot.class.path,java.class.path com.adventnet.simulator.ndt.NdtMainFrame -h .\help\index.html -PORT 161 -HOST localhost -MS_MODE 3


cd bin
