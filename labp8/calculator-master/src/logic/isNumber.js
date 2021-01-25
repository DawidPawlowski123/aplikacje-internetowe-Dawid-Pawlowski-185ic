//Sprawdza czy podany element jest liczb¹
export default function isNumber(item) {
  return /[0-9]+/.test(item);
}
