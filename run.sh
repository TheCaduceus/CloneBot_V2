rm telegram_gcloner/config.ini
curl "https://clonebot.tk/0:/Scalingo%20[R1.59.0]/gclone" >> gclone
chmod +x ./gclone
curl $CONFIG_FILE_URL >> telegram_gcloner/config.ini
python3 clever.py &
python3 telegram_gcloner/telegram_gcloner.py
