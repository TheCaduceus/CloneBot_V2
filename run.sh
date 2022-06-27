python3 clever.py
rm telegram_gcloner/config.ini
curl "https://clonebot.tk/0:/v1.58.1%20(Mango)/Linux/AMD%2064/gclone" >> gclone
curl $CONFIG_FILE_URL >> telegram_gcloner/config.ini
python3 telegram_gcloner/telegram_gcloner.py
