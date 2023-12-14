/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function (init) {
  let n = init;
  return {
    increment: () => {
      return ++n;
    },
    decrement: () => {
      return --n;
    },
    reset: () => {
      n = init;
      return n;
    },
  };
};

const counter = createCounter(5);
console.log(counter.increment()); // 6
console.log(counter.reset()); // 5
console.log(counter.decrement()); // 4
