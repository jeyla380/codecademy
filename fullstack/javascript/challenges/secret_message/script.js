let secretMessage = ['Learning', 'is', 'not', 'about', 'what', 'you', 'get', 'easily', 'the', 'first', 'time,', 'it', 'is', 'about', 'what', 'you', 'can', 'figure', 'out.', '-2015,', 'Chris', 'Pine,', 'Learn', 'JavaScript'];

secretMessage.pop();
//console.log(secretMessage);
console.log(secretMessage.length);

secretMessage.push('to', 'Program');
//console.log(secretMessage);

rightWord = secretMessage.indexOf('easily');
//console.log(rightWord);
secretMessage[rightWord] = "right";
//console.log(secretMessage);

secretMessage.shift();
//console.log(secretMessage);

secretMessage.unshift("Programming");
//console.log(secretMessage);

//starts at index 6, gets rid of the 5 indices and replaces the empty space with "know,"
secretMessage.splice(6, 5, "know,");
//console.log(secretMessage);

//.join gets rid of the array, and turns the ',' into spaces (" ").
console.log(secretMessage.join(" "));
