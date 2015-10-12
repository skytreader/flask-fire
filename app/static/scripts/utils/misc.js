/**
A collection of miscellaneous JavaScript functions that can be (potentially)
used anywhere.

@author Chad Estioco
*/

/**
Add a function like Python's capitalize to JavaScript strings.
*/
String.prototype.capitalize = function(){
    return this.charAt(0).toUpperCase() + this.slice(1);
}

var Random = {};

/**
Get a random number in the range [min, max).
*/
Random.getRandomInterval(min, max){
    return Math.random() * (max - min) + min;
}

/**
Get a random integer in the range [min, max).
*/
Random.getRandomInt(min, max){
    return Math.floor(Random.getInterval(min, max));
}

/**
Get  random integer in the range [min, max].
*/
Random.getRandomIntInclusive(min, max){
    return Math.floor(Math.random() * (max - min + 1) + min);
}

/**
Chooses a random element in the given array.
*/
Random.choice(a){
    return a[Random.getRandomInt(0, a.length)];
}
