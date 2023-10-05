# CD-Final-Assignment
# Report
## Three components that are part of my assignment:

1. GitHub Actions:

- GitHub Actions is an automation and workflow automation tool. It allows developers to automate tasks, workflows, and CI/CD processes directly within the GitHub repositories. It is a really powerful tool. In this assignment, I created a GitHub Action that runs a test first on the code, and if it passes the test, it deploys it on my VPS automatically.

2. VPS:

- It is a virtual private server or virtualized server environment provided by Digital Ocean, which is a hosting company. It operates on a large physical server but works as an independent and isolated server with its own operating system, in this case Ubuntu, but when you are creating your own droplet, you have more choices to choose from.

3. SSH:

- SSH, or Secure Shell, is a cryptographic network protocol used to securely access and manage networked devices and servers over an unsecured network. It provides a secure channel for data communication or remote command execution. SSH is frequently used for remote administration and secure file trasfer, as in this assignment as well.

## Problems I have encountered during my assignment:

* Making the yml file for the tests and the deployment took a some time, I needed extra info about the matter and read alot of articles to fully understand how it works especially about conditional deployment but I managed to found the right info in github workflow syntax.

* In the process of deploying, I kept getting the error `Host key verification failed`. Furthermore I have alot of problems using the needed keys (public and private) but after alot of trial and errors I managed to fill in the right keys into the settings and preferences. Also I got an error Ssh: handshake failed: ssh: unable to authenticate, attempted methods [ none publickey] which I couldn't solve at the first place but after looking for answers on the net I manage to solve the problem by changing the key algorithm on the server. Setting up the configuration of nginx and systemd CD service was also a challenge but all in all I managed to let it work. A very nice assignment and I learned a lot by trial and error.


