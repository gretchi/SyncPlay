FROM ubuntu:22.04

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y g++ make cmake build-essential unzip pkg-config

WORKDIR /root/build



CMD make
