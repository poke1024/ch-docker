# Installing the CH Docker Jupyter Environment

Download `ch_docker.zip` and unzip it. Then follow the descriptions below, depending on your operating system (i.e. Linux, macOS or Windows 10).

If you run into problems, please contact us.

## Why Docker?

Skip this section if you do not care what Docker is and just want to get things running.

Docker is a software that allows you to run software isolated inside a defined environment, a concept not completely unsimilar to virtual machine (VM) solutions like VirtualBox, Parallels or VMWare. However, Docker is much more lightweight, smaller and faster than VMs. In short, Docker allows us to provide you with a defined software stack - consisting of JupyterLab and an installation Python3 - that contains all needed software packages for the course and runs fast and is resource friendly.

While it would be possible to install various necessary packages for the course in isolated Python environments directly on your machine (e.g. using `conda`), this approach breaks down for some other components we use in the course that need compilation for installing them. Docker allows us to provide all course participants with the same working environment, regardless of the operating system you are using.

While the installation of Docker is a bit technical on Linux and cumbersome on Windows, once installed, you will have obtained a fast and tested environment that contains all you need for the course. You won't have to second guess whether installing packages used in the courses will actually work on your machine.

For a short but more detailed introduction of what Docker is and what it is about, watch https://www.youtube.com/watch?v=TvnZTi_gaNc


## Linux

### Docker or not?

We suggest using our prepackaged Docker container to run Jupyter in an isolated environment that comes with all necessary packages.

If you do not want to install Docker, you could alternatively manually install the packages as seen in `ch_docker/docker/Dockerfile` directly on your machine. However we do not encourage this except for tech savvy users who know how to set up isolated Python environments in order to avoid conflicts (we suggest you use dedicated `conda` environments for the Python packages in this case). For the general user, we suggest the following procedure using Docker.

### Installing Docker

Install Docker for Linux. The exact steps depend on your Linux distribution. For Ubuntu, instructions are at https://docs.docker.com/engine/install/ubuntu/. We suggest you follow the steps in the five boxes under the "Install using the repository" option, i.e. starting with "sudo apt-get update" and ending with "sudo apt-get install docker-ce docker-ce-cli containerd.io".

Once Docker is installed, you should be able to run `docker` in a terminal without an error. You then also need to install `docker-compose`. On Ubuntu this can be achieved through `sudo apt install docker-compose`.

To automatically launch the Docker server on boot, you need to take additional steps. For details, see "Configure Docker to start on boot" under https://docs.docker.com/engine/install/linux-postinstall/. On most distros, you want to run `sudo systemctl enable docker`.

### Installing chdocker environment

Basically, we now need to run `docker-compose up`. However, since we share the home folder and need to run `docker-compose up` with `sudo` on a default Docker installation, our `$HOME` directory will be wrong. Also, there are some problems with Docker's volume sharing and user ids. We provide an `up.sh` script that fixes these issues and lets you read and write your HOME directory from Jupyter.

Run:

```
cd /path/to/ch_jupyter/launchers/linux
chmod +x up.sh
cat up.sh  # verify what you are running
./up.sh
```

This will take a while on the first run.

Once the installation is done - this can take up to 30 minutes on the first run - and you see messages with "jupyter_1  |", you can access Jupyter via a web browser on localhost:8888. To test file access works, try to create and save a new Jupyter notebook in one of your folders.

When done, stop the container/server by hitting Control-C in the terminal.


## macOS

You need to install Docker Desktop for Mac, then run `ch_docker/launchers/macOS/Juypter`. Alternatively, you can `cd` to `ch_docker/docker` and run `docker-compose up`. Once the installation is done - this can take up to 30 minutes on the first run - and you see messages with "jupyter_1  |", you can access a preconfigured Jupyter Lab installation via a web browser on localhost:8888. 

To stop Jupyter hit "Cancel" and then "Quit" if you are using the `launchers/macOS/Jupyter` app, or - if you are using the terminal - by hitting Control-C. You can also use the Docker Desktop Dashboard to check and manage running containers.

A step-by-step video of the whole installation procedure is here:

https://www.dropbox.com/s/j24cj4ndijfkfkj/macOS.mp4?dl=0

Note that Docker is by default configured to always run in the background upon each machine launch, which might not be what you want. Please read the section "General Advice on Docker" below.

### Links

Docker Desktop for Mac:
https://hub.docker.com/editions/community/docker-ce-desktop-mac




## Windows 10

You need to install Docker Desktop for Windows with the WSL2 backend. When properly installed, this will allow you to launch the ch_jupyter environment using the `ch_docker/launchers/win10/launch.bat` batch file. 


To stop Jupyter hit "Cancel" and then "Quit" in the Jupyter app, or - if you are using the terminal - by hitting Control-C. You can also use the Docker Desktop Dashboard to check and manage running containers.


We offer two versions for installing these components. Choose the one that suits your level of tech expertise.

### Tech Savvy Version

The installation procedure is unfortunately rather involved. If you are tech savvy, we suggest the following steps:

* Obtain a Docker Hub ID by signing up on Docker Hub (http://hub.docker.com). Your Docker ID is a username you choose yourself.
* Enable hardware virtualization in the BIOS settings. Steps for doing this are here: https://bce.berkeley.edu/enabling-virtualization-in-your-pc-bios.html
* Check that your Windows 10 version has version >= 1903. If not, update accordingly.
* Install WSL2 using the steps described in https://docs.microsoft.com/de-de/windows/wsl/install-win10
* Install Docker Desktop for Windows from https://hub.docker.com/editions/community/docker-ce-desktop-windows 
* Log into Docker, either using the UI or `docker login` on the console using your Docker ID from above
* Once Docker is running, either launch `ch_docker/launchers/win10/launch.bat` or perform the steps yourself in a terminal (look at what `ch_docker/launchers/win10/launch.bat` does).
* Once the container installation is done - this can take up to 30 minutes on the first run - and you see messages with "jupyter_1  |", you can access a preconfigured Jupyter Lab installation via a web browser on localhost:8888. 
* When done, stop the container/server by hitting Control-C. You can also use the Docker Desktop Dashboard to check and manage running containers.

Note that Docker is by default configured to always run in the background upon each machine launch, which might not be what you want. Please read the section "General Advice on Docker" below.

### Easier Version

If you are not so tech savvy, follow this video, which is a step-by-step approach to finishing the installation:

https://www.dropbox.com/s/e099h1vk4z4qzo2/win10.mp4?dl=0

Two corrections to the video:

* The video mentions a separate video on how to obtain a Docker ID. This video does not exist, as the process is really simple. Simply go to http://hub.docker.com and sign up. Your Docker ID is a username you choose yourself.
* The mention to Hyper-V in the BIOS setting is wrong and misleading. What is actually meant is that if problems with starting up Docker persist, you should enable hardware virtualization in your BIOS and described here: https://bce.berkeley.edu/enabling-virtualization-in-your-pc-bios.html

Note that Docker is by default configured to always run in the background upon each machine launch, which might not be what you want. Please read the section "General Advice on Docker" below.

### Links

Docker Desktop for Windows:
https://hub.docker.com/editions/community/docker-ce-desktop-windows

Information on Installing WSL2: 
https://docs.microsoft.com/de-de/windows/wsl/install-win10

Docker Hub:
https://hub.docker.com


## General Advice on Docker

Docker is a system service that, once installed, usually runs in the background each time you reboot your machine. It might also restart containers that were not closed on previous shutdowns, which means your machine might run the CH Jupyter notebook all the time inn background.

If you experience performance problems, configure open up the preferences in Docker Desktop in order to:

	* not start Docker when you login
	* then quit Docker Desktop

This should terminate Docker and all running containers.

Note that you can also use the Docker Desktop Dashboard - accessible via the Docker menu - to check and manage running containers.
