from shutil import copy2
import os
import re
# cmic_config_dir = 'D:\\Apps-cas\\workspace\\CMiCAPP\\CMiC\\src\\main\\java\\com\\aia\\cmic\\config'
# backup_config_dir = 'D:\\ws\\backlog\\2020 project\\HNW Deduct\\src\\aia\\cmic\\config'
# config_list = ['CXFConfig.java']

dir_src = 'D:\\ws\\backlog\\2020 project\\Y20-1 iClaim\\20201223_src'

cmic_contrl_dir = 'D:\\Apps-cas\\workspace\\CMiCAPP\\CMiC\\src\\main\\java\\com\\aia\\cmic\\controller'
backup_contrl_dir = dir_src +'\\aia\\cmic\\controller'
contrl_list = ['ClaimController.java','BillingController.java']

cmic_rest_dir = 'D:\\Apps-cas\\workspace\\CMiCAPP\\CMiC\\src\\main\\java\\com\\aia\\cmic\\rest'
backup_rest_dir = dir_src +'\\aia\\cmic\\rest'
file_rest_list = ['ClaimRest.java','UtilityRest.java']

cmic_service_dir = 'D:\\Apps-cas\\workspace\\CMiCAPP\\CMiC\\src\\main\\java\\com\\aia\\cmic\\services'
backup_service_dir = dir_src +'\\aia\\cmic\\services'
file_service_list = [
    'SettlementService.java',
    'ClaimService.java']

cmic_service_impl_dir = 'D:\\Apps-cas\\workspace\\CMiCAPP\\CMiC\\src\\main\\java\\com\\aia\\cmic\\services\\impl'
backup_service_impl_dir = dir_src +'\\aia\\cmic\\services\\impl'
file_service_impl_list = ['SettlementServiceImpl.java', 'ClaimServiceImpl.java']

cmic_rest_repo_dir = 'D:\\Apps-cas\\workspace\\CMiCAPP\\CMiC\\src\\main\\java\\com\\aia\\cmic\\repository\\rest'
backup_rest_repo_dir = dir_src +'\\aia\\cmic\\repository\\rest'
file_rest_repo_list = ['ClaimRestRepositoryImpl.java']

cmic_repository_impl_dir = 'D:\\Apps-cas\\workspace\\CMiCAPP\\CMiC\\src\\main\\java\\com\\aia\\cmic\\repository\\impl'
backup_repository_impl_dir = dir_src +'\\aia\\cmic\\repository\\impl'
file_repository_impl_list = ['ClaimPaymentTransferRepositoryImpl.java']
#'BenefitItemRepository.java',
#     'impl\BenefitItemRepositoryHbmImpl.java',
#     'ClaimDeductDetailRepository.java',
#     'impl\ClaimDeductDetailRepositoryHbmImpl.java',
#     'ClaimDeductRepository.java',
#     'impl\ClaimDeductRepositoryHbmImpl.java',
#     'ClaimPaymentRepository.java',
#     'impl\ClaimPaymentRepositoryHbmImpl.java',
#     'ClaimPolicyCoverageRepository.java',
#     'impl\ClaimPolicyCoverageHbmImpl.java',
#     'ClaimRepository.java',
#     'impl\ClaimRepositoryHbmImpl.java']

# cmic_entity_dir = 'D:\\Apps-cas\\workspace\\CMiCAPP\\CMiC\\src\\main\\java\\com\\aia\\cmic\\entity'
# backup_entity_dir = 'D:\\ws\\backlog\\2020 project\\HNW Deduct\\src\\aia\\cmic\\entity'
# file_entity_list = ['BenefitItem.java',
#     'Claim.java',
#     'ClaimDeduct.java',
#     'ClaimDeductDetail.java',
#     'ClaimPayment.java']

cmic_helper_dir = 'D:\\Apps-cas\\workspace\\CMiCAPP\\CMiC\\src\\main\\java\\com\\aia\\cmic\\services\\helper'
backup_helper_dir = dir_src +'\\aia\\cmic\\services\\helper'
file_helper_list = ['ClaimHelper.java']

cmic_model_src_dir = 'D:\\Apps-cas\\workspace\\CMiCAPP\\CMiC\\src\\main\\java\\com\\aia\\cmic\\model'
cmic_model_dest_dir = dir_src +'\\aia\\cmic\\model'
cmic_model_list = ['CaseDataEntry.java','BaseCaseData.java','DocumentiClaimRecordSearchResult.java','DocumentRecordDetailModel.java']

cmic_js_dir = 'D:\\Apps-cas\\workspace\\CMiCAPP\\CMiC\\src\\main\\webapp\\js\\page'
backup_js_dir = dir_src +'\\js\\page'
page_js_list = ['simplifySubmission.js']

cmic_html_dir1 = 'D:\\Apps-cas\\workspace\\CMiCAPP\\CMiC\\src\\main\\webapp\\WEB-INF\\templates\\claim'
dest_html_dir1 = dir_src +'\\WEB-INF\\templates\\claim'
html_list1 = ['simplifySubmission.html']

cmic_html_dir2 = 'D:\\Apps-cas\\workspace\\CMiCAPP\\CMiC\\src\\main\\webapp\\WEB-INF\\templates\\payment'
dest_html_dir2 = dir_src +'\\WEB-INF\\templates\\payment'
html_list2 = ['iClaimDocumentRecord.html']

# cmic_html_dir2 = 'D:\\Apps-cas\\workspace\\CMiCAPP\\CMiC\\src\\main\\webapp\\WEB-INF\\templates\\claim'
# dest_html_dir2 = 'D:\\ws\\backlog\\2020 project\\HNW Deduct\\src\\WEB-INF\\templates\\claim'
# html_list2 = ['benefitDetermination.html',
#     'caseDataEntry.html',
#     'section\\benefitdetermination_table_detail.html',
#     'hnw_deduct.html',
#     'hnw_deduct_accumulate.html',
#     'hnw_deduct_detail.html',
#     'settlementDetail.html']

# cmic_css__dir = 'D:\\Apps-cas\\workspace\\CMiCAPP\\CMiC\\src\\main\\webapp\\styles'
# dest_css_dir = 'D:\\ws\\backlog\\2020 project\\HNW Deduct\\src\\styles'
# page_css_list = ['site.css']
def makeSureDirExit(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def backupFile(src_dir, desc_dir, list_file):
    count = 0
    makeSureDirExit(desc_dir)
    print("backup...")
    for file in list_file:
        full_path_file = f'{src_dir}\\{file}' 
        if os.path.isfile(full_path_file):
            copy2(full_path_file, desc_dir)
            print(f"backup from {full_path_file} ")
            print(f"         to {desc_dir} ")
            count = count+ 1
        else:
            print(f"*******not found {full_path_file}.")
            #Path("/my/directory").mkdir(parents=True, exist_ok=True)
    print(f"-----{count}----")
    return count;

def updateFile(cmic_dir, backup_dir, list_file):
    count = 0
    print("update...")
    for file in list_file:
        ind = file.rfind('\\')
        fdir = None
        sfile = file
        if ind >= 0:
            #print(f"ind:{ind}")
            sfile = file[ind+1:]
            #print(f"{file} to {sfile}")
            fdir = file[:ind]
            #print(f"{fdir}")
        cmic_path_file = f'{cmic_dir}\\{fdir}\\{sfile}' if fdir else f'{cmic_dir}\\{file}'
        if os.path.isdir(backup_dir):
            backup_path_file = f'{backup_dir}\\{sfile}'
            print(f"update from {backup_path_file}")
            print(f"         to {cmic_path_file}")
            copy2(backup_path_file, cmic_path_file)
            count = count + 1
        else:
            print(f"*******not found {backup_dir}")
    return count;

if __name__ == '__main__':
   
    backup_count = 0
   
    # backup_count = backup_count + backupFile(cmic_contrl_dir, backup_contrl_dir, contrl_list)
    # backup_count = backup_count + backupFile(cmic_rest_dir,backup_rest_dir,file_rest_list)
    # backup_count = backup_count + backupFile(cmic_service_dir,backup_service_dir,file_service_list)
    # backup_count = backup_count + backupFile(cmic_service_impl_dir,backup_service_impl_dir,file_service_impl_list)
    # backup_count = backup_count + backupFile(cmic_helper_dir,backup_helper_dir,file_helper_list)
    # backup_count = backup_count + backupFile(cmic_repository_impl_dir,backup_repository_impl_dir,file_repository_impl_list)
    # backup_count = backup_count + backupFile(cmic_rest_repo_dir,backup_rest_repo_dir,file_rest_repo_list)
    # backup_count = backup_count + backupFile(cmic_model_src_dir,cmic_model_dest_dir,cmic_model_list)
    # backup_count = backup_count + backupFile(cmic_js_dir, backup_js_dir, page_js_list)
    # backup_count = backup_count + backupFile(cmic_html_dir1, dest_html_dir1, html_list1)
    # backup_count = backup_count + backupFile(cmic_html_dir2, dest_html_dir2, html_list2)



    backup_count = backup_count + updateFile(cmic_contrl_dir, backup_contrl_dir, contrl_list)
    backup_count = backup_count + updateFile(cmic_rest_dir,backup_rest_dir,file_rest_list)
    backup_count = backup_count + updateFile(cmic_model_src_dir,cmic_model_dest_dir,cmic_model_list)
    backup_count = backup_count + updateFile(cmic_service_dir,backup_service_dir,file_service_list)
    backup_count = backup_count + updateFile(cmic_service_impl_dir,backup_service_impl_dir,file_service_impl_list)
    backup_count = backup_count + updateFile(cmic_helper_dir,backup_helper_dir,file_helper_list)
    backup_count = backup_count + updateFile(cmic_repository_impl_dir,backup_repository_impl_dir,file_repository_impl_list)
    backup_count = backup_count + updateFile(cmic_rest_repo_dir,backup_rest_repo_dir,file_rest_repo_list)
    backup_count = backup_count + updateFile(cmic_js_dir, backup_js_dir, page_js_list)
    backup_count = backup_count + updateFile(cmic_html_dir1, dest_html_dir1, html_list1)
    backup_count = backup_count + updateFile(cmic_html_dir2, dest_html_dir2, html_list2)
    
    
    
    
    print(f' total update {backup_count} files')