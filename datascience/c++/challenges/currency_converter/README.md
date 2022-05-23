### C++ Code
``` c++
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
```

### Bash Code

```
$ g++ currency.cpp
$ ./a.out
```
The user will be prompted to enter the number of Colombian Pesos, Brazilian Reais, and Peruvian Soles (we will use 5, 4, and 3 in the example). Then the results will be converted into USD.
```
Enter number of Colombian Pesos: 5
Enter number of Brazilian Reais: 4
Enter number of Peruvian Soles: 3
US Dollars = $1.61125
```
