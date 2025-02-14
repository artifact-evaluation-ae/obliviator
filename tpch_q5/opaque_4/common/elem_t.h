#ifndef __COMMON_NODE_T_H
#define __COMMON_NODE_T_H

#include <assert.h>
#include <stddef.h>
#include <stdbool.h>
#include <stdint.h>

#define ELEM_SIZE 32
#define ELEM_STRUCT_SIZE 19
#define DATA_LENGTH 305
#define max_output_bytes 1073741824

typedef int ojoin_int_type;

typedef struct elem {
    char unused[12];
    float discount; // discount
    uint64_t key; // groupby key
    float adrevenue; // extended price
    float sum_adrevenue; // sum result, for second sort, 2nd printout
    // float ship_priority; // forth printout
    // int order_key; // first printout
    // int order_date; // for second sort, 3rd printout
} elem_t;

typedef struct ele2m {
    ojoin_int_type key;
    unsigned char data[4];

    /* Oblivious join stuff*/
    bool has_value;
    bool table_0;

    /* Florian's join */
    ojoin_int_type m0;
    ojoin_int_type m1;
    ojoin_int_type true_key;
    ojoin_int_type idx_start;
    ojoin_int_type j_order;

    //unsigned char unused[ELEM_SIZE - ELEM_STRUCT_SIZE];
} ele2m_t;

static_assert(sizeof(elem_t) == ELEM_SIZE, "Element should be 64 bytes");

#endif /* common/elem_t.h */
