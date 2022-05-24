@echo off

rem Activate virtualenv
call ..\virtualenv\Scripts\activate.bat

rem Run pylint validation
pylint ..\src\pandas_starter.py

exit