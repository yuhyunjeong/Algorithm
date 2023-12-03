/**
 * @param {string} val
 * @return {Object}
 */
var expect = function (val) {
  return {
    toBe: (val2) => {
      if (val !== val2) throw new Error("Not Equal");
      else return true;
    },

    notToBe: (val2) => {
      if (val == val2) throw new Error("Equal");
      else return true;
    },
  };
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */

// The == and === operators in JavaScript are comparison operators that we use to determine if two values are equal or not.
// The == operator performs a loose equality comparison that performs type coercion if necessary to make the comparison possible.
// The === operator, on the other hand, performs a strict equality comparison that does not perform type coercion and requires the operands to have the same type (as well as the same value).
