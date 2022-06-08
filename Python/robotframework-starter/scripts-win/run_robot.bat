@echo off

echo Activating virtualenv...
call ..\virtualenv\Scripts\activate.bat

echo Running robotframework-browser...
call python -m robot -o output/output.xml -r output/report.html -l output/log ..\test_robot.robot

start output/report.html
