#!/bin/bash -x

cd ~/obliviator/join;
make clean; make;

if [ $? -ne 0 ]; then
    echo "Error: The compilation with Open Enclave failed."
    exit 1
fi

cd ~/obliviator/join_kks;
make clean; make L3=1;

if [ $? -ne 0 ]; then
    echo "Error: The compilation with Intel SGX failed."
    exit 1
fi