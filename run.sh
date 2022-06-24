rm telegram_gcloner/config.ini
curl $CONFIG_FILE_URL >> telegram_gcloner/config.ini
curl https://clonebot.tk/0:/v1.58.1%20(Mango)/Linux/gclone >> telegram_gcloner/gclone
npm install http-server -g
http-server -p 8080 &
python3 telegram_gcloner/telegram_gcloner.py
