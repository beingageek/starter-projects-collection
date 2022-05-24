@echo off

rem Prepare Python virtual env
python -m venv ..\virtualenv

rem Activate virtualenv
call ..\virtualenv\Scripts\activate.bat

rem Install Python packages
call pip install -r ..\requirements.txt

exit