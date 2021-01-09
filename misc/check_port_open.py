import socket
host =  'thlogon-uat.aia.biz'#'thlogon.aia.biz' #'thadcplwcm11'#'thcmic.aia.biz'#'thcmic-uat.aia.biz'#'thadculwmi01'#'thadcplwcm13'
port = 22
ports = [22, 80, 9080, 443, 5455]
mail_hosts = ['smtpsg-int.aia.biz','smtphk-int.aia.biz']

def check_port():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host,port))
    if result == 0:
       print(f"{host} Port {port} is open")
    else:
       print(f"{host} Port {port} is not open")
    sock.close()

def check_port(port_list):
    for p in port_list:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((host,p))
        if result == 0:
           print(f"{host} Port {p} is open")
        else:
           print(f"{host} Port {p} is not open")
        sock.close()
        
def check_mail_host():
    for h in mail_hosts:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((h, 25))
        if result == 0:
           print(f"{h} Port 25 is open")
        else:
           print(f"{h} Port 25 is not open")
        sock.close()

def check_host_port(host_n_port):
    for k, v in host_n_port.items():
        for p in v:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((k, p))
            if result == 0:
               print(f"{k} Port {p} is open")
            else:
               print(f"{k} Port {p} is not open")
            sock.close()

#thlogon-uat.aia.biz = { 'thlogon-uat.aia.biz': (443)}
uat_commonlogon_host = { 'thlogon-uat.aia.biz': (80, 443, 9080) }
prd_commonlogon_host = { 'thlogon.aia.biz': (443,) }
thcmic_uat_host = { 'thcmic-uat.aia.biz': (22, 80, 9080, 443, 5455) }
thadc_ul_wmi01 = { 'thadculwmi02' : (22,5455) }
thcmic_aia_biz = { 'thcmic.aia.biz' : (443,) }
thadc_pl_wcm11 = { 'thadcplwcm11' : (22, 9080) }
thadc_pl_wcm12 = { 'thadcplwcm12' : (22, 9080) }
thadc_pl_wcm13 = { 'thadcplwcm13' : (22, 9080) }
thadc_sl_wmi01 = { 'thadcslwmi01': (5355, ) }
thicp = { 'thicp.aia.biz': (22, 80, 9080, 443, 5455) }


#main function
if __name__ == "__main__":
    #check_port()
    #check_port(ports)
    #check_mail_host()
    #print(type(thcmic_uat_host))
    #check_host_port(thcmic_uat_host)
    check_host_port(thadc_ul_wmi01)
    # check_host_port(thadc_pl_wcm12)
    # check_host_port(thadc_pl_wcm13)
    #check_host_port(uat_commonlogon_host)
    
# as port list is open for each hosts.
# thcmic-uat.aia.biz (10.140.201.37)
# thcmic-uat.aia.biz Port 22 is open
# thcmic-uat.aia.biz Port 80 is open
# thcmic-uat.aia.biz Port 9080 is open
# thcmic-uat.aia.biz Port 443 is open
# thcmic-uat.aia.biz Port 5455 is open
# thadculwmi01 (10.140.101.59)
# thadculwmi01 Port 22 is open
# thadculwmi01 Port 80 is not open
# thadculwmi01 Port 9080 is not open
# thadculwmi01 Port 443 is not open
# thadculwmi01 Port 5455 is open

# thcmic.aia.biz (10.140.216.100)
# thcmic.aia.biz Port 22 is not open
# thcmic.aia.biz Port 80 is not open
# thcmic.aia.biz Port 9080 is not open
# thcmic.aia.biz Port 443 is open
# thcmic.aia.biz Port 5455 is not open

#thadcplwcm11 (10.140.196.102)
# thadcplwcm11 Port 22 is open
# thadcplwcm11 Port 80 is not open
# thadcplwcm11 Port 9080 is open
# thadcplwcm11 Port 443 is not open
# thadcplwcm11 Port 5455 is not open

#thlogon.aia.biz (10.140.213.24)
# thlogon.aia.biz Port 22 is not open
# thlogon.aia.biz Port 80 is not open
# thlogon.aia.biz Port 9080 is not open
# thlogon.aia.biz Port 443 is open
# thlogon.aia.biz Port 5455 is not open
# thlogon-uat.aia.biz (10.140.101.247)
# thlogon-uat.aia.biz Port 22 is not open
# thlogon-uat.aia.biz Port 80 is open
# thlogon-uat.aia.biz Port 9080 is open
# thlogon-uat.aia.biz Port 443 is open
# thlogon-uat.aia.biz Port 5455 is not open