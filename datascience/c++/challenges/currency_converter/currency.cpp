#include <iostream>

int main() {
  
  double pesos;
  double reais;
  double soles;
  double dollars;

  std::cout << "Enter number of Colombian Pesos: ";
  std::cin >> pesos;

  std::cout << "Enter number of Brazilian Reais: ";
  std::cin >> reais;

  std::cout << "Enter number of Peruvian Soles: ";
  std::cin >> soles;

  //pesos to usd: 0.00025
  //reais to usd: 0.20
  //soles to usd: 0.27

  dollars = (0.00025 * pesos) + (0.20 * reais) + (0.27 * soles);
  std::cout << "US Dollars = $" << dollars << "\n";
}
