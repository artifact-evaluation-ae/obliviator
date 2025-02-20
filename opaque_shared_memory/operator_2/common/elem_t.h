#ifndef __COMMON_NODE_T_H
#define __COMMON_NODE_T_H

#include <assert.h>
#include <stddef.h>
#include <stdbool.h>
#include <stdint.h>

#define DATA_LENGTH 23

typedef int ojoin_int_type;

typedef struct elem {
    char data[DATA_LENGTH];
    bool dummy;
    float sum;
    int key;
} elem_t;

static_assert(sizeof(elem_t) == 32, "Element should be 32 bytes");

#endif /* common/elem_t.h */
