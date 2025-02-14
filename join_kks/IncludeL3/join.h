#ifdef SUBTIME
#include <time.h>
#endif
#include "layout.h"
#include "sort.h"
#include "trace_mem.h"
#include "db_primitives.h"

#define TIME_VAL ((clock() - begin) / (float)CLOCKS_PER_SEC)

void join(Table &t, Table &t0, Table &t1) {
    int n1 = t0.data.size, n2 = t1.data.size;
    int n = n1 + n2;

    #ifdef SUBTIME
    clock_t begin = clock();
    #endif
    
    bitonic_sort<Table::TableEntry, Table::attr_comp>(&t.data);

    int output_size = write_block_sizes(n, t);
    
    bitonic_sort<Table::TableEntry, Table::tid_comp>(&t.data);
    
    #ifdef SUBTIME
    printf("Sorting concatenated table twice: %.2fs\n", TIME_VAL);
    #endif

    for (int i = 0; i < n1; i++) {
        Table::TableEntry e = t.data.read(i);
        t0.data.write(i, e);
    }
    obliv_expand<Table::entry_width>(&t0.data);
    
    for (int i = 0; i < n2; i++) {
        Table::TableEntry e = t.data.read(n1 + i);
        t1.data.write(i, e);
    }
    obliv_expand<Table::entry_height>(&t1.data);

    assert(t0.data.size == output_size);
    assert(t1.data.size == output_size);
    
    #ifdef SUBTIME
    begin = clock();
    #endif
    
    bitonic_sort<Table::TableEntry, Table::t1_comp>(&t1.data);

    #ifdef SUBTIME
    printf("Sorting second expanded table: %.2fs\n", TIME_VAL);
    #endif

}
