/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */

// Using a for loop with operational container
// TC and SC: O(n)
var map = function (arr, fn) {
  const newArray = []; //operational container
  for (let i = 0; i < arr.length; i++) {
    newArray[i] = fn(arr[i], i);
  }
  return newArray;
};

// Using a for loop without any container a.k.a Inmemory transformations
// This is a bad practice as it alters the given data
// and also It can result in unexpected problems
// where the programmer was not expecting that as a side-effect.
// TC and SC : O(n) and O(1)
var map = function (arr, fn) {
  for (let i = 0; i < arr.length; ++i) {
    arr[i] = fn(arr[i], i);
  }
  return arr;
};
