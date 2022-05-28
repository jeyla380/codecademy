### C++ Code:
``` c++
#include <iostream>

int main()
{
  int gryffindor = 0;
  int hufflepuff = 0;
  int ravenclaw = 0;
  int slytherin = 0;

  int answer1;
  int answer2;
  int answer3;
  int answer4;

  std::cout << "The Sorting Hat Quiz!\n";
  std::cout << "------------------------------------------\n";
  std::cout << "\n";

  std::cout << "Q1) When I'm dead, I want people to remember me as: \n";
  std::cout << "     1) The Good\n";
  std::cout << "     2) The Great\n";
  std::cout << "     3) The Wise\n";
  std::cout << "     4) The Bold\n";
  std::cout << "Answer: ";
  std::cin >> answer1;
  std::cout << "\n";

  switch (answer1)
  {
    case 1:
      hufflepuff++;
      break;
    case 2:
      slytherin++;
      break;
    case 3:
      ravenclaw++;
      break;
    case 4:
      gryffindor++;
      break;
    default:
      std::cout << "Invalid input\n";
      break;
  }


  std::cout << "Q2) Dawn or Dusk?\n";
  std::cout << "     1) Dawn\n";
  std::cout << "     2) Dusk\n";
  std::cout << "Answer: ";
  std::cin >> answer2;
  std::cout << "\n";

  if(answer2 == 1)
  {
    gryffindor++;
    ravenclaw++;
  }
  else if(answer2 == 2)
  {
    hufflepuff++;
    slytherin++;
  }
  else
  {
    std::cout << "Invalid input\n";
  }


  std::cout << "Q3) Which kind of instrument most pleases your ear?\n";
  std::cout << "     1) The violin\n";
  std::cout << "     2) The trumpet\n";
  std::cout << "     3) The piano\n";
  std::cout << "     4) The drum\n";
  std::cout << "Answer: ";
  std::cin >> answer3;
  std::cout << "\n";

  switch(answer3)
  {
    case 1:
      slytherin++;
      break;
    case 2:
      hufflepuff++;
      break;
    case 3:
      ravenclaw++;
      break;
    case 4:
      gryffindor++;
      break;
    default:
      std::cout << "Invalid input";
      break;
  }


  std::cout << "Q4) Which road tempts you most?\n";
  std::cout << "     1) The wide, sunny grassy lane\n";
  std::cout << "     2) The narrow, dark, lantern-lit alley\n";
  std::cout << "     3) The twisting, leaf-strewn path through woods\n";
  std::cout << "     4) The cobbled street lined (ancient buildings)\n";
  std::cout << "Answer: ";
  std::cin >> answer4;
  std::cout << "\n";

  switch(answer4)
  {
    case 1:
      hufflepuff++;
      break;
    case 2:
      slytherin++;
      break;
    case 3:
      gryffindor++;
      break;
    case 4:
      ravenclaw++;
      break;
    default:
      std::cout << "Invalid input";
      break;
  }


  int max = 0;
  std::string house;

  if(gryffindor > max)
  {
    max = gryffindor;
    house = "Gryffindor";
  }
  
  if(hufflepuff > max)
  {
    max = hufflepuff;
    house = "Hufflepuff";
  }

  if(ravenclaw > max)
  {
    max = ravenclaw;
    house = "Ravenclaw";
  }

  if (slytherin > max)
  {
    max = slytherin;
    house = "Slytherin";
  }

  std::cout << "You will be placed in " << house << "!\n";
}
```

### Bash Code:
```
$ g++ sortinghat.cpp
$ ./a.out
```
The quiz will be initiated after typing out the code above. (I'll be using an example to show to final outcome.)
```
The Sorting Hat Quiz!
------------------------------------------

Q1) When I'm dead, I want people to remember me as:
     1) The Good
     2) The Great
     3) The Wise
     4) The Bold
Answer: 3

Q2) Dawn or Dusk?
     1) Dawn
     2) Dusk
Answer: 1

Q3) Which kind of instrument most pleases your ear?
     1) The violin
     2) The trumpet
     3) The piano
     4) The drum
Answer: 3

Q4) Which road tempts you most?
     1) The wide, sunny grassy lane
     2) The narrow, dark, lantern-lit alley
     3) The twisting, leaf-strewn path through woods
     4) The cobbled street lined (ancient buildings)
Answer: 1

You will be placed in Ravenclaw!
```
