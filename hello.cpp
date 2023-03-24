#include <iostream>
#include <gsl/gsl_sf_bessel.h>

int main() {
    std::cout << "Hello!" << std::endl;
    std::cout << gsl_sf_bessel_J0(0) << std::endl;
    return 0;
}
