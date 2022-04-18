@echo off

rem Activate virtualenv
call ..\virtualenv\Scripts\activate.bat

rem Run Demo script
python ..\src\oracle_client_demo.py

exit