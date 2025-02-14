#ifndef __COMMON_NODE_T_H
#define __COMMON_NODE_T_H

#include <assert.h>
#include <stddef.h>
#include <stdbool.h>
#include <stdint.h>

#define ELEM_SIZE 256
#define ELEM_STRUCT_SIZE 19
#define DATA_LENGTH 224

typedef int ojoin_int_type;

typedef struct elem {
    // char data[247];
    // bool has_value;
    // for sort only
    // int true_key;

    // bool has_value;
    // int key;
    char region[19];
    bool unused;
    int key;
    int c_nationkey;
    int s_nationkey;
    char data[DATA_LENGTH];
} elem_t;

static_assert(sizeof(elem_t) == ELEM_SIZE, "Element should be 128 bytes");

#endif /* common/elem_t.h */
