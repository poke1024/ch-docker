# Installation

Download `ch_docker.zip` and unzip it. Then follow the descriptions below, depending on your operating system (i.e. Linux, macOS or Windows 10).

If you run into problems, please contact us.

## Linux

Install Docker for Linux. Then run:

```
cd ch_jupyter/docker
docker-compose up
```

Once the installation is done - this can take up to 30 minutes on the first run - and you see messages with "jupyter_1  |", you can access Jupyter via a web browser on localhost:8888. When done, stop the container/server by hitting CTRL-C.


## macOS

You need to install Docker Desktop for Mac, then run `ch_docker/launchers/macOS/Juypter`. Alternatively, you can `cd` to `ch_docker/docker` and run `docker-compose up`. Once the installation is done - this can take up to 30 minutes on the first run - and you see messages with "jupyter_1  |", you can access a preconfigured Jupyter Lab installation via a web browser on localhost:8888. 

To stop Jupyter hit "Cancel" and then "Quit" if you are using the `launchers/macOS/Jupyter` app, or - if you are using the terminal - by hitting CTRL-C. You can also use the Docker Desktop Dashboard to check and manage running containers.

A step-by-step video of the whole installation procedure is here:

https://www.dropbox.com/s/j24cj4ndijfkfkj/macOS.mp4?dl=0

Note that Docker is by default configured to always run in the background upon each machine launch, which might not be what you want. Please read the section "General Advice on Docker" below.

### Links

Docker Desktop for Mac:
https://hub.docker.com/editions/community/docker-ce-desktop-mac




## Windows 10

You need to install Docker Desktop for Windows with the WSL2 backend. When properly installed, this will allow you to launch the ch_jupyter environment using the `ch_docker/launchers/win10/launch.bat` batch file. 


To stop Jupyter hit "Cancel" and then "Quit" in the Jupyter app, or - if you are using the terminal - by hitting CTRl-C. You can also use the Docker Desktop Dashboard to check and manage running containers.


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
* When done, stop the container/server by hitting CTRL-C. You can also use the Docker Desktop Dashboard to check and manage running containers.

Note that Docker is by default configured to always run in the background upon each machine launch, which might not be what you want. Please read the section "General Advice on Docker" below.

### Easier Version

If you are not so tech savvy, follow this video, which is a step-by-step approach to finishing the installation:

https://www.dropbox.com/s/e099h1vk4z4qzo2/win10.mp4?dl=0

Two corrections to the video:

* The video mentions a separate video on how to obtain a Docker ID. This video does not exist, as the process is really simple. Simply go to http://hub.docker.com and sign up. Your Docker ID is a username you choose yourself.
* The mentioned Hyper-V BIOS setting is wrong and misleading. What is actually meant is that if problems with starting up Docker persist, you should enable hardware virtualization in your BIOS and described here: https://bce.berkeley.edu/enabling-virtualization-in-your-pc-bios.html

Note that Docker is by default configured to always run in the background upon each machine launch, which might not be what you want. Please read the section "General Advice on Docker" below.

### Links

Docker Desktop for Windows:
https://hub.docker.com/editions/community/docker-ce-desktop-windows

Information on Installing WSL2: 
https://docs.microsoft.com/de-de/windows/wsl/install-win10

Docker Hub:
https://hub.docker.com


## Why Docker?

While it would be possible to install various necessary packages for the course on your machine in isolated Python environments (e.g. using `conda`), this approach breaks down for some other components we use in the course (e.g. Tesseract). Docker allows us to provide all course participants with a standard working environment, regardless of the operating system you are on.

## General Advice on Docker

Docker is a system service that, once installed, usually runs in the background each time you reboot your machine. It might also restart containers that were not closed on previous shutdowns, which means your machine might run the CH Jupyter notebook all the time inn background.

If you experience performance problems, configure open up the preferences in Docker Desktop in order to:

	* not start Docker when you login
	* then quit Docker Desktop

This should terminate Docker and all running containers.

Note that you can also use the Docker Desktop Dashboard - accessible via the Docker menu - to check and manage running containers.
