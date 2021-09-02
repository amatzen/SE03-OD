# Lab: Questions 

**Your tasks:**

1. Explain what a Dockerfile is.
   1. How does it work?
   2. Which instructions can be used?
   3. What do the above-mentioned instructions do?
2. Explain how a Docker image is built.
   1. Which options do you know?
   2. What are they used for?
3. Explain how a Docker container is runned.
   1. Which options do you know?
   2. What are they used for?
4. 'Compare cheat sheets and share your pearls of wisdom.



**Answer:**

Q1:

A Dockerfile is a set of instructions to build a image. It typically starts by inheriting another image ("the base image") (e.g. an application (nginx, python) or an operating system (ubuntu, alpine)) and then use the builtin Dockerfile operators like RUN, COPY, WORKDIR and ENTRYPOINT to customize the image to your application's needs. RUN inserts a command into the base image's shell. COPY copy (a) file(s) from the host system to the image. WORKDIR changes the current working directory. ENTRYPOINT is the main executable, that the Docker image listens to.

Q2:



Q3:

The HyperVisor spins up a virtual environment (the container) and boots the image up and listens to the entrypoint. They are primarily used for distrubing applications.

`-d`for running it detached. `-p`for port forwarding. `-v`for volume mapping. `--name`for naming. Various network commands, and so on.

