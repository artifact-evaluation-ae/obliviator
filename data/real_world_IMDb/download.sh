#!/bin/bash -x

wget https://datasets.imdbws.com/name.basics.tsv.gz;
gzip -d name.basics.tsv.gz;