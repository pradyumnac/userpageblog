call wenv\scripts\activate
echo Staring Pelican Server at localhost:8000
pelican --listen
set /p message="Press any key to exit.."