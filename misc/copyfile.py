from shutil import copy2, move
import glob, os
#document_path = 'CorresponedencePending'
document_path = 'RequestDocument'
#document_path = 'SettlementProviderFax'
#source_dir = 'D:\\Apps-cas\\workspace\\eForm\\jasper\\jrxml'
source_dir = 'C:\\Users\\asnpatd\\JaspersoftWorkspace\\eFrmWS\\jasper\\jrxml'
dest_dir = 'D:\\Apps-cas\\workspace\\eForm\\jasper\\template'
#D:\Apps-cas\workspace\eForm\jasper\template\CorresponedencePending
source_dir = '{}\\{}'.format(source_dir,document_path)
dest_dir = '{}\\{}'.format(dest_dir,document_path)
#source_dir = 'D:\\temp'
#dest_dir = 'D:\\temp1'
#files = glob.iglob(os.path.join(source_dir,"*.jasper"))
#files = [source_dir+'\\PREAUTHIBFAX.jasper',source_dir+'\\HospitalExpensesPreAuth.jasper',source_dir+'\\CSPREAUTH.jasper']
#files = [source_dir+'\\SUB_PREAUTHCSFAX.jasper',source_dir+'\\PREAUTHCSFAX.jasper']
files = [source_dir+'\\C12301.jasper']
for file in files:
    if os.path.isfile(file):
        copy2(file, dest_dir)
        print(f"copy {file} ")
        src = os.path.join(source_dir, file)
        os.remove(src)
        #move(file, os.path.join(dest_dir))
        ###move file####
        # src = os.path.join(source_dir, file)
        # dest = os.path.join(dest_dir, file) 
        # if os.path.exists(dest):
        #     ret = input('file '+file+' is exit replace ? \'Y\' or \'N\':')
        #     if ret == 'Y':
        #         os.remove(dest)
        #         move(src, dest_dir)
        #         print('move {}', file)
