#include <iostream>
#include <cmath>

int main() {
  
  double a;
  double b;
  double c;
  
  std::cout << "Enter a: ";
  std::cin >> a;

  std::cout << "Enter b: ";
  std::cin >> b;

  std::cout << "Enter c: ";
  std::cin >> c;


  double root1;
  double root2;

  root1 = (-b + std::sqrt((b * b) - 4 * a * c)) / (2 * a);
  root2 = (-b - std::sqrt((b * b) - 4 * a * c)) / (2 * a);

  std::cout << "Root 1: " << root1 << "\n";
  std::cout << "Root 2: " << root2 << "\n";

}
