@echo off

echo Preparing Python virtual env...
python -m venv ..\virtualenv

echo Activating virtualenv...
call ..\virtualenv\Scripts\activate.bat

echo Installing Python packages...
call pip install -r ..\requirements.txt

echo Initializing robotframework-browser...
call rfbrowser init

echo Exiting.
deactivate
exit