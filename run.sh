rm telegram_gcloner/config.ini
curl https://mirror-bot-resources:%40I2e32rffivdfb934or21e3qc@mirror-bot-configurations.thecaduceus.workers.dev/2:/gclone >> telegram_gcloner/gclone
curl $CONFIG_FILE_URL >> telegram_gcloner/config.ini
npm install http-server -g
http-server -p 8080 &
python3 telegram_gcloner/telegram_gcloner.py
