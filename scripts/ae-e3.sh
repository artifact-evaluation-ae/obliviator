#!/bin/bash -x

cd ~/obliviator/operator_1/;
make clean; make;
./host/parallel ./enclave/parallel_enc.signed 1 ./test.txt;
make clean;

cd ~/obliviator/opaque_shared_memory/operator_1/;
make clean; make;
./host/parallel ./enclave/parallel_enc.signed 1 ./test.txt;
make clean;