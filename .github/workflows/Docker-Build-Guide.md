<h1 align="center"><b>🐳 Docker Build Guide</b></h1>
<p><b>As per your requirements, or to run CloneBot V2 easily on your OS and depending upon its architecture you can make your own Docker Image for CloneBot V2, the process of building docker image is automated and easy, you just need to edit <code>Dockerfile</code> available in root directory of <code>main</code> branch and trigger the Workflow from <code>Actions</code> Tab and it will start building your Docker Image.</b></p>
<h2><b>🛠️ Instructions:</b></h2>
<p><b>For quickly building the same Docker Image used by CloneBot V2:</b></p>
<h4><b>1.Go to <code>.github/workflows</code> in <code>main</code> branch.</b></h4>
<img src="https://user-images.githubusercontent.com/87380104/176392810-a0c1b483-82f9-4927-acca-0b9dc3826975.png">
<h4><b>2.Open <code>Docker-Code</code> file and copy its code.</b></h4>
<img src="https://user-images.githubusercontent.com/87380104/183818049-2ee29172-c9cf-4d47-bf53-741f1aa9ef70.png">
<h4><b>3.Go back to root directory of <code>main</code> branch and paste the copied code (by removing previous code) in <code>Dockerfile</code>.</b></h4>
<h4><b>4.Once you make new commit, then go to <code>Actions</code> tab and run the <code>Publish Docker Image</code> workflow! and it will start building your Docker Image.</b></h4>
<img src="https://user-images.githubusercontent.com/87380104/183817676-817d3b8a-1bad-4fa3-9043-9ee6f15f394b.png">
<h4><b>5.Your Docker Image is now ready to be used, check out your Repository's <code>Packages</code> to know how to use it.😊</b></h4>
<img src="https://user-images.githubusercontent.com/87380104/176394861-8d0567c2-96ec-4b5b-a5cf-ef20f409489d.png">
<p><b>⛔NOTE: Use your own Docker Image for deploying on VPS only! Using it for deploying platforms like Heroku will simply cause Account suspension.</b></p>
<h2><b>⚙️ Customizations</b></h2>
<p><b>You can also customize the behaviour of Docker Image Build tool as per your needs!😉</b></p>
<h4><b>🔫 Trigger Customization:</b></h4>
<p><b>To set the condition "When Workflow should be triggered?", you can customize following code:</b></p>
https://github.com/TheCaduceus/CloneBot_V2/blob/dbbd61dc0430a5bc8eda672ef4e123a9ee5c2794/.github/workflows/docker-publish.yml#L3-L12
<p><b>by default, Workflow will be triggered only if user manually do it from <code>Actions</code> Tab otherwise if automatic workflow trigger is enabled then it will get triggered automatically when there is new commit (including Pull Request) in <code>main</code> branch which can be changed.</b></p>
<h4><b>✏️ Environment Variables:</b></h4>
<p><b>By setting environment variables you can change the Registry and Name of your Docker Image:</b></p>
https://github.com/TheCaduceus/CloneBot_V2/blob/dbbd61dc0430a5bc8eda672ef4e123a9ee5c2794/.github/workflows/docker-publish.yml#L14-L18
<p><b><code>REGISTRY</code>: Value can be <code>docker.io</code> or <code>ghcr.io</code>. If empty then <code>docker.io</code> will be used.</b></p>
<p><b><code>IMAGE_NAME</code>: Value can be anything between <code>""</code> or by default it is <code>${{ github.repository }}</code> which automatically set Repository name + Branch Name as <code>IMAGE_NAME</code>.</b></p>
