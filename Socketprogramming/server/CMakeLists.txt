cmake_minimum_required(VERSION 3.10.2)

set (CMAKE_CXX_STANDARD 11)

project(server)

add_executable(${PROJECT_NAME} server.cpp)

