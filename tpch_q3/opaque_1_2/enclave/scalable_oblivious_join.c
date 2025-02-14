#include "enclave/scalable_oblivious_join.h"
#include <limits.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdio.h>
#include <stdarg.h>
#include <threads.h>
#include <liboblivious/algorithms.h>
#include <liboblivious/primitives.h>
#include "common/elem_t.h"
#include "common/error.h"
#include "common/util.h"
#include "common/ocalls.h"
#include "common/code_conf.h"
#include "enclave/mpi_tls.h"
#include "enclave/parallel_enc.h"
#include "enclave/threading.h"
#include "enclave/bitonic.h"

#ifndef DISTRIBUTED_SGX_SORT_HOSTONLY
#include <openenclave/enclave.h>
#include "enclave/parallel_t.h"
#endif



static int number_threads;
//static bool *control_bit;
int res_thread[100];

#define MAX_DUMMY_ORDER 2147480000

void reverse(char *s) {
    int i, j;
    char c;

    for (i = 0, j = strlen(s)-1; i<j; i++, j--) {
        c = s[i];
        s[i] = s[j];
        s[j] = c;
    }
}

int my_len(char *data) {
    int i = 0;

    while ((data[i] != '\0') && (i < DATA_LENGTH)) i++;
    
    return i;
}

void itoa(int n, char *s, int *len) {
    int i = 0;
    int sign;

    if ((sign = n) < 0) {
        n = -n;
        i = 0;
    }
        
    do {
        s[i++] = n % 10 + '0';
    } while ((n /= 10) > 0);
    
    if (sign < 0)
        s[i++] = '-';
    s[i] = '\0';
    
    *len = i;
    
    reverse(s);
}

int scalable_oblivious_join_init(int nthreads) {

    number_threads = nthreads;
    return 0;

}

void scalable_oblivious_join_free() {
    return;
}


struct soj_scan_1_args {
    int idx_st;
    int idx_ed;
    elem_t *arr1;
    int thread_order;
};


void soj_scan_1(void *voidargs) {
    struct soj_scan_1_args *args = (struct soj_scan_1_args*)voidargs;
    int index_start = args->idx_st;
    int index_end = args->idx_ed;
    //bool* cb1 = args->control_bit;
    elem_t *arr1 = args->arr1;
    int thread_order = args->thread_order;

    for (int i = index_start; i < index_end; i++) {
        //cb1[i] = (88 < arr1[i].key);
        arr1[i].key = (arr1[i].true_key < 19950315) * i + (19950315 <= arr1[i].true_key) * MAX_DUMMY_ORDER;
        res_thread[thread_order] += (arr1[i].true_key < 19950315);
    }

    return;
}


void scalable_oblivious_join(elem_t *arr, int length1, int length2, char* output_path){
    for (int i = 0; i < number_threads; i++) res_thread[i] = 0;
    (void)length2;
    int length_result = 0;
    int length_thread = length1 / number_threads;
    int length_extra = length1 % number_threads;
    struct soj_scan_1_args soj_scan_1_args_[number_threads];
    int index_start_thread[number_threads + 1];
    index_start_thread[0] = 0;
    struct thread_work soj_scan_1_[number_threads - 1];
    init_time2();

    if (number_threads == 1) {
        for (int i = 0; i < length1; i++) {
            arr[i].key = 1 - (arr[i].true_key < 19950315);
            length_result += (arr[i].true_key < 19950315);
        }
    } else {
        for (int i = 0; i < number_threads; i++) {
            index_start_thread[i + 1] = index_start_thread[i] + length_thread + (i < length_extra);
        
            soj_scan_1_args_[i].idx_st = index_start_thread[i];
            soj_scan_1_args_[i].idx_ed = index_start_thread[i + 1];
            soj_scan_1_args_[i].arr1 = arr;
            soj_scan_1_args_[i].thread_order = i;

            if (i < number_threads - 1) {
                soj_scan_1_[i].type = THREAD_WORK_SINGLE;
                soj_scan_1_[i].single.func = soj_scan_1;
                soj_scan_1_[i].single.arg = soj_scan_1_args_ + i;
                thread_work_push(soj_scan_1_ + i);
            }
        }
        soj_scan_1(soj_scan_1_args_ + number_threads - 1);
        for (int i = 0; i < number_threads; i++) {
            if (i < number_threads - 1) {
                thread_wait(soj_scan_1_ + i);
            };
        }
        for (int i = 0; i < number_threads; i++) {
            length_result += res_thread[i];
        }
    }

    bitonic_sort(arr, true, 0, length1, number_threads);

    get_time2(true);

    char *char_current = output_path;
    for (int i = 0; i < length_result; i++) {
        int data_len1 = my_len(arr[i].data);
        strncpy(char_current, arr[i].data, data_len1);
        char_current += data_len1; char_current[0] = '\n'; char_current += 1;
    }
    char_current[0] = '\0';

    return;
}