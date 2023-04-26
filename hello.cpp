#include <iostream>
#include <gsl/gsl_sf_bessel.h>

#include "primitives.hpp"

int main() {
    std::cout << "Hello!" << std::endl;
    std::cout << "J0(0) = " << gsl_sf_bessel_J0(0) << std::endl;
    Int a = 40;
    Int b = 2;
    Int c = 0;
    add(a, b, c);
    std::cout << "a + b = " << c << std::endl;
    std::cout << "sizeof(Int) = " << sizeof(Int) << std::endl;
    std::cout << "sizeof(Float) = " << sizeof(Float) << std::endl;
    Float u = 40.02;
    Float v = 2.4;
    Float w = 0;
    add(u, v, w);
    std::cout << "u + v = " << w << std::endl;
    return 0;
}
