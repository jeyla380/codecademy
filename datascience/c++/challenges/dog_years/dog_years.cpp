#include <iostream>
#include <string>
using namespace std;

int main() {
  
  //dog's age in years
  int dog_age = 3;
  int early_years, later_years, human_years;

  //first 2 years of a dog's life = 21 human years
  early_years = 21;

  //each of the following years count as 4 human years
  later_years = (dog_age - 2) * 4;

  human_years = early_years + later_years;

  string dog_name;
  cout << "What is your dog's name: ";
  getline (cin, dog_name);

  cout << "My name is " << dog_name << "! Ruff ruff, I am " << human_years << " years old in human years.\n";

}
