import io
from datetime import datetime
start = datetime.now()
filename = "D:\\logs\\prod\\20201121\\ii\\log_SystemOut_20.11.21.tar\\log_SystemOut_20.11.21\\SystemOut_20.11.21_09.18.11.log"
with io.open(filename,'r',encoding='utf8') as o:
    print(o)