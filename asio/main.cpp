#include <boost/asio.hpp>
#include <iostream>
#include <iterator>
#include <algorithm>
#include <chrono>
#include <string>
#include <sstream>

std::string get_date_time()
{
    std::time_t now = std::chrono::system_clock::to_time_t(std::chrono::system_clock::now());

    std::string s(30, '\0');
    std::strftime(&s[0], s.size(), "%Y-%m-%d %H:%M:%S", std::localtime(&now));
    return s;
}

void run_sync()
{
    std::cout << get_date_time() + " - sync\n";

    boost::asio::io_context io_context;
    boost::asio::steady_timer t(io_context, boost::asio::chrono::seconds{3});

    t.wait();

    std::cout << get_date_time() + " - bye\n\n";
}

void print(const boost::system::error_code &e)
{
    std::cout << get_date_time() + " - print()\n";
}

void run_async()
{
    std::cout << get_date_time() + " - async\n";
    boost::asio::io_context io;
    boost::asio::steady_timer t(io, boost::asio::chrono::seconds{3});

    // Call the async
    t.async_wait(&print);

    io.run();

    std::cout << get_date_time() + " - bye\n\n";
}

void run_resolver()
{
    std::string url_to_resolve = "www.calpoly.edu";
    std::cout << "Running resolver for: " + url_to_resolve + "\n";

    boost::asio::io_context io_context;
    boost::asio::ip::tcp::resolver resolver{io_context};
    boost::system::error_code error_code;
    for (auto &&result : resolver.resolve(url_to_resolve, "http", error_code))
    {
        std::cout << result.service_name() << " "
                  << result.host_name() << " "
                  << result.endpoint() << "\n";
    }
    if (error_code)
        std::cout << "Error code: " << error_code << "\n";
}

int main()
{
    //run_sync();
    //run_async();

    run_resolver();

    return 0;
}
