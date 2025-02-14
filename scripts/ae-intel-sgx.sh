#!/bin/sh

sudo apt update;
sudo apt upgrade -y;
sudo apt-get install -y build-essential;
sudo apt-get install -y ocaml;
sudo apt-get install -y ocaml-nox;
sudo apt-get install -y ocamlbuild;
sudo apt-get install -y automake;
sudo apt-get install -y autoconf;
sudo apt-get install -y libtool;
sudo apt-get install -y wget;
sudo apt-get install -y python-is-python3;
sudo apt-get install -y libssl-dev;
sudo apt-get install -y git;
sudo apt-get install -y cmake;
sudo apt-get install -y perl;
sudo apt-get install -y libssl-dev;
sudo apt-get install -y libcurl4-openssl-dev;
sudo apt-get install -y protobuf-compiler;
sudo apt-get install -y libprotobuf-dev;
sudo apt-get install -y debhelper;
sudo apt-get install -y cmake;
sudo apt-get install -y reprepro;
sudo apt-get install -y unzip;
sudo apt-get install -y pkgconf;
sudo apt-get install -y libboost-dev;
sudo apt-get install -y libboost-system-dev;
sudo apt-get install -y libboost-thread-dev;
sudo apt-get install -y lsb-release;
sudo apt-get install -y libsystemd0;
sudo apt-get install -y dkms;

cd ~/;
git clone https://github.com/intel/linux-sgx.git;
(if ! grep SGX_LINUX_PATH ~/.bashrc; then
    (echo && echo 'export SGX_LINUX_PATH=/home/'$USER'/linux-sgx') >> ~/.bashrc
fi);
cd /opt/intel;
sudo wget https://download.01.org/intel-sgx/latest/linux-latest/distro/ubuntu20.04-server/sgx_linux_x64_driver_2.11.b6f5b4a.bin;
sudo chmod 777 sgx_linux_x64_driver_2.11.b6f5b4a.bin;
sudo ./sgx_linux_x64_driver_2.11.b6f5b4a.bin;
cd ~/linux-sgx;
make preparation;
sudo cp external/toolset/ubuntu20.04/* /usr/local/bin;
which ar as ld objcopy objdump ranlib;
find ./ -type f | grep \\.sh$ | xargs chmod +x;
find ./ -type f | grep configure$ | xargs chmod +x;
sudo apt-get install -y ocamlbuild;
sudo apt-get install -y ocaml-nox;
sudo apt-get install -y python-is-python3;
sudo apt-get install -y nasm;
make sdk;
make sdk_install_pkg;
