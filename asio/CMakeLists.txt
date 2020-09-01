cmake_minimum_required(VERSION 3.0.0)
set (CMAKE_CXX_STANDARD 17)
project(HelloBoost VERSION 0.1.0)

include(CTest)
enable_testing()

add_executable(HelloBoost main.cpp)

set(BOOST_ROOT "/usr/local/homebrew/opt/boost/include")
set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)

find_package(Boost 1.72.0 COMPONENTS thread regex system)
if(Boost_FOUND)
  include_directories(${Boost_INCLUDE_DIRS})
  target_link_libraries(${PROJECT_NAME} ${Boost_THREAD_LIBRARY} ${Boost_REGEX_LIBRARY} ${Boost_SYSTEM_LIBRARY})
endif()