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

/**
 * Use closure to retain the counter value between function calls.
 * The reason for holding the value of init in another variable is to preserve the value of the initial init.
 * If we don't, init will keep changing when we execute increment and decrement.
 * Then, when reset is executed, the initial init will not be returned.
 */

/**
 * JS의 클로저에 관한 문제인 것 같다.
여기서 init의 값을 다른 변수에 담아두는 이유는 초기 init의 값을 보존하기위해서다. 담아두지 않게되면 increment, decrement 실행시 init이 계속 변하게된다. 그러면 reset실행시 초기 init을 리턴하지 못하게 된다.
초기 init값을 보존하고 다른 변수를 통해 계산을 실행시키면된다.
 */
