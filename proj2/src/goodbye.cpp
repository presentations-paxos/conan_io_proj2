#include <proj1/hello.hpp>

#include <boost/format.hpp>
#include <sstream>

namespace proj2 {

    std::string goodbye(const std::string& name) {

        std::stringstream ss;
        ss << boost::format("Goodbye, %s") % name;

        return ss.str();
    }
}
