cmake_minimum_required(VERSION 3.0.0)
project(linklist01 VERSION 0.1.0)

include(CTest)
enable_testing()
add_executable(linklist01 main.cpp)

find_package(fmt CONFIG REQUIRED)
target_link_libraries(${PROJECT_NAME} PRIVATE fmt::fmt-header-only)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
