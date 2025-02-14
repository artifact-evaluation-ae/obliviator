#!/bin/bash -x

cd ~/obliviator/fk_join/;
make clean; make;
./host/parallel ./enclave/parallel_enc.signed 1 ./test.txt;


cd ~/obliviator/opaque_shared_memory/fk_join;
make clean; make;
./host/parallel ./enclave/parallel_enc.signed 1 ./test.txt;
