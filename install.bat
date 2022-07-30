set file_name=automate-files.py
set script_directory=%USERPROFILE%\bin
set startup_direcory="%USERPROFILE%\Start Menu\Programs\Startup"
set new_file_name=%file_name%w

md %script_directory%
copy "%cd%\%file_name%" "%script_directory%\%new_file_name%"

copy "%cd%\startup_scripts\startup.vbs" %startup_direcory%"\run_file_automation.vbs"

cscript %startup_direcory%"\run_file_automation.vbs"