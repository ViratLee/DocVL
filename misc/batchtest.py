from subprocess import Popen
p = Popen("batch.bat", cwd=r"D:\\Apps-cas\\WinPython-3.6.3.0Qt5\\notebooks\\misc")
stdout, stderr = p.communicate()