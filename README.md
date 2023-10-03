# CD-Final-Assignment
# Report
## Three components that are part of my assignment:

1. GitHub Actions:

- GitHub Actions is an automation and workflow automation tool. It allows developers to automate tasks, workflows, and CI/CD processes directly within the GitHub repositories. It is a really powerful tool. In this assignment, I created a GitHub Action that runs a test first on the code, and if it passes the test, it deploys it on my VPS automatically.

2. VPS:

- It is a virtual private server or virtualized server environment provided by Digital Ocean, which is a hosting company. It operates on a large physical server but works as an independent and isolated server with its own operating system, in this case Ubuntu, but when you are creating your own droplet, you have more choices to choose from.

3. SSH:

- SSH, or Secure Shell, is a cryptographic network protocol used to securely access and manage networked devices and servers over an unsecured network. It provides a secure channel for data communication or remote command execution. SSH is frequently used for remote administration and secure file trasfer, as in this assignment as well.

## Three problems I have encountered during my assignment:

1. When I started to make the yml file for the tests and the deployment, I made a spelling mistake. Instead of `appleboy/ssh-action@v0.1.2` I had `appelboy/ssh-action@v0.1.2` which of course caused an error, and I was just unable to connect to the VPS. It took me a good while until I found the problem, but when I did, connecting wasn't an issue anymore.

2. After I fixed the first issue, I realised that the most important part was still missing from my assignment, which was the conditional deployment. I have been searching through the internet for a solution but could not really find the right match until I dug deeper into the github workflow syntax and found `needs`, which saved the day.

3. In the process of deploying, I kept getting the error `Host key verification failed`. I found out that I was getting this error message because GitHub was not the on list of known hosts. After I added it, the problem was solved.

4. In the begining, for the SSH_KEY, I used the public key instead of the private key. It's not a surprise that I couldn't connect to my VPS. In the end, I ended up starting the whole process of generating an SSH public and private key on a new VPS server, and I came across the cause of the problem while I was setting everything up again. Since I already had a new VPS started up, I finished it and used that one for my assignment.
