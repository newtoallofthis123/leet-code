#!/usr/bin/env python3

import sys

boiler_plate = """
#include <iostream>
using namespace std;

int main(){
  auto solution = Solution();
}
"""

if len(sys.argv) < 2:
    print("Please provide the name of the problem")
    sys.exit(1)
arg = sys.argv[1]

filename = arg + ".cpp"
with open(filename, "w") as f:
    f.write(boiler_plate)

f.close()
