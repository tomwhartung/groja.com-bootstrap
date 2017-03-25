#!/bin/bash
#
#  Create and print the db
#
python3 -m db_create
python3 -c "from db_access import print_table ; print_table()"
