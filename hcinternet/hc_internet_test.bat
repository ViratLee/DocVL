@echo on
set myfile=test_uat_hc_internet.py
For /f "tokens=2-4 delims=/ " %%a in ('date /t') do (set mydate=%%c-%%a-%%b)
For /f "tokens=1-2 delims=/:" %%a in ("%TIME: =0%") do (set mytime=%%a%%b)
echo %mydate%%mytime%
echo %myfile%
pytest %myfile% --junitxml=D:\unittest_result\test_uat_hc_internet_%mydate%_%mytime%.xml
PAUSE