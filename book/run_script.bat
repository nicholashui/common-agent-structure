@echo off
setlocal
cd /d "%~dp0"

rem Usage:
rem   run_script.bat
rem   run_script.bat xai
rem   run_script.bat openai
rem   run_script.bat anthropic
rem   run_script.bat poe
rem   run_script.bat deepseek
rem   run_script.bat grok grok-4.6
rem First arg = LLM provider (default xai). Second arg = optional model override.

set "LLM=xai"
if not "%~1"=="" set "LLM=%~1"
set "MODEL_ARGS="
if not "%~2"=="" set "MODEL_ARGS=--model %~2"

echo LLM=%LLM% %MODEL_ARGS%
echo Using book\.env

python translate_book.py -i CASOPS_THE_COMPLETE_BOOK.md -o CASOPS_THE_COMPLETE_BOOK.hk.md --llm %LLM% %MODEL_ARGS%
if errorlevel 1 exit /b 1

python gen_script.py -i CASOPS_THE_COMPLETE_BOOK.md -o CASOPS_THE_COMPLETE_BOOK.script.hk.txt -p ytscript.txt --llm %LLM% %MODEL_ARGS%
if errorlevel 1 exit /b 1

python gen_tts.py -i CASOPS_THE_COMPLETE_BOOK.script.hk.txt -o CASOPS_THE_COMPLETE_BOOK.hk.mp3 --audio-dir CASOPS_THE_COMPLETE_BOOK_audio_hk
if errorlevel 1 exit /b 1

echo Done.
endlocal
