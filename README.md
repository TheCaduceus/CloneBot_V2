<h1 align ="center"><b>CloneBot V2 🔥</b></h1>
<!---Introduction--->
<p><b>1. The Powerful Telegram Bot based on Gclone to clone Google Drive's Shared Drive data easily.</b></p>
<p><b>2. CloneBot V2 usage Service Accounts to easily clone TBs of data without hitting 750GB Upload/Clone limit of Google Drive.</b></p>
<p><b>3. It is most lightweight and performs only server-sided cloning to have very less load on system and don't use your own bandwidth.</b></p>
<p><b>4. Just provide the sharing link of a particular Shared Drive/folder or file and set multiple destination folders to clone data.</b></p>
<!---Index--->
<h2><b>📑 INDEX</b></h2>
<p><b>Easily navigate through out the guide and learn about Powerful CloneBot V2 and terms related to it.</b></p>
<p><b><a href="https://github.com/TheCaduceus/CloneBot_V2#clonebot-v2-">🔥CloneBot V2 </a></b></p>
<p><b><a href="https://github.com/TheCaduceus/CloneBot_V2#-whats-new">🆕 What's New!</a></b></p>
<p><b><a href="https://github.com/TheCaduceus/CloneBot_V2#-notice">⛔ NOTICE</a></b></p>
<p><b><a href="https://github.com/TheCaduceus/CloneBot_V2#-making-service-accounts">🪪 Making Service Accounts</a></b></p>
<p><b><a href="https://github.com/TheCaduceus/CloneBot_V2#%EF%B8%8F-create-service-accounts">->🛠️ Create Service Accounts</a></b></p>
<p><b><a href="https://github.com/TheCaduceus/CloneBot_V2#-adding-in-google-group">->🌐 Adding in Google Group</a></b></p>
<p><b><a href=""></a></b></p>
<p><b><a href=""></a></b></p>
<p><b><a href=""></a></b></p>
<p><b><a href=""></a></b></p>
<!---ChangeLog--->
<h2><b>🆕 What's New!</b></h2>
<p><b>1.Gclone upgraded to v1.58.1 (latest)!😉</b></p>
<p><b>2.Deployment on Okteto & Scalingo Added!🤩</b></p>
<p><b>3.Port Error fixed for Okteto deployments!😄</b></p>
<p><b>4.Bot can be deployed as both Web or Container on Heroku.🙃</b></p>
<p><b>5.Mitigated Time Zone Error while deployment.🤗</b></p>
<p><b>6.Addressed GitHub Workflow Error!😙</b></p>
<p><b>7.Docker Image changed!😌</b></p>
<p><b><a href="www.github.com/TheCaduceus/CloneBot_V2/releases">Show Full Update history</a></b></p>
<!---NOTICE--->
<h2><b>⛔ NOTICE</b></h2>
<p><b>1.You may need account for Heroku/Okteto/Scalingo while deploying CloneBot V2 to on respected platforms.</b></p>
<p><b>2.Service Accounts are mandatory to use CloneBot, because it uses Service Accounts to prevent hitting 750GB Upload/Clone limit of Google Drive while cloning large amount of dat.</b></p>
<p><b>3.VPS or your local machine (PC,Laptop or Mobile) should have Python 3.10 and Git installed in order to run CloneBot V2.</b></p>
<p><b>4.CloneBot V2 don't use your bandwidth or Internet connection while cloning data but it can if hosted on your local machine or VPS for calling required Telegram APIs to update the progress or to generate required response.</b></p>
<p><b>5.This Project comes with GNU License, please consider reading it before using this.</b></p>
<!---Creating Service Accounts--->
<h2><b>🪪 Making Service Accounts</b></h2>
<p><b>Service Accounts are just like normal Google Account and thus have same Upload or Download limits as Google Account which is 750 GB Upload and 10 TB Download. They are used to act on behalf of a Google Account and hence we can use them to prevent hitting Google Drive limits by creating them in a bulk amount. After creating Service Accounts, we have to add them in Google Group so that we can directly add Google Group's Email ID in Shared Drive at place of adding each Service Accounts manually.</b></p>
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
<h4><b>12.Once downloaded, now download some required python scripts from here and extract it. Then move "gen_sa_accounts.py","rename_script.py" as well as "requirements.txt" files to folder in which you downloaded "credentials.json".</b></h4>
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
