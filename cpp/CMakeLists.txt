cmake_minimum_required(VERSION 3.27)
project(cpp)

set(CMAKE_CXX_STANDARD 17)

add_executable(cpp main.cpp
        longest_palindromic_substring.cpp
        longest_common_prefix.cpp
        two_sum.cpp
)
