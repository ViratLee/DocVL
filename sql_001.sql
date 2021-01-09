  select * from all_sequences;
  
  REVOKE SELECT ON s_standardbilling FROM PUBLIC;
  ALTER SEQUENCE s_standardbilling  INCREMENT BY 999821;
  SELECT s_standardbilling.nextval  FROM dual;
  ALTER SEQUENCE s_standardbilling  INCREMENT BY 1;
  REVOKE SELECT ON s_standardbilling TO PUBLIC;
---------------------------
select case 
            when exists (select 1 
                         from claim 
                         where partyid = 386414673 and companyid='051' and claimstatus = '40' and claimno like 'C%' ) 
            then 'Y' 
            else 'N' 
        end as rec_exists
from dual;
----
desc all_sequences;
select * from all_sequences;
----------
Insert into SYSTEMCONFIG (PARAMKEY,PARAMVALUE,CREATEDBY,CREATEDDT,LASTMODIFIEDBY,LASTMODIFIEDDT) 
values ('cmic.reservefail.enable.cancel','N','wMUser',current_timestamp,
'wMUser',current_timestamp);

---------
UPDATE
  COMMONCODE
SET
  codevalue = UPPER(codevalue)
where codename = 'PhysicianRole';
---------

-------
select claimno, policyno, TREATMENTTYPE, CAUSEOFTREATMENT, SUBMISSIONTYPE, phase
from claim where claimno = 'C000020025';
-------
select claimid, caseid, claimno, occurrence, CREATEDBY, CREATEDDT from claim 
where createdby = 'asnpac0' and claimno like 'C00000%' and caseid is not null 
order by caseid desc;
-------
select CLAIMNO || '/' || occurrence as cn,policyno, planid, PRODUCTCODE, PRODUCTTYPE, SYSTEMELIGIBILITY
, ELIGIBILITY, ELIGIBLEAMT, APPROVEDAMT, paymentstatus, CREATEDDT, PAYMENTDATE, SETTLEMENTDATE
from claimpayment 
-------
select claimno, occurrence, policyno, cycledate, TRANSACTIONAMT,
transactiondt, createddt, lastmodifieddt 
from cwsworking where claimno = 'C000138468' and occurrence = 5;

select * from mclworking where claimno = 'C7512281';-- and occurrence = 4;

update claimpolicy 
set PABONUSDEDUCTAMT = 1000 
where claimno = 'C000003130' and policyno = 'P201302743';
select claimpaymentid, claimno,OCCURRENCE, policyno, planid, SYSTEMELIGIBILITY,
ELIGIBILITY,ELIGIBLEAMT, APPROVEDAMT, ADJUSTEDAMT,PAYMENTTRANSFERDT , SETTLEMENTDATE 
from claimpayment where CLAIMNO = 'C000013805';
select claimno, policyno, PABONUSAMT, PABONUSDEDUCTAMT 
from claimpolicy where claimno = 'C000003042'; --and occurrence = 8;




select * from plan where plancode in ('P92016','P92017','P92216');

update claimpolicy 
set PABONUSDEDUCTAMT = 10000,  PABONUSAMT = 10000
where claimno = 'C000003134' and policyno = 'P328556524';

update claimpayment
set ELIGIBLEAMT = 60000, approvedamt = 60000
where claimpaymentid = 279137;


update claimpayment
set ELIGIBLEAMT = 0, approvedamt = 0
where claimpaymentid = 0;
--------------------------
P703618249
T076580826

T091972985
C000003016/1
PLA
62845957

UAT
No.:C000004879/1

caseid 
3024
3025
3026
C000003027
3028



T106435016




P703618249
T091972985

select ACCOUNTPOSTSETUPID, ACCOUNTINGTYPE, ACCOUNTINGDESC, ACCOUNTINGACTIONCODE, ACCOUNTINGCATEGORY, INITPHASE, POSTSTEP, figure 
from ACCOUNTPOSTSETUP order by figure;

-----------------------------------------------
select caseid, claimid, claimno, occurrence,policyno,claimstatus, TREATMENTTYPE,
 CLAIMSTATUSDT, SUBMISSIONTYPE
from claim where claimno = 'C000026179';

select claimpaymentid, claimno,OCCURRENCE,paymentstatus, SETTLEMENTDATE,
policyno, planid, PLANCOVERAGENO, SYSTEMELIGIBILITY, ELIGIBILITY,ELIGIBLEAMT, APPROVEDAMT, ADJUSTEDAMT 
from claimpayment where CLAIMNO = 'C000015410';


select claimpaymentid,
planid , (select planname from plan where planid = cp.planid) as planname,
PRODUCTCODE, PRODUCTTYPE, ELIGIBILITY, ELIGIBLEAMT, PLANCODE from claimpayment  cp where claimno = 'C900000206';

select CLAIMPAYMENTID, claimno|| '/' || occurrence, policyno, planid,  PRESENTEDAMT, ELIGIBLEAMT, PAYMENTSTATUS
from claimpayment where claimno in('C000017460','C000017461'); --and occurrence = 2;

select CLAIMPAYMENTDETAILID, claimno|| '/' || occurrence, policyno, planid, plancoverageno, BENEFITCODE, PRESENTEDAMT, ELIGIBLEAMT, PAYMENTSTATUS
from claimpaymentdetail where claimno in('C000017460','C000017461'); --and occurrence = 2;

select distinct a.benefitItemCode,a.hsBenefitInd from BenefitItem a,PlanBenefit b 
where a.benefitItemCode=b.benefitItemCode and b.planId=189; --and a.hsBenefitInd='N';

select * from BenefitItem; --where planid = 174;
select * from PlanBenefit where planid = 189;

select claimid, claimno, occurrence, ACCIDENTDT, SYMPTOMDATE, DISABILITYSTARTDT, DISABILITYENDDT,
 HOSPITALIZATIONDATE, CONSULTATIONDT 
from claim where claimno = 'C000003306';

select claimpaymentid, claimno,OCCURRENCE,paymentstatus,
policyno, planid, SYSTEMELIGIBILITY, ELIGIBILITY,ELIGIBLEAMT, APPROVEDAMT, ADJUSTEDAMT 
from claimpayment where CLAIMNO = 'C000003306';

select claimpaymentid, claimno,OCCURRENCE, policyno, PAYMENTSTATUS,planid,producttype,
SYSTEMELIGIBILITY, ELIGIBILITY,ELIGIBLEAMT,PRESENTEDAMT, APPROVEDAMT, ADJUSTEDAMT,SETTLEMENTDATE 
from claimpayment where CLAIMNO = 'C000012748' and occurrence = 1;

select * from plan where planshortname like 'HSJ%';
select planid, plancode, subplancode, PLANSHORTNAME, planname, PRODUCTCODE, planthaidesc, businessline, CREATEDDT, LASTMODIFIEDBY, DEFAULTPLANID from plan where planshortname like 'HSJ%';

select claimid, claimno, occurrence, ACCIDENTDT, SYMPTOMDATE, DISABILITYSTARTDT, DISABILITYENDDT, HOSPITALIZATIONDATE, CONSULTATIONDT 
from claim where claimno = 'C000003054';
---------select for benefit table -------
select cp.claimpaymentid, cp.claimno, cp.OCCURRENCE, cp.paymentstatus, cp.SETTLEMENTDATE,cp.businessline,
cp.policyno, cp.PRODUCTCODE, cp.producttype, cp.planid, p.planshortname, cp.PLANCOVERAGENO, 
cp.SYSTEMELIGIBILITY, cp.ELIGIBILITY,cp.ELIGIBLEAMT, cp.APPROVEDAMT, cp.ADJUSTEDAMT 
from claimpayment cp, plan p 
where cp.CLAIMNO = 'C000460744' and cp.planid = p.planid;

select cp.claimpaymentid, cp.claimno, cp.OCCURRENCE, cp.paymentstatus, cp.SETTLEMENTDATE,--cp.businessline,
cp.policyno, cp.PRODUCTCODE, cp.producttype, cp.planid,p.planname, p.planshortname, cp.PLANCOVERAGENO, 
cp.SYSTEMELIGIBILITY, cp.ELIGIBILITY,cp.ELIGIBLEAMT, cp.APPROVEDAMT, cp.ADJUSTEDAMT 
from claimpayment cp, plan p 
where cp.CLAIMNO = 'C900000101' and occurrence = 1 and cp.planid = p.planid;

update claimpolicy 
set PABONUSDEDUCTAMT = 1000 
where claimno = 'C000003038' and policyno = 'P703618249';

update claimpolicy 
set PABONUSDEDUCTAMT = 1000 , PABONUSAMT = 1000
where claimno = 'C000003128' and policyno = 'P328556524';


select claimpaymentid, claimno,OCCURRENCE, policyno, planid, SYSTEMELIGIBILITY,
 ELIGIBILITY,ELIGIBLEAMT, APPROVEDAMT, ADJUSTEDAMT 
from claimpayment where CLAIMNO = 'C000003034'; --and occurrence = 8;
select claimno, policyno, PABONUSAMT, PABONUSDEDUCTAMT 
from claimpolicy where claimno = 'C000003034'; --and occurrence = 8;

select * from plan where plancode in ('P92016','P92017','P92216');


update claimpayment
set eligibleamt = 45000, adjustedamt = 0
where claimpaymentid = 279069;


update claimpayment
set eligibleamt = 45000, approvedamt = 45000, adjustedamt = 0
where claimpaymentid = 279065;

update claimpayment
set eligibleamt = 45000, approvedamt = 45000, adjustedamt = 0
where claimpaymentid = 279069;

select claimno,producttype,approvedamt as amount 
from claimpayment where claimno = 'C000128050' and occurrence = 1; --

select claimno,producttype,sum(approvedamt) as amount 
from claimpayment where claimno = 'C000128050' and occurrence = 1 GROUP BY claimno,producttype;


select cb.claimbenefititemid,cb.claimno,cb.servicecatid,NVL(cb.presentedamt,0), NVL(cb.presenteddiscountamt,0),
 NVL(cb.presentedamt,0) - NVL(cb.presenteddiscountamt,0) as presentedamt ,s.serviceitemdesc
from claimbenefititem cb join serviceitem s on cb.servicecatid = s.servicecatid 
where cb.claimno = 'C000128050' and cb.occurrence = 1;


select claimpaymentid, claimno,OCCURRENCE, policyno, planid, 
SYSTEMELIGIBILITY, ELIGIBILITY,ELIGIBLEAMT, APPROVEDAMT, ADJUSTEDAMT 
from claimpayment where CLAIMNO = 'C000004880' and occurrence = 1;
select claimno, policyno, PABONUSAMT, PABONUSDEDUCTAMT 
from claimpolicy where claimno = 'C000004880' and occurrence = 1;

select * from plan where plancode in ('P92016','P92017','P92216');


--------- claim policy detail-----
select claimno, occurrence, policyno, POLICYISSUEDT from claimpolicy where claimno = 'C6430571' and policyno = 'T134805304';-- and occurrence = 50;-- and occurrence = 22; --  like 'C0000%'; -- where claimno = 'C5445103'; --where claimno = 'C6430571' and occurrence = 50;--where policyno = 'T134805304';
select claimno, OCCURRENCE, policyno, planid, PLANCOVERAGENO, PLANISSUEDT, planexpirydt, createddt, lastmodifieddt from CLAIMPOLICYPLAN where claimno = 'C6430571' and occurrence = 50 ;

update claimpolicyplan 
set planissuedt = current_timestamp
WHERE claimno = 'C000003140' and policyno = 'T198897235' and PLANCOVERAGENO = '05';

select myCycleDate.currentCycleDt from CycleDate myCycleDate where trim(upper(myCycleDate.applicationName)) =  'BCLAIMS';

--------- edit claim --
update claim 
set dob 
update claim 
set claimstatus = '65', claimstatusdt = to_timestamp('31-JAN-17 12.00.00.000000000 AM','DD-MON-RR HH.MI.SSXFF AM')
where claimno = 'C000003156';

update claim 

to_timestamp('28-NOV-17 09.44.43.108000000 AM','DD-MON-RR HH.MI.SSXFF AM')

select myCycleDate.currentCycleDt from CycleDate myCycleDate where trim(upper(myCycleDate.applicationName)) =  'BCLAIMS';

update claim 
set claimstatus = '91', claimstatusdt = current_timestamp
where claimno = 'C000004450' and caseid = 1054385 ;

update claim 
set claimstatus = '91', claimstatusdt = current_timestamp
where claimno = 'C000005259'; 

select claimno, occurrence, claimstatus, claimstatusdt from claim where claimstatus in('91','95') and claimno like 'C00000%' order by claimno desc;

select claimid, claimno,TOOLKIT.decrypt(firstname,'1234567812345678'), TOOLKIT.decrypt(lastname,'1234567812345678') from claim;

select count(myClaimPayment) from ClaimPayment myClaimPayment 
where myClaimPayment.companyId = '051' and myClaimPayment.claimNo= 'C000006032' 
and myClaimPayment.occurrence= 1 and myClaimPayment.paymentStatus <  '70'
and eligibility not in ('91');
------ update by use replace function ----------
update systemconfig
set PARAMVALUE = REPLACE(PARAMVALUE,'thadcslwmi01','localhost')
where PARAMKEY like 'cmic.ods.endpoint%';

update systemconfig
set PARAMVALUE = REPLACE(PARAMVALUE,'localhost','thadcslwmi01')
where PARAMKEY like 'cmic.ods.endpoint%';
---ADM TABLE--
select TABLE_NAME, TABLE_VALUE, TABLE_VALUE_DESC 
from adam_ods.ADAM_ING_TEDIT
where TABLE_NAME = 'STB2';-- and TABLE_VALUE = 'RQ'; 


select claimno,claimid, occurrence, claimstatus,PROCESSSTATUS, billingstatus, BILLINGDECLINEREASON
from claim where claimno = 'C000010177' and occurrence = 1;
select claimno,claimid, occurrence, claimstatus,PROCESSSTATUS, billingstatus, BILLINGDECLINEREASON
from claim where claimno = 'C000010803' and occurrence = 1;
select * from CLAIMSUPPLEMENT where claimno = 'C000010177' and occurrence = 1;
select * from CLAIMSUPPLEMENT where claimno = 'C000010803' and occurrence = 1;

select * from ICD10CODE where icd10code like '%J01%' or ICDSUBCODE like '%J01%';


select caseid, claimno , claimstatus, claimstatusdt from claim where claimno = 'C900000209';
select claimpaymentid, claimno,OCCURRENCE,paymentstatus, SETTLEMENTDATE,
policyno, planid, PLANCOVERAGENO, productcode, SYSTEMELIGIBILITY, ELIGIBILITY,ELIGIBLEAMT, APPROVEDAMT, ADJUSTEDAMT 
from claimpayment where claimno = 'C900000209';

----------------fsuworking----
select claimno, fsuworkingid, payeetype, transactionamt, postingdesc, createddt, producttype, status
 from fsuworking where claimno = 'C000013980';
select fsuworkingid, policyno, payeetype, accountcode, COVERAGEPLANCODE, 
PRODUCTTYPE, postingdesc,TRANSACTIONAMT, CREATEDDT, status, CLAIMPAYMENTID 
from FSUWORKING where claimno = 'C000014062' order by fsuworkingid;
--------------------
select * from claimpolicy WHERE ROWNUM <= 10 order by claimpolicyid desc;

Insert into systemconfig 
(PARAMKEY,PARAMVALUE,CREATEDBY,CREATEDDT,LASTMODIFIEDBY,LASTMODIFIEDDT) 
values ('cmic.na.allow','CMIC_LMT_HS_AMT_GP:1000000001','wMUser',current_timestamp,'wMUser',current_timestamp);

delete from systemconfig 
where paramkey = 'cmic.calculated.decision';

Insert into systemconfig 
(PARAMKEY,PARAMVALUE,CREATEDBY,CREATEDDT,LASTMODIFIEDBY,LASTMODIFIEDDT) 
values ('cmic.calculated.decision','93','wMUser',current_timestamp,'wMUser',current_timestamp);
select * from systemconfig where PARAMKEY = 'cmic.calculated.decision';

Insert into systemconfig 
(PARAMKEY,PARAMVALUE,CREATEDBY,CREATEDDT,LASTMODIFIEDBY,LASTMODIFIEDDT) 
values ('cmic.dev.aiInd','Y','wMUser',current_timestamp,'wMUser',current_timestamp);
select * from systemconfig where PARAMKEY = 'cmic.dev.aiInd';

Insert into systemconfig 
(PARAMKEY,PARAMVALUE,CREATEDBY,CREATEDDT,LASTMODIFIEDBY,LASTMODIFIEDDT) 
values ('cmic.dev.stpInd','Y','wMUser',current_timestamp,'wMUser',current_timestamp);
select * from systemconfig where PARAMKEY = 'cmic.dev.stpInd';


Insert into systemconfig 
(PARAMKEY,PARAMVALUE,CREATEDBY,CREATEDDT,LASTMODIFIEDBY,LASTMODIFIEDDT) 
values ('cmic.dev.aiStatus','10','wMUser',current_timestamp,'wMUser',current_timestamp);
select * from systemconfig where PARAMKEY = 'cmic.dev.aiStatus';

Insert into systemconfig 
(PARAMKEY,PARAMVALUE,CREATEDBY,CREATEDDT,LASTMODIFIEDBY,LASTMODIFIEDDT) 
values ('cmic.dev.callAiService','Y','wMUser',current_timestamp,'wMUser',current_timestamp);
select * from systemconfig where PARAMKEY = 'cmic.dev.callAiService';


update claim
set 
update systemconfig
set PARAMVALUE = 'Y'
where PARAMKEY = 'cmic.dev.aiInd';

update systemconfig
set PARAMVALUE = '93;not approve'
where PARAMKEY = 'cmic.dev.aiStatus';

update systemconfig
set PARAMVALUE = 'N'
where PARAMKEY = 'cmic.dev.stpInd';
select * from systemconfig where PARAMKEY in ('cmic.dev.stpInd','cmic.dev.aiInd','cmic.dev.aiStatus');
-------------------------
select claimpolicyid, claimno, occurrence, policyno, CERTNO,PLANBASICCODE, businessline, PRODUCTCODE
from claimpolicy  where CLAIMNO = 'C004217127' and OCCURRENCE = 3;
select CLAIMPOLICYPLANID, claimno, occurrence, POLICYNO, planid, PRODUCTCODE, PLANCOVERAGENO
from CLAIMPOLICYPLAN where CLAIMNO = 'C004217127' and OCCURRENCE = 3;
select CLAIMPOLICYCOVERAGEID, claimno, OCCURRENCE, policyno, planid, SHAREIND, 
PRODUCTCODE, benefitcode, PLANCOVERAGENO, sumcategory, SUMSEQUENCENO
from CLAIMPOLICYCOVERAGE where CLAIMNO = 'C004217127' and OCCURRENCE = 3;

select claimpolicyid, claimno, occurrence, policyno, CERTNO,PLANBASICCODE, businessline, PRODUCTCODE, createddt
from claimpolicy  where policyno = '02995' and CERTNO = '2011080380' order by createdby desc;

-------------
select * from claim where claimno = 'C004393301';
select * from claimpolicy where claimno = 'C004393301';
select distinct(claimno) from claimpolicy 
where policyno = '0000011144' and certno = '01695010' and MEMBERID = '2844948103' 
and trunc(CREATEDDT) = to_date('05/15/2019', 'MM/dd/yyyy') ;
--------------
select claimno, occurrence,POLICYNO, ENABLEIND, SHAREIND, ACCUMULATORNO, PRODUCTCODE, BENEFITCODE, SUMCATEGORY , SUMTIMEFRAME, CREATEDDT
from CLAIMPOLICYCOVERAGE where REGEXP_LIKE(claimno, '^[[:digit:]]+$') and sumtimeframe in ('B','P')
order by CREATEDDT desc, claimno, occurrence, BENEFITCODE;


update claim
set EXPECTEDADMISSIONDATE = to_date('11/25/2020', 'MM/DD/YYYY')
where claimno = 'C000032721';
--------
C007880865/
select * from TRANSACTIONLOG where  claimno = 'C004971577' and OCCURRENCE = 2 and servicename = 'Calculation' order by CREATEDDT desc ;
-------
select * from TRANSACTIONLOG where TRANSACTIONLOGID > 1544170000 and LOGLEVEL = 'ERROR';
----
select MAX(TRANSACTIONLOGID) from TRANSACTIONLOG ;
select * from TRANSACTIONLOG where TRANSACTIONLOGID > 2695041572 
and  LOGLEVEL = 'ERROR';
------------
