#!/bin/bash  
python graphwriter.py
dot graph.dot -Tpng -o graph.png
NO_AT_BRIDGE=1 eog graph.png

