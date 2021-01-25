import Big from "big.js";

import operate from "./operate";
import isNumber from "./isNumber";


/**
 * Bior¹c pod uwagê nazwê przycisku i obiekt danych kalkulatora, zwróæ zaktualizowany obiekt danych kalkulatora.
 * Obiekt danych kalkulatora zawiera:
 * total: bierz¹ca liczba
 * next: Podaj nastêpn¹ liczbê do operacji
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
      // Jeœli jest nastêpna operacja zaktualizuj next jako nastêpn¹
    if (obj.operation) {
      if (obj.next) {
        return { next: obj.next + buttonName };
      }
      return { next: buttonName };
    }
    // Jeœli nie ma operacji zaktualizuj next i wyczyœæ wartoœæ
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
        //  zignoruj znak "." jeœli nastêpny numer ju¿ go ma
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
        //  „=” bez operacji nie rób nic
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

  // U¿ytkownik nacisn¹³ przycisk operacji i istnieje ju¿ operacja
  if (obj.operation) {
    return {
      total: operate(obj.total, obj.next, obj.operation),
      next: null,
      operation: buttonName,
    };
  }

    // nie ma jeszcze ¿adnej operacji, ale u¿ytkownik j¹ wpisa³

  // U¿ytkownik nie wpisa³ jeszcze numeru, po prostu zapisz operacjê
  if (!obj.next) {
    return { operation: buttonName };
  }

    // zapisz operacjê i zmieñ next na total
  return {
    total: obj.next,
    next: null,
    operation: buttonName,
  };
}
