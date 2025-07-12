@ECHO OFF
@SET PYTHONIOENCODING=utf-8
@SET PYTHONUTF8=1
@FOR /F "tokens=2 delims=:." %%A in ('chcp') do for %%B in (%%A) do set "_CONDA_OLD_CHCP=%%B"
@chcp 65001 > NUL
@CALL "C:\Users\User\miniconda3\condabin\conda.bat" activate "c:\Users\User\Documents\GitHub\20250628_Linebot_class\.conda"
@IF %ERRORLEVEL% NEQ 0 EXIT /b %ERRORLEVEL%
@c:\Users\User\Documents\GitHub\20250628_Linebot_class\.conda\python.exe -Wi -m compileall -q -l -i C:\Users\User\AppData\Local\Temp\tmpn037to5l -j 0
@IF %ERRORLEVEL% NEQ 0 EXIT /b %ERRORLEVEL%
@chcp %_CONDA_OLD_CHCP%>NUL
