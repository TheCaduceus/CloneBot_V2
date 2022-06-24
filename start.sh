CONFIG_FILE_URL = $CONFIG_FILE_URL
rm telegram_gcloner/config.ini
curl $CONFIG_FILE_URL >> telegram_gcloner/config.ini
npm install http-server -g
http-server -p $PORT &
python3 telegram_gcloner/telegram_gcloner.py
