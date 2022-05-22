### C++ Code

```C++
#include <iostream>

int main() {
  
  double tempf;
  double tempc;
  
  // Ask the user
  std::cout << "Enter the temperature in Fahrenheit: ";
  std::cin >> tempf;
  
  tempc = (tempf - 32) / 1.8;
  
  std::cout << "The temp is " << tempc << " degrees Celsius.\n";
  
}
```


### Bash Code

```
$ g++ temperature.cpp
$ ./a.out
```
This will prompt the user for the temperature in Fahrenheit (83 is used for the example), then will show the result of the degrees in Celsius.
```
Enter the temperature in Fahrenheit: 83
The temp is in 28.3333 degrees Celsius.
```
