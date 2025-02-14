#ifndef __COMMON_NODE_T_H
#define __COMMON_NODE_T_H

#include <assert.h>
#include <stddef.h>
#include <stdbool.h>
#include <stdint.h>

#define ELEM_SIZE 256
#define ELEM_STRUCT_SIZE 19
#define DATA_LENGTH 234
#define KEY_LENGTH 10

typedef int ojoin_int_type;

typedef struct elem {
    char data[234];
    char true_key[13];
    bool has_value;
    int key; // for sort only
    int unused_1;

} elem_t;

static_assert(sizeof(elem_t) == ELEM_SIZE, "Element should be 256 bytes");

#endif /* common/elem_t.h */
