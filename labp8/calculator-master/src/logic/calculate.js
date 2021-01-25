import Big from "big.js";

import operate from "./operate";
import isNumber from "./isNumber";


/**
 * Bior�c pod uwag� nazw� przycisku i obiekt danych kalkulatora, zwr�� zaktualizowany obiekt danych kalkulatora.
 * Obiekt danych kalkulatora zawiera:
 * total: bierz�ca liczba
 * next: Podaj nast�pn� liczb� do operacji
 * operacja: +, - ...
 */
export default function calculate(obj, buttonName) {
  if (buttonName === "AC") {
    return {
      total: null,
      next: null,
      operation: null,
    };
  }

  if (isNumber(buttonName)) {
    if (buttonName === "0" && obj.next === "0") {
      return {};
    }
      // Je�li jest nast�pna operacja zaktualizuj next jako nast�pn�
    if (obj.operation) {
      if (obj.next) {
        return { next: obj.next + buttonName };
      }
      return { next: buttonName };
    }
    // Je�li nie ma operacji zaktualizuj next i wyczy�� warto��
    if (obj.next) {
      const next = obj.next === "0" ? buttonName : obj.next + buttonName;
      return {
        next,
        total: null,
      };
    }
    return {
      next: buttonName,
      total: null,
    };
  }

  if (buttonName === "%") {
    if (obj.operation && obj.next) {
      const result = operate(obj.total, obj.next, obj.operation);
      return {
        total: Big(result)
          .div(Big("100"))
          .toString(),
        next: null,
        operation: null,
      };
    }
    if (obj.next) {
      return {
        next: Big(obj.next)
          .div(Big("100"))
          .toString(),
      };
    }
    return {};
  }

  if (buttonName === ".") {
    if (obj.next) {
        //  zignoruj znak "." je�li nast�pny numer ju� go ma
      if (obj.next.includes(".")) {
        return {};
      }
      return { next: obj.next + "." };
    }
    return { next: "0." };
  }

  if (buttonName === "=") {
    if (obj.next && obj.operation) {
      return {
        total: operate(obj.total, obj.next, obj.operation),
        next: null,
        operation: null,
      };
    } else {
        //  �=� bez operacji nie r�b nic
      return {};
    }
  }

  if (buttonName === "+/-") {
    if (obj.next) {
      return { next: (-1 * parseFloat(obj.next)).toString() };
    }
    if (obj.total) {
      return { total: (-1 * parseFloat(obj.total)).toString() };
    }
    return {};
  }

  // U�ytkownik nacisn�� przycisk operacji i istnieje ju� operacja
  if (obj.operation) {
    return {
      total: operate(obj.total, obj.next, obj.operation),
      next: null,
      operation: buttonName,
    };
  }

    // nie ma jeszcze �adnej operacji, ale u�ytkownik j� wpisa�

  // U�ytkownik nie wpisa� jeszcze numeru, po prostu zapisz operacj�
  if (!obj.next) {
    return { operation: buttonName };
  }

    // zapisz operacj� i zmie� next na total
  return {
    total: obj.next,
    next: null,
    operation: buttonName,
  };
}
