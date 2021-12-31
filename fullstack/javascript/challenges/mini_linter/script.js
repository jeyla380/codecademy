let story = 'Last weekend, I took literally the most beautiful bike ride of my life. The route is called "The 9W to Nyack" and it actually stretches all the way from Riverside Park in Manhattan to South Nyack, New Jersey. It\'s really an adventure from beginning to end! It is a 48 mile loop and it basically took me an entire day. I stopped at Riverbank State Park to take some extremely artsy photos. It was a short stop, though, because I had a really long way left to go. After a quick photo op at the very popular Little Red Lighthouse, I began my trek across the George Washington Bridge into New Jersey.  The GW is actually very long - 4,760 feet! I was already very tired by the time I got to the other side.  An hour later, I reached Greenbrook Nature Sanctuary, an extremely beautiful park along the coast of the Hudson.  Something that was very surprising to me was that near the end of the route you actually cross back into New York! At this point, you are very close to the end.';

let overusedWords = ['really', 'very', 'basically'];
let unnecessaryWords = ['extremely', 'literally', 'actually' ];


var storyWords = story.split(' ');
//console.log(storyWords);
console.log(storyWords.length);


var betterWords = storyWords.filter(word => {
  return !(unnecessaryWords.includes(word));
});
console.log(betterWords);


var commonWords = storyWords.filter(word => {
  return overusedWords.includes(word);
});
console.log(commonWords);


reallyWord = [];
basicallyWord = [];
veryWord = [];
for(var i = 0; i < commonWords.length; i++)
{
  if(commonWords[i] == 'really')
  {
    reallyWord.push(commonWords[i]);
  }
  else if(commonWords[i] == 'basically')
  {
    basicallyWord.push(commonWords[i]);
  }
  else if(commonWords[i] == 'very')
  {
    veryWord.push(commonWords[i]);
  }
}
//console.log(reallyWord);
//console.log(basicallyWord);
//console.log(veryWord);
console.log(reallyWord.length);
console.log(basicallyWord.length);
console.log(veryWord.length);


sentences = 0;
betterWords.forEach(word => {
  if(word[word.length - 1] == "." || word[word.length - 1] == '!')
  {
    //console.log(word);
    sentences += 1;
  }
});
console.log(sentences);


function logItems()
{
  return 'Word Count: ' + betterWords.length + "\nSentence Count: " + sentences + '\nCount of Overused Words: \n   - Really: ' + reallyWord.length + "\n   - Basically: " + basicallyWord.length + '\n   - Very: ' + veryWord.length;
}
console.log(logItems());


console.log(betterWords.join(' '));
