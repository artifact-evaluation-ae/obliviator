#!/bin/bash -x

cd ~/Parallel-join/fk_join/;
make clean; make;

cd ~/Parallel-join/opaque_shared_memory/operator_3/3_2;
make clean; make;