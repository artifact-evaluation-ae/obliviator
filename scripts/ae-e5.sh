#!/bin/bash -x

cd ~/obliviator/operator_3/3_1/;
make clean; make;
./host/parallel ./enclave/parallel_enc.signed 1 ~/obliviator/data/big_data_benchmark/bdb_query3_partA_step1_input.txt;
make clean;

cd ~/obliviator/operator_3/3_2/;
make clean; make;
./host/parallel ./enclave/parallel_enc.signed 1 ~/obliviator/data/big_data_benchmark/bdb_query3_step2_sample_input.txt;
make clean;

cd ~/obliviator/operator_3/3_3/;
make clean; make;
./host/parallel ./enclave/parallel_enc.signed 1 ~/obliviator/data/big_data_benchmark/bdb_query3_step3_sample_input.txt;
make clean;

cd ~/obliviator/opaque_shared_memory/operator_3/3_1/;
make clean; make;
./host/parallel ./enclave/parallel_enc.signed 1 ~/obliviator/data/big_data_benchmark/bdb_query3_partA_step1_input.txt;
make clean;

cd ~/obliviator/opaque_shared_memory/operator_3/3_2/;
make clean; make;
./host/parallel ./enclave/parallel_enc.signed 1 ~/obliviator/data/big_data_benchmark/bdb_query3_step2_sample_input.txt;
make clean;

cd ~/obliviator/opaque_shared_memory/operator_3/3_3/;
make clean; make;
./host/parallel ./enclave/parallel_enc.signed 1 ~/obliviator/data/big_data_benchmark/bdb_query3_step3_sample_input.txt;
make clean;