#!/bin/sh

cd ~/linux-sgx;
make psw_install_pkg;
sudo ./linux/installer/bin/sgx_linux_x64_psw_2.20.100.4.bin;

cd ~/;
git clone https://github.com/intel/intel-sgx-ssl;
cd intel-sgx-ssl;
cd openssl_source;
wget https://github.com/openssl/openssl/releases/download/openssl-3.1.7/openssl-3.1.7.tar.gz;
cd ../Linux;
make clean;
make;
sudo make install;