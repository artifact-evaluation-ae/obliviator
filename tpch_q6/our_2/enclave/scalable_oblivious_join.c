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
#include "enclave/bitonic.h"
#include "enclave/parallel_enc.h"
#include "enclave/threading.h"
//#include "enclave/bucket.h"
//#include "enclave/nonoblivious.h"

#ifndef DISTRIBUTED_SGX_SORT_HOSTONLY
#include <openenclave/enclave.h>
#include "enclave/parallel_t.h"
#endif

int tree_node_idx_48[48] = {63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62};
int tree_node_idx_6[6] = {7, 8, 9, 10, 5, 6};

static int number_threads;

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

// < -1
// == 0
// > 1
int o_strcmp(char* str1, char* str2) {
    bool flag = false;
    int result = 0;

    for (int i = 0; i < 16; i++) {
        result = !flag * (-1 * (str1[i] < str2[i]) + 1 * (str1[i] > str2[i])) + flag * result;
        flag = (!flag && ((str1[i] < str2[i]) || (str1[i] > str2[i]))) || flag;
    }

    return result;
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
    //aggregation_tree_init(number_threads);

    
    return 0;

}

void scalable_oblivious_join_free() {
    
    //aggregation_tree_free();
    //aligned_expand_free();
}

int o_strcmp_(volatile char* str1, volatile char* str2) {
    bool flag = false;
    int result = 0;

    for (int i = 0; i < 16; i++) {
        result = !flag * (-1 * (str1[i] < str2[i]) + 1 * (str1[i] > str2[i])) + flag * result;
        flag = (!flag && ((str1[i] < str2[i]) || (str1[i] > str2[i]))) || flag;
    }

    return result;
}

struct tree_node_op2 {
    volatile uint64_t key_first;
    volatile uint64_t key_last;
    volatile float sum_first;
    volatile float sum_last;
    volatile float sum_prefix;
    volatile float sum_suffix;
    volatile float sum_first2;
    volatile float sum_last2;
    volatile float sum_prefix2;
    volatile float sum_suffix2;
    volatile float sum_first3;
    volatile float sum_last3;
    volatile float sum_prefix3;
    volatile float sum_suffix3;
    volatile bool complete1;
    volatile bool complete2;
};

struct tree_node_op2* ag_tree;

void o_strcp_(volatile char* str1, volatile char* str2) {
    for (int i = 0; i < 16; i++) {
        str1[i] = str2[i];
    }
}

struct args_op2 {
    int index_thread_start;
    int index_thread_end;
    int *count;
    elem_t* arr;
    int thread_order;
};

void aggregation_tree_op2(void *voidargs) {
    struct args_op2 *args = (struct args_op2*) voidargs;
    int index_thread_start = args->index_thread_start;
    int index_thread_end = args->index_thread_end;
    elem_t* arr = args->arr;
    // int thread_order = args->thread_order;

    for (int i = index_thread_start; i < index_thread_end; i++) {
        arr[i].sum_adrevenue = arr[i].adrevenue * arr[i].discount;
    }

    return;

}

void scalable_oblivious_join(elem_t *arr, int length1, int length2, char* output_path){
    int length = length1;
    (void)length2;
    int* count = calloc(length, sizeof(*count));
    int length_thread = length / number_threads;
    int length_extra = length % number_threads;
    struct args_op2 args_op2_[number_threads];
    int idx_start_thread[number_threads + 1];
    idx_start_thread[0] = 0;
    struct thread_work multi_thread_aggregation_tree_1[number_threads - 1];
    ag_tree = calloc(2 * number_threads - 1, sizeof(*ag_tree));
    ag_tree[0].sum_prefix = 0;
    ag_tree[0].sum_suffix = 0;
    ag_tree[0].sum_prefix2 = 0;
    ag_tree[0].sum_suffix2 = 0;
    ag_tree[0].sum_prefix3 = 0;
    ag_tree[0].sum_suffix3 = 0;
    ag_tree[0].complete2 = true;
    init_time2();

    if (number_threads == 1) {
        for (int i = 0; i < length; i++) {
            arr[i].sum_adrevenue = arr[i].adrevenue * arr[i].discount;
        }
    } else {
        for (int i = 0; i < number_threads; i++) {
            idx_start_thread[i + 1] = idx_start_thread[i] + length_thread + (i < length_extra);

            args_op2_[i].arr = arr;
            args_op2_[i].count = count;
            args_op2_[i].index_thread_start = idx_start_thread[i];
            args_op2_[i].index_thread_end = idx_start_thread[i + 1];
            if (number_threads == 6) {
                args_op2_[i].thread_order = tree_node_idx_6[i];        
            } else if (number_threads == 48) {
                args_op2_[i].thread_order = tree_node_idx_48[i];
            } else {
                args_op2_[i].thread_order = number_threads + i - 1;
            }
            if (i < number_threads - 1) {
                multi_thread_aggregation_tree_1[i].type = THREAD_WORK_SINGLE;
                multi_thread_aggregation_tree_1[i].single.func = aggregation_tree_op2;
                multi_thread_aggregation_tree_1[i].single.arg = &args_op2_[i];
                thread_work_push(&multi_thread_aggregation_tree_1[i]);
            }
        }
        aggregation_tree_op2(&args_op2_[number_threads - 1]);
        for (int i = 0; i < number_threads - 1; i++) {
            thread_wait(&multi_thread_aggregation_tree_1[i]);
        }
    }

    get_time2(true);

    char *char_current = output_path;
    for (int i = 0; i < length; i++) {
        char revenue[20];
        int len2;
        sprintf(revenue, "%.2f", arr[i].sum_adrevenue);
        len2 = my_len(revenue);
        strncpy(char_current, revenue, len2);
        char_current += len2; char_current[0] = '\n'; char_current += 1;
    }
    char_current[0] = '\0';

    free(count);
    free(ag_tree);

    
    return ;
}