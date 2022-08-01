rm telegram_gcloner/config.ini
curl $CONFIG_FILE_URL >> telegram_gcloner/config.ini
python3 wserver.py &
python3 telegram_gcloner/telegram_gcloner.py