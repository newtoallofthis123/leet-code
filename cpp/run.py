#!/usr/bin/env python3

import sys
import subprocess

prog = sys.argv[1]
if len(sys.argv) < 2:
    print("Please provide the name of the problem")
    sys.exit(1)

filename = prog + ".cpp"
subprocess.run(["g++", "-std=c++17", "-o", "./bin/" + prog, filename])
subprocess.run(["./bin/" + prog])
