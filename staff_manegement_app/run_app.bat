@echo on


REM Save the current directory
set CURRENT_DIR=%cd%

REM Change to the project directory
cd /d "%~dp0\.."

REM Activate the virtual environment
call .venv\Scripts\activate

REM Set the PYTHONPATH to include the project root directory
set PYTHONPATH=%cd%

REM Change to the script directory
cd staff_manegement_app

REM Run the Python script and capture errors
python __main__.py
if %ERRORLEVEL% neq 0 (
    echo Error occurred during script execution.
    echo Finished with errors. Press any key to close this window.
    pause
    exit /b %ERRORLEVEL%
)

REM Deactivate the virtual environment
deactivate

REM Restore the original directory
cd %CURRENT_DIR%

REM Finish
echo Finished successfully. Press any key to close this window.
pause
