import Big from "big.js";

//działanie operatorów

export default function operate(numberOne, numberTwo, operation) {
  const one = Big(numberOne || "0");
  const two = Big(numberTwo || (operation === "÷" || operation === 'x' ? "1": "0")); 
  if (operation === "+") {
    return one.plus(two).toString();
  }
  if (operation === "-") {
    return one.minus(two).toString();
  }
  if (operation === "x") {
    return one.times(two).toString();
  }
  if (operation === "÷") {
    if (two === "0") {
      alert("Divide by 0 error");
      return "0";
    } else {
      return one.div(two).toString();
    }
  }
    if (operation === "mod") {
        return one.mod(two).toString();
    }
    if (operation === "sqrt") {
        return one.sqrt().toString();
    }
    if (operation === "^") {
        return one.pow(2).toString();
    }
  throw Error(`Unknown operation '${operation}'`);
}
