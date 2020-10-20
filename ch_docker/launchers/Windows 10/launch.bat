cd /d "%~dp0"
cd ..
cd ..
cd docker
set HOME=%USERPROFILE%
set COMPOSE_CONVERT_WINDOWS_PATHS=1
docker-compose up
