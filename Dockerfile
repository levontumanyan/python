FROM python:3.10

RUN apt-get update && apt-get install -y \
 	&& rm -rf /var/lib/apt/lists/*

# Set user and group
ARG user=levtuman
ARG group=gamers
ARG uid=1000
ARG gid=1000
RUN groupadd -g ${gid} ${group}
RUN useradd -u ${uid} -g ${group} -s /bin/sh -m ${user} # <--- the '-m' create a user home directory
ENV HOME /home/${user}

WORKDIR ${HOME}

# COPY factorial.c to workdir
# COPY --chown="${user}":"${group}" factorial.c factorial.c

# Switch to user
USER ${uid}:${gid}