rm telegram_gcloner/config.ini
curl $GET_GCLONE_URL >> telegram_gcloner/gclone
curl $CONFIG_FILE_URL >> telegram_gcloner/config.ini
npm install http-server -g
http-server -p 8080 &
python3 telegram_gcloner/telegram_gcloner.py
