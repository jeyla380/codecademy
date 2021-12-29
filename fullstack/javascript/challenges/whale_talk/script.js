var input = "i like to eat oranges and udon noodles";
var vowels = ["a", "e", "i", "o", "u"]; //won't be adding "y"
var resultArray = [];

for(var i = 0; i < input.length; i++)
{
  //console.log(input[i]);
  for(var j = 0; j < vowels.length; j++)
  {
    //console.log(vowels[j]); //this will print "a, e, i, o, u" for every letter in input.
    if(input[i] == vowels[j])
    {
      //console.log(input[i]);
      if(input[i] == "e" || input[i] == "u")
      {
        resultArray.push(input[i]);
      }
    }
  }
}
//console.log(resultArray);
console.log(resultArray.join('').toUpperCase());
