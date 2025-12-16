#include "greeter.hpp"
#include <fmt/core.h>

std::string greet(const std::string& name) {
    return fmt::format("Hello, {}!", name);
}
