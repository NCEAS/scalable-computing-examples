# Dockerfile for Scalable Computing Course
# Build with:
#     docker build -t mycontainer:0.1 .
FROM ubuntu:22.04
SHELL ["/bin/bash", "-c"]
WORKDIR /home/scomp
RUN apt update && apt -y install python3 pip virtualenvwrapper vim nano iproute2
RUN groupadd -r scomp && useradd -r -g scomp scomp
RUN mkdir -p /home/scomp && chown scomp.scomp /home/scomp
USER scomp:scomp
RUN echo "source /usr/share/virtualenvwrapper/virtualenvwrapper.sh" >> /home/scomp/.bashrc
COPY ./requirements.txt .
RUN source /usr/share/virtualenvwrapper/virtualenvwrapper.sh && \
	mkvirtualenv scomp && \
	pip install --no-cache-dir --upgrade -r requirements.txt
CMD ["/bin/bash"]
