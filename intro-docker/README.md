# Jamhacks 6 - Intro to Docker

## A Shift in the Industry

Before we actually start talking about Docker, I'm going to start off with a bit of history how applications are designed.

### Monolithic Applications

For many years the most popular way of designing an application is as a monolith. For the most part, what this meant is that the whole application would just run as a single process. Consider a social media app with some features, for example you could post, message others, and can browse a marketplace. Under the monolithic model, all of these would be running as part of the same process, similar to this:
<center> <img src="media/monolith.svg" width="80%"> </center>

Monolithic apps really caught on because of their simplicity. They are really easy to reason about and deploy. The fact that it's all in a single process makes it much easier to visualize and trace how data flows in the application. In addition, many applications ended up as a single file, like a Java `.jar` or some other kind of executable. This means that running the application was just a matter of executing the file that contains the code for it. 

This sounds really great, especially for small apps. As the application grows though problems start to crop up. First of all, start up time is really affect by such a large application. This has been known in larger companies to be issues after servers have gone down that getting them running again. Performance is also impacted by monolithic applications at times, such as investigated in this [paper](https://www.researchgate.net/publication/327918047_Performance_Analysis_of_Monolithic_and_Micro_Service_Architectures_-_Containers_Technology_Proceedings_of_the_7th_International_Conference_on_Software_Process_Improvement_CIMPS_2018). There are other issues related to development later on. Because the application is a single executable, every time there is a change the whole executable has to be rebuilt and redeployed. There are of course ways to cache some results in the build step, but redeploying the app can be slow as discussed before. A final issue I want to talk about is code coupling. It is easy to design a monolithic application that where the features and systems are tightly coupled together. This is because of the "single process" nature of the application. This leads to making it much harder to make changes as a single change might affect very many features in the app, as all rely on this one feature to work in a particular way. There are ways around this though with good design! I found this [article](https://codeopinion.com/loosely-coupled-monolith/) an interesting read.

### Microservices
Over the last decade or so, another way of designing an application emerged: Microservices. Although it was talked about an demoed before, the big push for these designs started with Docker's launch in 2013. The idea behind microservices is to split the application into smaller features, each being a process. These processes then communicate with each other to perform the same functionality as the traditional monolithic app. An example of a microservice application is:
<center> <img src="media/microservices.svg" width="80%"> </center>
This model really tries to solve some issues with the monolithic design. The first one is deployment. The microservices are very light weight, so launching one is much quicker. This is especially true when a service goes down. Instead of the whole app needing to start up, a single service just needs to start. In particular, this is useful if a service fails and needs to restart. Instead of needing to restart the whole app it will only need to relaunch the single service.

Making changes too and deploying is less intrusive on currently running services. You only really need to deploy the services that you make changes to. In addition, the separation promotes more decoupled code from the get-go.

The biggest issue with Microservices though is the complexity of the design. The way that everything interacts might be very intricate. You need to spend much more time when actually designing and implementing the services.

## Virtualization
So how does Docker help with implementing microservices? The basic answer: It manages the computer's resources for the services. What it does is called "Virtualization", basically abstracting away the hardware of the computer and managing the resources like Memory and CPU time for the processes.

Virtualization was introduced many years ago with virtual machines (VMs). The idea behind a VM is use software to manage the hardware resources for a computer, again with the purpose of abstracting it away. This software is called a Hypervisor. Having a hypervisor could allow you to run several operating systems, each thinking it's just interacting with the hardware directly, but in reality everything is being rerouted through the hypervisor. A virtual machine setup could look something like this:
<center> <img src="media/vm.svg" height="200px"> </center>
There are two types of hypervisors, Type 1 do not have an operating system between it and the Hardware, while Type 2 hypervisors do. If you've ever used a hypervisor on your own computer, such as VMware workstation, you probably used a Type 2. Type 1 hypervisors are used most commonly on servers.

It does seem like we can run microservices as I described above using this setup and we technically could. We can have each service inside its own VM and set up a way for them to interact. There is an inefficiency here though; Each VM must have a all the files for an operating system. There is a lot of redundancy as many of these files will be the exact same across all VMs.

This is a big change that Docker did, they reduced the number of copies to files! The biggest difference for Docker is that the Kernel, basically a process doing the management of resources, is shared between all of the virtual instances. For terminology, Docker uses the word Container, which is analogous to a Virtual Machine for a hypervisors. Each container will have access to the same Kernel which is necessarily run on an existing OS, called the Host OS. The setup looks like this:
<center> <img src="media/containers.svg" height="200px"> </center>
A process called the Docker Daemon will act analogous to the hypervisor, actually allocating resources to the containers by communicating with the Kernel. All of the containers run some sort of Linux operating system. Interestingly, to be able to run these containers on Windows or Mac OS, we actually need to run the Linux Host OS in a operating system itself! You can see these two technologies build on top of each other! 

There are two more benefits I want to talk about that comes around from virtualization. First of all, it is very easy to move around the files to actually launch containers and VMs. The point is, you can set up an environment for running and app inside of a VM or container and then send it to a different computer and it will behave the same way! (With some exceptions unfortunately though). This makes it so much easier for developing and deploying applications. The second ability is isolation. Since all resources are managed by software, the Daemon/Hypervisor, the software can manage what parts of the system that a container has access to (I will start just saying container from now on, this also applied to VMs though). This can mean a few things. First, the container will only have access to files that the Daemon allows it to see. This means that the container won't be able to necessarily browse the Host OS's files, or those in other containers (we can enable it though!). Another thing that isolation could provide is not being able to see the other processes, or even containers. Really as far as the container concerned, it is running straight on the hardware. It doesn't know about anything that Docker is doing behind the scenes. What we can set up though are Volumes for storing files and Networks for containers to communicate!

## Getting Started with Docker

### Getting Docker Installed
I won't be going through the actual installation process, but here are some links to how to do so:
- [Docker Desktop](https://docs.docker.com/get-docker/) for Mac/Windows/Linux
- [Debian Linux](https://docs.docker.com/engine/install/debian/) like Ubuntu
- [Fedora Linux](https://docs.docker.com/engine/install/fedora/)

In general you can probably search "[My OS] install docker" for steps how to do so.

### Running a Container
The features in Docker revolve around containers. What is a container though? The way I often thinking about it is as a lightweight virtual computer running on top of my physical computer. To this computer it feel like it is just a normal system, even though we know it's not.

A container is launched using an existing "Template" called an Image. An image is just the state we will be launching the container in. It knows the files that the container will know about by default and will likely have some command that it runs when the container is launched. This Image can be used to launch many containers, again it is just a template for how the container will start out as.

#### Launching our First Container
Let's get to actually launching a container!
Docker provides a great "Hello World" container that we can run to make sure docker is installed properly.
We can run `docker run hello-world`.

You might see something like:
```
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
7050e35b49f5: Pull complete 
Digest: sha256:80f31da1ac7b312ba29d65080fddf797dd76acfb870e677f390d5acba9741b17
Status: Downloaded newer image for hello-world:latest
```

What's happening is that Docker is looking for the image `hello-world`. Assuming we have a new installation of Docker, such an image doesn't exist. It will then try to look for such an image in some repository, in this case DockerHub. It downloads the files for the image and then runs a container from that image.

We will be using `docker run` quite a bit today and trying out various configurations with it.

We will quickly check out two more commands, `docker ps` and `docker images`.
First, let's run `docker images`. What this will do is print out what images you have on your system. Doing so now may look something like this:
```
REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
hello-world   latest    46331d942d63   2 months ago   9.14kB
```
We can see that we currently have the `hello-world` image downloaded. Remember how we saw the `Unable to find image 'hello-world:latest' locally` message before? Well now if we run `docker run hello-world` it will see that we have that an image called that already and launch that one. Something we will come back to soon is tags. They essentially allow you to have different versions of an image.

Let's take a look at `docker ps` now. It will display the current containers that you have. Let's run it now.
Just running `docker ps` right now might look pretty empty:
```
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```
This is because we don't actually have any active containers. Whenever you run a container, once the main command finishes it will stop the container. We can see all containers by doing `docker ps -a`:
```
CONTAINER ID   IMAGE         COMMAND    CREATED         STATUS                     PORTS     NAMES
e3f4268e7026   hello-world   "/hello"   2 minutes ago   Exited (0) 2 minutes ago             friendly_davinci
9ca9ae659ea1   hello-world   "/hello"   2 minutes ago   Exited (0) 2 minutes ago             cool_napier
```

Your output might look something like this. You can see some of information about the containers. We can confirm why we didn't see these containers just from running `docker ps`, they have the `Exited` status.

We will be using some of this information from `docker ps` and `docker images` quite a bit.

Before moving on, let me quickly talk about `docker logs`. It will print out the output that the container has produced while it was active. We run `docker logs <id>` to see the logs for that container. Doing so on the containers we launched from `hello-world` should bring up the same message as before. The `<id>` for the command (and for commands going forward) can be either be the ID under `CONTAINER ID` or the name under `NAMES`. Also, the concrete IDs I will be using are the ones from the examples I provide. Use the ones that your containers launch with.

A note about the `CONTAINER ID`, you can specify just enough to distinguish the container from all others. In this case we can use `e` or `e3` or `e3f`, etc. as the ID for the first container.

#### Cleaning Up

Once we don't need a container and/or image, we can delete them. This makes it easier to navigate your containers and images, and can free up space that the files for the images are using.

To remove an image, we run `docker rmi <id...>`. We can specify a list of image IDs we want to delete. Note that we shouldn't be deleting images for containers that currently exist, although technically we can.

`docker rm <id...>` let's you delete a container. In a similar way to deleting images, we're not able to delete containers which are running. We will need to run `docker stop <id...>` (or if necessary `docker kill <id...>`) to stop the container. Luckily for us our containers have already exited. Let's then run:
```
docker rm e3 cool_napier
docker rmi hello-world
```

Then running `docker ps -a` and `docker images` will show you that they have indeed been deleted.
