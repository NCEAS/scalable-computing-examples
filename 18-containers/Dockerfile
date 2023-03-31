# Dockerfile for Scalable Computing Course
# Build with:
#     nerdctl build -t mycontainer:0.1 .
FROM ubuntu:22.04
WORKDIR /home/scomp
RUN apt update && apt -y install python3 pip virtualenvwrapper
RUN groupadd -r scomp && useradd -r -g scomp scomp
RUN mkdir -p /home/scomp && chown scomp.scomp /home/scomp
#RUN pip install --no-cache-dir --upgrade -r requirements.txt
USER scomp:scomp
CMD ["/bin/bash"]
