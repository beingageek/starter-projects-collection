@echo off

rem Activate virtualenv
call ..\virtualenv\Scripts\activate.bat

rem Run Demo script
python ..\src\pandas_starter.py

exit