<h1 align="center"><b>🐳 Docker Build Guide</b></h1>
<p><b>As per your requirements, or to run CloneBot V2 easily on your OS and its architecture you can make your own Docker Image for CloneBot V2, the process of building docker image is automated and easy, you just need to edit <code>Dockerfile</code> available in root directory <code>main</code> branch and Workflow will be triggered automatically which can be checked from <code>Actions</code> tab.</b></p>
<h2><b>🛠️ Instructions:</b></h2>
<p><b>For quickly building the same Docker Image used by CloneBot V2:</b></p>
<h4><b>1.Go to <code>.github/workflows</code> in <code>main</code> branch.</b></h4>
<img src="https://user-images.githubusercontent.com/87380104/176392810-a0c1b483-82f9-4927-acca-0b9dc3826975.png">
<h4><b>2.Open <code>Docker-Code</code> file and copy its code.</b></h4>
<img src="https://user-images.githubusercontent.com/87380104/176393096-869ea197-5512-4bad-b31e-ce532d2bab08.png">
<h4><b>3.Go back to root directory of <code>main</code> branch and paste the copied code (by removing previous code) in <code>Dockerfile</code>.</b></h4>
<h4><b>4.Once you make new commit, then go to <code>Actions</code> tab and you will see that Workflow is now triggered and started building your <code>Dockerfile</code>.</b></h4>
<img src="https://user-images.githubusercontent.com/87380104/176394414-6c94dae1-d80d-486d-b406-3dc217b37832.png">
<h4><b>5.Your Docker Image is now ready to be used, check out your Repository's <code>Packages</code> to know how to use it.😊</b></h4>
<img src="https://user-images.githubusercontent.com/87380104/176394861-8d0567c2-96ec-4b5b-a5cf-ef20f409489d.png">
