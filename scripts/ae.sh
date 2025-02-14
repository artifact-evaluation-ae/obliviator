#!/bin/bash -x

echo "Start compilation...";
cd ~/obliviator/join/;
make clean; make;
cd ~/obliviator/join_kks/;
make clean; make;
cd ~/obliviator/fk_join/;
make clean; make;
cd ~/obliviator/opaque_shared_memory/fk_join;
make clean; make;
cd ~/obliviator/operator_1;
make clean; make;
cd ~/obliviator/opaque_shared_memory/operator_1;
make clean; make;
cd ~/obliviator/operator_2;
make clean; make;
cd ~/obliviator/opaque_shared_memory/operator_2;
make clean; make;
cd ~/obliviator/operator_3/3_1/;
make clean; make;
cd ~/obliviator/operator_3/3_2/;
make clean; make;
cd ~/obliviator/operator_3/3_3/;
make clean; make;
cd ~/obliviator/opaque_shared_memory/operator_3/3_1/;
make clean; make;
cd ~/obliviator/opaque_shared_memory/operator_3/3_2/;
make clean; make;
cd ~/obliviator/opaque_shared_memory/operator_3/3_3/;
make clean; make;


echo "Start running...";
cd ~/obliviator/join/;
./host/parallel ./enclave/parallel_enc.signed 1 ./test.txt;
cd ~/obliviator/join_kks/;
./app ./output.txt ./test.txt;
echo "Complete (E1) NFK Join";

cd ~/obliviator/fk_join/;
./host/parallel ./enclave/parallel_enc.signed 1 ./test.txt;
cd ~/obliviator/opaque_shared_memory/fk_join/;
./host/parallel ./enclave/parallel_enc.signed 1 ./test.txt;
echo "Complete (E2) FK Join";

cd ~/obliviator/operator_1/;
./host/parallel ./enclave/parallel_enc.signed 1 ./test.txt;
cd ~/obliviator/opaque_shared_memory/operator_1/;
./host/parallel ./enclave/parallel_enc.signed 1 ./test.txt;
echo "Complete (E3) Filter";

cd ~/obliviator/operator_2/;
./host/parallel ./enclave/parallel_enc.signed 1 ./test.txt;
cd ~/obliviator/opaque_shared_memory/operator_2/;
./host/parallel ./enclave/parallel_enc.signed 1 ./test.txt;
echo "Complete (E4) Aggregation";

cd ~/obliviator/operator_3/3_1/;
./host/parallel ./enclave/parallel_enc.signed 1 ~/obliviator/data/big_data_benchmark/bdb_query3_partA_step1_input.txt;
cd ~/obliviator/operator_3/3_2/;
./host/parallel ./enclave/parallel_enc.signed 1 ~/obliviator/data/big_data_benchmark/bdb_query3_step2_sample_input.txt;
cd ~/obliviator/operator_3/3_3/;
./host/parallel ./enclave/parallel_enc.signed 1 ~/obliviator/data/big_data_benchmark/bdb_query3_step3_sample_input.txt;

cd ~/obliviator/opaque_shared_memory/operator_3/3_1/;
./host/parallel ./enclave/parallel_enc.signed 1 ~/obliviator/data/big_data_benchmark/bdb_query3_partA_step1_input.txt;
cd ~/obliviator/opaque_shared_memory/operator_3/3_2/;
./host/parallel ./enclave/parallel_enc.signed 1 ~/obliviator/data/big_data_benchmark/bdb_query3_step2_sample_input.txt;
cd ~/obliviator/opaque_shared_memory/operator_3/3_3/;
./host/parallel ./enclave/parallel_enc.signed 1 ~/obliviator/data/big_data_benchmark/bdb_query3_step3_sample_input.txt;
echo "Complete (E5) Complex Query";