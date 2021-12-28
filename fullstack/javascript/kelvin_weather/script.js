//constant variable "kelvin" of 293
const kelvin = 293

//celsius = 273 subtracted by kelvin
celsius = kelvin - 273

//fahrenheit is 32 + (9/5) * celsius
fahrenheit = celsius * (9/5) + 32
//.floor() will round down to a whole number
Math.floor(fahrenheit)

newton = celsius * (33/100)
Math.floor(newton)


console.log(`The temperature is ${fahrenheit} degrees Fahrenheit.`)
console.log(`The temperature is ${newton} on the Newton scale.`)
