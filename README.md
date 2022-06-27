
[![Deploy on Scalingo](https://cdn.scalingo.com/deploy/button.svg)](https://my.scalingo.com/deploy?source=https://github.com/tiararosebiezetta/SearchX#main)
</p>



<h1 align ="center"><b>CloneBot V2 🔥</b></h1>
<!---Introduction--->
<p><b>CloneBot V2 is inspired from MsGsuite's CloneBot, which got out-dated and having too many errors in it. We both created it to keep the legacy of CloneBot alive! The bot who helped thousands for cloning their data.❤️</b></p>
<p><b>1. The Powerful Telegram Bot based on Gclone to clone Google Drive's Shared Drive data easily.⚡</b></p>
<p><b>2. CloneBot V2 usage Service Accounts to easily clone TBs of data without hitting 750GB Upload/Clone limit of Google Drive.♻️</b></p>
<p><b>3. It is most lightweight and performs only server-sided cloning to have very less load on system and don't use your own bandwidth.🗃️</b></p>
<p><b>4. Just provide the sharing link of a particular Shared Drive/folder or file and set multiple destination folders to clone data.🔗</b></p>
<!---Index--->
<h2><b>📑 INDEX</b></h2>
<p><b>Easily navigate through out the guide and learn about Powerful CloneBot V2 and terms related to it.</b></p>
<p><b><a href="https://github.com/TheCaduceus/CloneBot_V2#clonebot-v2-">🔥 CloneBot V2</a></b></p>
<p><b><a href="https://github.com/TheCaduceus/CloneBot_V2#-whats-new">🆕 What's New!</a></b></p>
<p><b><a href="https://github.com/TheCaduceus/CloneBot_V2#-notice">⛔ NOTICE</a></b></p>
<p><b><a href="https://github.com/TheCaduceus/CloneBot_V2#%EF%B8%8F-how-to-use">⚙️ How to use?</a></b></p>
<p><b><a href="https://github.com/TheCaduceus/CloneBot_V2/blob/main/Commands.md">->🔩Commands for BotFather</a></b></p>
<p><b><a href="https://github.com/TheCaduceus/CloneBot_V2#%EF%B8%8Fdeployment">🕹️Deployment</a></b></p>
<p><b><a href="https://github.com/TheCaduceus/CloneBot_V2#getting-config_file_url">->📄Getting CONFIG_FILE_URL</a></b></p>
<p><b><a href="https://github.com/TheCaduceus/CloneBot_V2#deploy-on-heroku">->⚡Deploy on Heroku</a></b></p>
<p><b><a href="https://github.com/TheCaduceus/CloneBot_V2#deploy-using-github-actions">->🧿Deploy using GitHub Actions</a></b></p>
<p><b><a href="https://github.com/TheCaduceus/CloneBot_V2#deploy-on-okteto">->🪬Deploy on Okteto</a></b></p>
<p><b><a href="https://github.com/TheCaduceus/CloneBot_V2#%EF%B8%8F-deploy-on-vps-or-pc">->🖥️ Deploy on VPS or PC</a></b></p>
<p><b><a href="https://github.com/TheCaduceus/CloneBot_V2#deploy-on-termux">->📱Deploy on Termux</a></b></p>
<p><b><a href="https://github.com/TheCaduceus/CloneBot_V2#deploy-on-scalingo">->🎲Deploy on Scalingo</a></b></p>
<p><b><a href="https://github.com/TheCaduceus/CloneBot_V2#-making-service-accounts">🪪 Making Service Accounts</a></b></p>
<p><b><a href="https://github.com/TheCaduceus/CloneBot_V2#%EF%B8%8F-create-service-accounts">->🛠️ Create Service Accounts</a></b></p>
<p><b><a href="https://github.com/TheCaduceus/CloneBot_V2#-adding-in-google-group">->🌐 Adding in Google Group</a></b></p>
<p><b><a href="https://github.com/TheCaduceus/CloneBot_V2#contact-us">⛑Contact Us!</a></b></p>
<p><b><a href="https://github.com/TheCaduceus/CloneBot_V2#%EF%B8%8Fcredits--thanks">❤️Credits & Thanks</a></b></p>
<!---ChangeLog--->
<h2><b>🆕 What's New!</b></h2>
<p><b>1.Gclone upgraded to v1.58.1 (latest)!😉</b></p>
<p><b>2.Deployment on Okteto & Scalingo Added!🤩</b></p>
<p><b>3.Port Error fixed for Okteto deployments!😄</b></p>
<p><b>4.Bot can be deployed as both Web or Worker on Heroku.🙃</b></p>
<p><b>5.Mitigated Time Zone Error while deployment.🤗</b></p>
<p><b>6.Addressed GitHub Workflow Error!😙</b></p>
<p><b>7.Docker Image changed!😌</b></p>
<p><b><a href="www.github.com/TheCaduceus/CloneBot_V2/releases">Show Full Update history</a></b></p>
<!---NOTICE--->
<h2><b>⛔ NOTICE</b></h2>
<p><b>1.You may need account for Heroku/Okteto/Scalingo while deploying CloneBot V2 on respected platforms.</b></p>
<p><b>2.Service Accounts are mandatory to use CloneBot, because it uses Service Accounts to prevent hitting 750GB Upload/Clone limit of Google Drive while cloning large amount of data.</b></p>
<p><b>3.VPS or your local machine (PC or Laptop or Mobile) should have Python 3 and Git installed in order to run CloneBot V2.</b></p>
<p><b>4.CloneBot V2 don't use your bandwidth or Internet connection while cloning data but it can if hosted on your local machine or VPS for calling required Telegram APIs to update the progress or to generate required response.</b></p>
<p><b>5.This Project comes with GNU License, please consider reading it before using this.</b></p>
<!---Deployment--->
<h2><b>⚙️ How to use?</b></h2>
<p><b>CloneBot V2 is very straight forward and easy to use bot. If you deployed your CloneBot V2 then consider adding commands in it through <a href="https://t.me/BotFather">@BotFather</a> to make it easy for other users to know bot commands, here is the <a href="https://github.com/TheCaduceus/CloneBot_V2/blob/main/Commands.md" alt="Command-list">commands list</a> to be set in <a href="https://t.me/BotFather">@BotFather</a>:</b></p>
<h4><b>1.First convert accounts folder of your Service Accounts into accounts.zip then send it to bot and write "/sa" in caption or send "/sa" as reply to accounts.zip file. Don't have Service Accounts? <a href="https://github.com/TheCaduceus/CloneBot_V2#-making-service-accounts">Learn here</a> how to create</b></h4>
<h4><b>2.Now Send /folders to your CloneBot V2 and then bot will show Shared Drives name in which you added your Service Accounts's Google Group, select Shared Drive or directory available in it as destination. Not added Service Accounts in Google Group? <a href="https://github.com/TheCaduceus/CloneBot_V2#%EF%B8%8F-create-service-accounts">Learn here</a> how to do.</b></h4>
<h4><b>3.Your CloneBot V2 is now ready to be used! just send any Google Drive sharing link and select to Destination folder to selected before to clone data in it.</b></h4>
<h4><b>4.Additionally, "/ban" and "/unban" command is to unauthorize or authorize user again and "/id" command is to get your Telegram User ID.</b></h4>
<p><b>⛔NOTE: Each allowed user have to upload their own accounts.zip to use CloneBot_V2.</b></p>
<h2><b>🕹️Deployment</b></h2>
<p><b>Deployment of CloneBot_V2 is as simple as its usage! Their are many methods listed below to deploy CloneBot easily, but before you deploy it, you need some values listed below and how to get it:</b></p>
<p><b>
	path_to_gclone - Path to gclone file, by default it is "gclone" or change it if you using different one.<br>
	BOT_TOKEN / telegram_token - Get your bot's Telegram API Token from <a href="https://t.me/BotFather">BotFather</a>.<br>
	ALLOW_USERS / user_ids - Telegram User IDs of users who can use your CloneBot_V2. Separate them using ',' and first User ID is Admin.<br>
	ALLOW_GROUPS / group_ids - Telegram Group IDs of Groups in which CloneBot can be used otherwise keep it "-1". Separate them using ','<br>
	gclone_para_override - Keep it blank if you don't know what it is.
</b></p>
<h3><b>📄Getting CONFIG_FILE_URL</b></h3>
<p><b>CONFIG_FILE_URL is URL to config.ini file which contains values of variables discussed above, lets see how to get your CONFIG_FILE_URL easily:</b></p>
<h4><b>1.First open <a href="https://github.com/TheCaduceus/CloneBot_V2/blob/main/sample-config.ini"> sample-config.ini file</a> then copy its code.</b></h4>
<img src="Img/32.png" alt="32">
<h4><b>2.Now open <a href="https://gist.github.com" alt="GitHub Gist">GitHub Gist</a> and create a new gist and paste the code you just copied and name it as "config.ini" and now fill below values carefully:</b></h4>
<p><b>
	path_to_gclone - Keep it as "gclone".<br>
    telegram_token - Enter Telegram Bot Token, get it from <a href="https://t.me/BotFather">@BotFather</a>.<br>
    user_ids - Enter User IDs, which you want to allow your CloneBot V2. Separate IDs by ',' and first ID is Admin.<br>
    group_ids - Enter Group IDs, in which you want to allow your CloneBot V2 to be used otherwise keep it "-1". Separate IDs by ','<br>
    gclone_para_override - Keep it blank if you don't know what it is.
</b></p>
<img src="Img/33.png" alt="33">
<h4><b>3.Then press "Create Secret Gist" then click "Raw", it will open a New Tab in your Browser. Just copy the URL of that New Tab</b></h4>
<img src="Img/34.png" alt="34">
<img src="Img/35.png" alt="35">
<h4><b>4.Once you copied the URL! then remove Commit_ID from the URL:</b></h4>
<p><b>Before:<br>
https://gist.githubusercontent.com/UserName/0ee24eXXXXXXXXXXXXXXX6b/raw/{Commit_ID}/config.ini<br>
After:<br>
https://gist.githubusercontent.com/UserName/0ee24eXXXXXXXXXXXXXXX6b/raw/config.ini
</b></p>
<!---Heroku--->
<h3><b>⚡Deploy on Heroku</b></h3>
<p><b>Heroku is very famous PaaS (Platform as a Service) platform and it provides very simple user environment as well as you can deploy CloneBot V2 very quickly on Heroku to run it continuously for 24 Hours.</b></p>
<h4><b>1.Press below CloneBot V2 deploy button for Heroku:</b></h4>
<a href="https://heroku.com/deploy?template=https://github.com/TheCaduceus/CloneBot_V2"><img src="Img/Deploy-Button-Heroku.png" alt="Deploy on Heroku"></a>
<h4><b>2.Enter Below Values:</b></h4>
<p><b>
	App Name - Give a unique name to your Bot.<br>
	CONFIG_FILE_URL - Enter CONFIG_FILE_URL which you made <a href="">here</a>.
</b></p>
<img src="Img/36.png" alt="36">
<h4><b>3.Click "Deploy" button and once it got deployed, click "Manage App" then go to "Resource Tab" and enable the dyno as shown in the image.</b></h4>
<img src="Img/37.png" alt="37">
<h4><b>3.Enjoy! Your CloneBot V2 is now deployed and you can freely use it.</b></h4>
<p><b>⛔NOTE: Heroku provides 550 running hours (dyno hours) per month and it restarts deployed app each 24 Hours.</b></p>
<!---GitHub-Actions-Heroku--->
<h2><b>🧿Deploy using GitHub Actions</b></h2>
<p><b>This methods is really amazing and simple!🥰 You can deploy your CloneBot V2 on Heroku using GitHub Actions itself by just providing your HEROKU API KEY,HEROKU EMAIL and HEROKU APPNAME.</b></p>
<h4><b>1.First fork this repository, now open the settings of your Forked Repository and click Secrets->Actions.</b></h4>
<img src="Img/44.png" alt="44">
<h4><b>2.Then click "New repository secret" and create 4 secrets as stated below:</b></h4>
<p><b>
	HEROKU_API_KEY - Enter your Heroku API Key as value.<br>
	HEROKU_EMAIL - Your Heroku Email ID.<br>
	HEROKU_APP_NAME - A unique app name in small letters only.<br>
	CONFIG_FILE_URL - CONFIG_FILE_URL you made above for Heroku deployment!
</b></p>
<h4><b>3.Go to Actions Tab then click "Deploy to Heroku" and "Run Workflow". Now it will be automatically got deployed on given Heroku Account!😉</b></h4>
<img src="Img/45.png" alt="45">
<p><b>⛔NOTE: Deploying as web? change deploy.yml (Docker Process Type) and add PORT as Repository secret, value can be "8080".</b></p>
<!---Okteto--->
<h2><b>🪬Deploy on Okteto</b></h2>
<p><b>Okteto is also very famous Kubernetes development platforms and used by many users and it is ideal for lightweight apps and it is perfect for CloneBot V2, Okteto don't have any running hours limit like Heroku but your CloneBot V2 will go to sleep if the ENDPOINT provided by Okteto for your CloneBot V2 untouched. Don't worry, I have solution too and some special arrangements.</b></p>
<h4><b>1.First Create your Okteto Account, You need one GitHub account as okteto supports only one Method to either Create or Login:<a href="https://cloud.okteto.com/#/login" alt="Login on Okteto"> Create/Login on Okteto</a></b></h4>
<img src="Img/38.png" alt="38">
<h4><b>2.Now fork this repository, and go to Okteto Dashboard then press "Launch Dev Environment".</b></h4>
<img src="Img/39.png" alt="39">
<h4><b>3.After it, select your forked repository and select branch "main" and add following values carefully:</b></h4>
<p><b>
	BOT_TOKEN - Enter Telegram Bot Token, get it from <a href="https://t.me/BotFather">@BotFather</a>.<br>
	ALLOW_USERS - Enter User IDs, which you want to allow your CloneBot V2. Separate IDs by ',' and first ID is Admin.<br>
	ALLOW_GROUPS - Enter Group IDs, in which you want to allow your CloneBot V2 to be used otherwise keep it "-1". Separate IDs by ','.
</b></p>
<img src="Img/40.png" alt="40">
<h4><b>4.Once done! press "Launch" and you successfully done it! Yes 😊</b></h4>
<h4><b>5.Okteto make your deployed app to sleep if provided ENDPOINT (Allotted URL) remain untouched for 24 Hours. So lets setup a simple cron-job to keep your app active.</b></h4>
<h4><b>6.First copy your app's ENDPOINT as shown in the image and go to <a href="https://cron-job.org/en" alt="Cron-Job">Cron-Job.org</a> and sign up!</b></h4>
<img src="Img/41.png" alt="41">
<img src="Img/42.png" alt="42">
<h4><b>7.Done? Nice! now click "CREATE CRONJOB" button and provide your copied ENDPOINT URL that you just copied and change execution schedule to every 5 minutes.Finally! click "CREATE" and you done it! 😌 Relax and use CloneBot V2 freely.</b></h4>
<img src="Img/43.png" alt="43">
<p><b>⛔NOTE: Don't forget to setup Cron-Job for Okteto otherwise your deployed bot will go into sleep and you have to active it from Okteto Dashboard, while Cron-Job doing it on your behalf.</b></p>
<!---Deploy-on-VPS/PC--->
<h2><b>🖥️ Deploy on VPS or PC</b></h2>
<p><b>Running CloneBot_V2 on your PC or VPS is very simple and takes very less efforts! It have very less load on your System and don't use your bandwidth or Internet connection for cloning Google Drive data but only for calling Telegram APIs to update the progress or to generate required response.</b></p>
<h4><b>1.Download Requirements:</b></h4>
<p><b>
	-><a href="https://www.python.org/downloads/">Python 3 or above with pip</a><br>
	-><a href="https://git-scm.com/downloads">Git</a>
</b></p>
<h4><b>2.Download Repository:</b></h4>
<p><b>
	->git clone https://github.com/TheCaduceus/CloneBot_V2<br>
	->Or Download from <a href="https://github.com/TheCaduceus/CloneBot_V2/releases">Here</a>
</b></p>
<h4><b>3.Install CloneBot_V2 Requirements:</b></h4>
<p><b>
	->cd CloneBot_V2<br>
	->pip install -r requirements.txt
</b></p>
<h4><b>4.Download Gclone:</b></h4>
<p><b>
	->Go to <a href="https://clonebot.tk/0:/">Gclone Library</a> and download Gclone file as per your Operating System and place it in "telegram_gcloner" folder.<br>
	->Website provides direct download link, so you can also use Command-line to download Gclone.<br>
	Linux:<br>
	->curl download_link_here >> telegram_gcloner/gclone<br>
	Windows:<br>
	->curl download_link_here >> telegram_gcloner/gclone.exe
</b></p>
<h4><b>5.Edit Config.ini file</b></h4>
<p><b>
	->Open config.ini file in any text editor and enter the values of variables as <a href="https://github.com/TheCaduceus/CloneBot_V2#%EF%B8%8Fdeployment">written here</a><br>
	<br>Or you can download your config.ini file from external source using <a href="https://github.com/TheCaduceus/CloneBot_V2#getting-config_file_url">CONFIG_FILE_URL</a> by using Command-line:<br>
	->curl CONFIG_FILE_URL >> telegram_gcloner/config.ini
</b></p>
<h4><b>6.Start CloneBot_V2:</b></h4>
<p><b>
      ->cd CloneBot_V2<br>
      ->python telegram_gcloner/telegram_gcloner.py
</b></p>
<h4><b>7.Stop CloneBot_V2:</b></h4>
<p><b>
	->Press CTRL + C keys
</b></p>
<!---Termux--->
<h2><b>📱Deploy on Termux</b></h2>
<p><b>Termux is a best app for running and using Command-line tools on Mobile, CloneBot can also be deploy on your Mobile using Termux itself, don't worry because CloneBot V2 is very lightweight and designed to be deployed even on low-end systems and thus it will not cause heavy load on your Mobile.</b></p>
<h4><b>1.Download Termux app: <a href="https://github.com/termux/termux-app/releases" alt="Download-Termux">Download Here</a></b></h4>
<h4><b>2.Choose specific code <a href="https://github.com/TheCaduceus/CloneBot_V2/blob/main/Termux-Guide.md">from here</a> based on architecture of your phone.</b></h4>
<h4><b>3.Run the code you got from above and follow on-screen instructions.</b></h4>
<h2><b>🎲Deploy on Scalingo</b></h2>
<p><b>CloneBot V2 is also deployable to Scalingo cloud, Just deploy "Scalingo" Branch. You only have to provide <a href="https://github.com/TheCaduceus/CloneBot_V2#getting-config_file_url">CONFIG_FILE_URL</a while deploying on Scalingo.</b></p>
<!---Creating Service Accounts--->
<h2><b>🪪 Making Service Accounts</b></h2>
<p><b>Service Accounts are just like normal Google Account and thus have same Upload or Download limits as Google Account which is 750GB Upload and 10TB Download. They are used to act on behalf of a Google Account and hence we can use them to prevent hitting Google Drive limits by creating them in a bulk amount. After creating Service Accounts, we have to add them in Google Group so that we can directly add Google Group's Email ID in Shared Drive at place of adding each Service Accounts manually.</b></p>
<h3><b>🛠️ Create Service Accounts</b></h3>
<h4><b>1.First go to <a href="https://console.cloud.google.com/welcome">Google Cloud Console</a> and select "Crete or select a project" then click "CREATE PROJECT" as shown in the image.</b></h4>
<img src="Img/1.png" alt="1">
<img src="Img/2.png" alt="2">
<h4><b>2.Now give your Project Name, for location select "No organization" and click "CREATE".</b></h4>
<img src="Img/3.png" alt="3">
<h4><b>3.Once your project is created! then click "SELECT PROJECT". Now click on hamburger menu and hover the cursor on "APIs and services" after which a small drop-down menu list is visible, select "Enabled APIs and services"</b></h4>
<img src="Img/4.png" alt="4">
<img src="Img/5.png" alt="5">
<h4><b>4.After it, Click "ENABLE APIS AND SERVICES" button and search for "Google Drive API" in the Search bar as shown in the image.</b></h4>
<img src="Img/6.png" alt="6">
<img src="Img/7.png" alt="7">
<h4><b>5.Open "Google Drive API" and click on "ENABLE" button to enable it for your Project.</b></h4>
<img src="Img/8.png" alt="8">
<h4><b>6.Once Enabled, Click on "OAuth consent screen" then select "External" as "User Type" and click "CREATE" button.</b></h4>
<img src="Img/9.png" alt="9">
<img src="Img/10.png" alt="10">
<h4><b>7.It will now open "Edit app registration" screen, provide App Name, Support Email and Developer Email ID (Same as Support Email ID) and then click "SAVE AND CONTINUE" button.</b></h4>
<img src="Img/11.png" alt="11">
<h4><b>8.Now it will ask you to "ADD OR REMOVE SCOPES", just ignore this and directly click "SAVE AND CONTINUE" button. Then it will ask you to "ADD USERS" again ignore it and directly press "SAVE AND CONTINUE"</b></h4>
<img src="Img/12.png" alt="12">
<img src="Img/13.png" alt="13">
<h4><b>9.At summary page, press "BACK TO DASHBOARD" and click "PUBLISH APP".</b></h4>
<img src="Img/14.png" alt="14">
<img src="Img/15.png" alt="15">
<h4><b>10.After publishing, Select "Credentials" and click "CREATE CREDENTIALS", from drop down list select "OAuth Client ID".</b></h4>
<img src="Img/16.png" alt="16">
<img src="Img/17.png" alt="17">
<h4><b>11.Choose Application type as "Desktop app" and press "CREATE" button. Now create a Folder on your computer with name like "My Service Accounts", and then from pop-up click "DOWNLOAD JSON". Download the json file as "credentials.json" in the folder you just created.</b></h4>
<p><b>⛔NOTE: Download json file as credentials.json only!</b></p>
<img src="Img/18.png" alt="18">
<img src="Img/19.png" alt="19">
<h4><b>12.Once downloaded, now download some required python scripts <a href="https://www.caduceus.ml/files/SA%20-%20Auth%202.0.zip">from here</a> and extract it. Then move "gen_sa_accounts.py","rename_script.py" as well as "requirements.txt" files to folder in which you downloaded "credentials.json".</b></h4>
<img src="Img/20.png" alt="20">
<h4><b>13.Before we proceed further, please confirm you have installed Python (with pip) carefully. Not downloaded yet?<a href="https://www.python.org/downloads/" alt="Download Python"> Download Now!</a></b></h4>
<h4><b>14.All Ready? Type "cmd" in the address bar of folder which you created in STEP 11 and hit ENTER or as an alternative of this, you can use "cd" command like "cd FOLDER_PATH" in CMD.</b></h4>
<img src="Img/23.png" alt="23">
<h4><b>15.Now run following commands carefully in CMD one-by-one:</b></h4>
<!---Commands--->
<p><b>
	1. pip3 install -U -r requirements.txt - To install requirements.<br>
	2. py gen_sa_accounts.py - To get login URL.
</b></p>
<h4><b>16.Running command 2 will give you a Login URL, just copy & paste it in your URL and login using your Google Account and provide all asked permission.</b></h4>
<p><b>⛔NOTE: Login only with Google account which you used to create Project on Google Cloud Console.</b></p>
<img src="Img/21.png" alt="21">
<img src="Img/22.png" alt="22">
<h4><b>17.Back to CMD screen, run following commands carefully one-by-one:</b></h4>
<!---Commands--->
<p><b>
	3. py gen_sa_accounts.py --list-projects - To get the ID of your created Project.<br>
	4. py gen_sa_accounts.py --enable-services PROJECT_ID - To Enable Services in given project.<br>
	5. py gen_sa_accounts.py --create-sas PROJECT_ID - To create Service Accounts.<br>
	6. py gen_sa_accounts.py --download-keys PROJECT_ID - To download Service Accounts file.<br>
	7. py rename_script.py - To rename Service Accounts file in 1-100 sequence.
</b></p>
<p><b>⛔NOTE: Replace PROJECT_ID with Project ID which you will get from command 3 and if commands not working then replace "py" with "python".</b></p>
<h4><b>18.Till now, We have created 100 Service Accounts but we have to do some more work before we take them in our use. Open folder which you created in STEP 11 and you will see "accounts" folder in it which have your 100 Service Accounts file (json files), now type "Powershell" in address bar of accounts folder or as an alternative you can use "cd" commands like "cd FOLDER_PATH" in Powershell.</b></h4>
<img src="Img/24.png" alt="24">
<h4><b>19.Done? Now run following command in Powershell:</b></h4>
<!---Powershell-Command--->
<p><b>
	8. $emails = Get-ChildItem .\**.json |Get-Content -Raw |ConvertFrom-Json |Select -ExpandProperty client_email >>emails.txt
</b></p>
<h4><b>20.Above command collects the EMAIL-ID of all your Service Accounts available in "accounts" folder into emails.txt file. Move "emails.txt" file from accounts folder to prevent confusion or any other problem.</b></h4>
<h3><b>🌐 Adding in Google Group</b></h3>
<h4><b>21.Last work! we have to add them in a Google Group and have to add that Google Group in a Shared Drive to give read + write permission to all Service Accounts at once. Go to <a href="https://groups.google.com" alt="Create Google Group">Google Groups</a> and press "Create group" button to create a group.</b></h4>
<img src="Img/25.png" alt="25">
<h4><b>22.In pop-up, fill up details of your Google Group like Name and Email ID as shown in the image then press "Next". After it, let privacy settings as it is and again click "Next"</b></h4>
<img src="Img/26.png" alt="26">
<img src="Img/27.png" alt="27">
<h4><b>23.Once done, it will ask you to "Add Members" in your Group as shown in the image,just ignore it and directly press "Create Group". Now open your Google Group and select "Members" from sidebar and click "Add Members"</b></h4>
<img src="Img/28.png" alt="28">
<img src="Img/29.png" alt="29">
<h4><b>24.In the pop-up shown, enable "Directly add members" and open "emails.txt" file which you got from STEP 19 then copy & paste 10 Email IDs in the field named "Group Managers". In this way! add all 100 Email IDs in your Google Group but only 10 Email IDs at once.</b></h4>
<img src="Img/30.png" alt="30">
<h4><b>25.After adding all Email IDs of your Service Accounts, now copy the Email ID of your Google Group which looks like XXXXX@googlegroups.com and add it in your Shared Drives as "Manager".</b></h4>
<img src="Img/31.png" alt="31">
<h4><b>26.Finally! We have created 100 Service Accounts and also added them in Google Group. Each Service Account have 750 GB Upload/Clone limit and 10 TB Download limit that means now we can upload/clone 75 TB and can download 100 TB a day.</b></h4>
<h2><b>⛑Contact Us!</b></h2>
<h4><b>Join our Update Channel at Telegram:<a href="https://telegram.me/TheCaduceusUPDATE"> Join Now!</a></b></h4>
<h4><b>Directly Contact the Developer using Telegram <a href="https://telegram.me/HelpAutomatted_Bot">@HelpAutomatted_Bot</a></b></h4>
<h2><b>❤️Credits & Thanks</b></h2>
<h4><b>🔥CloneBot V2:</b></h4>
<p><b><a href="https://github.com/TheCaduceus">Dr.Caduceus</a>: For making this Project and Guide.</b></p>
<p><b><a href="https://github.com/l3v11">Levi</a>: For Gclone and upgrading it.</b></p>
<h4><b>⚡CloneBot:</b></h4>
<p><b>
	<a href="https://github.com/wrenfairbank/telegram_gcloner">wrenfairbank</a>: For the original python script.<br>
	<a href="https://github.com/smartass08/telegram_gcloner">smartass08</a>: To adapt the scrip to heroku.<br>
	<a href="https://github.com/anymeofu/CloneBot">anymeofu</a>: For making the Direct Heroku deployable Version.<br>
	<a href="#">Zero-The-Kamisama</a>: To making MsGsuite discover this amazing bot and the detailed instructions.<br>
	<a href="https://t.me/zorgof">zorgof</a>: For the termux script.<br>
	<a href="https://github.com/aishik2005">Aishik Tokdar</a>: For Adding Guide to Deploy on Railway.app , Qovery , Clever Cloud , Scalingo and some other Code Improvements.Also Added Heroku Workflow Deployment Method.<br>
	<a href="https://github.com/tiararosebiezetta">Katarina</a>: For adding the ability to be deployed to Clever Cloud and Scanlingo.<br>
	<a href="https://github.com/missemily2022">Miss Emily</a>: For adding Support of Okteto Cloud Deployment as well as improving little layout.
</b></p>
