#!/bin/bash -x

cd ~/Parallel-join/scripts/;
sed '53i CFLAGS = -march=native -mno-avx512f -O3 -Wall -Wextra -Werror' Makefile | tee ~/Parallel-join/join/Makefile;

cd ~/Parallel-join/;
mkdir result;

cd ~/Parallel-join/join/;
make clean; make;
./host/parallel ./enclave/parallel_enc.signed 1 ~/Parallel-join/data/TPCH/data.txt | tee -a ~/Parallel-join/result/figure10.txt;