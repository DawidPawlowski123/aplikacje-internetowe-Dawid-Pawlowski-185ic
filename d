warning: LF will be replaced by CRLF in labp8/calculator-master/src/component/Button.js.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in labp8/calculator-master/src/component/ButtonPanel.js.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in labp8/calculator-master/src/logic/calculate.js.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in labp8/calculator-master/src/logic/calculate.test.js.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in labp8/calculator-master/src/logic/isNumber.js.
The file will have its original line endings in your working directory
[1mdiff --git a/labp8/calculator-master/src/component/Button.js b/labp8/calculator-master/src/component/Button.js[m
[1mindex 0fe78c7..bea32de 100644[m
[1m--- a/labp8/calculator-master/src/component/Button.js[m
[1m+++ b/labp8/calculator-master/src/component/Button.js[m
[36m@@ -1,7 +1,7 @@[m
 import React from "react";[m
 import PropTypes from "prop-types";[m
 import "./Button.css";[m
[31m-[m
[32m+[m[32m//komponenty i ich w≥asnosci[m
 export default class Button extends React.Component {[m
   static propTypes = {[m
     name: PropTypes.string,[m
[1mdiff --git a/labp8/calculator-master/src/component/ButtonPanel.js b/labp8/calculator-master/src/component/ButtonPanel.js[m
[1mindex 994bca4..5c03911 100644[m
[1m--- a/labp8/calculator-master/src/component/ButtonPanel.js[m
[1m+++ b/labp8/calculator-master/src/component/ButtonPanel.js[m
[36m@@ -3,7 +3,7 @@[m [mimport React from "react";[m
 import PropTypes from "prop-types";[m
 [m
 import "./ButtonPanel.css";[m
[31m-[m
[32m+[m[32m//Wy≈õwietlanie kalkulatora[m
 export default class ButtonPanel extends React.Component {[m
   static propTypes = {[m
     clickHandler: PropTypes.func,[m
[36m@@ -45,6 +45,11 @@[m [mexport default class ButtonPanel extends React.Component {[m
           <Button name="." clickHandler={this.handleClick} />[m
           <Button name="=" clickHandler={this.handleClick} orange />[m
         </div>[m
[32m+[m[32m            <div>[m
[32m+[m[32m             <Button name="mod" clickHandler={this.handleClick} wide />[m
[32m+[m[32m             <Button name="^" clickHandler={this.handleClick} />[m
[32m+[m[32m`            <Button name="sqrt" clickHandler={this.handleClick} orange />[m
[32m+[m[32m            </div>[m
       </div>[m
     );[m
   }[m
[1mdiff --git a/labp8/calculator-master/src/logic/calculate.js b/labp8/calculator-master/src/logic/calculate.js[m
[1mindex 97e6532..cbe1608 100644[m
[1m--- a/labp8/calculator-master/src/logic/calculate.js[m
[1m+++ b/labp8/calculator-master/src/logic/calculate.js[m
[36m@@ -3,14 +3,13 @@[m [mimport Big from "big.js";[m
 import operate from "./operate";[m
 import isNumber from "./isNumber";[m
 [m
[32m+[m
 /**[m
[31m- * Given a button name and a calculator data object, return an updated[m
[31m- * calculator data object.[m
[31m- *[m
[31m- * Calculator data object contains:[m
[31m- *   total:String      the running total[m
[31m- *   next:String       the next number to be operated on with the total[m
[31m- *   operation:String  +, -, etc.[m
[32m+[m[32m * Biorπc pod uwagÍ nazwÍ przycisku i obiekt danych kalkulatora, zwrÛÊ zaktualizowany obiekt danych kalkulatora.[m
[32m+[m[32m * Obiekt danych kalkulatora zawiera:[m
[32m+[m[32m * total: bierzπca liczba[m
[32m+[m[32m * next: Podaj nastÍpnπ liczbÍ do operacji[m
[32m+[m[32m * operacja: +, - ...[m
  */[m
 export default function calculate(obj, buttonName) {[m
   if (buttonName === "AC") {[m
[36m@@ -25,14 +24,14 @@[m [mexport default function calculate(obj, buttonName) {[m
     if (buttonName === "0" && obj.next === "0") {[m
       return {};[m
     }[m
[31m-    // If there is an operation, update next[m
[32m+[m[32m      // Jeúli jest nastÍpna operacja zaktualizuj next jako nastÍpnπ[m
     if (obj.operation) {[m
       if (obj.next) {[m
         return { next: obj.next + buttonName };[m
       }[m
       return { next: buttonName };[m
     }[m
[31m-    // If there is no operation, update next and clear the value[m
[32m+[m[32m    // Jeúli nie ma operacji zaktualizuj next i wyczyúÊ wartoúÊ[m
     if (obj.next) {[m
       const next = obj.next === "0" ? buttonName : obj.next + buttonName;[m
       return {[m
[36m@@ -69,7 +68,7 @@[m [mexport default function calculate(obj, buttonName) {[m
 [m
   if (buttonName === ".") {[m
     if (obj.next) {[m
[31m-      // ignore a . if the next number already has one[m
[32m+[m[32m        //  zignoruj znak "." jeúli nastÍpny numer juø go ma[m
       if (obj.next.includes(".")) {[m
         return {};[m
       }[m
[36m@@ -86,7 +85,7 @@[m [mexport default function calculate(obj, buttonName) {[m
         operation: null,[m
       };[m
     } else {[m
[31m-      // '=' with no operation, nothing to do[m
[32m+[m[32m        //  Ñ=î bez operacji nie rÛb nic[m
       return {};[m
     }[m
   }[m
[36m@@ -101,15 +100,7 @@[m [mexport default function calculate(obj, buttonName) {[m
     return {};[m
   }[m
 [m
[31m-  // Button must be an operation[m
[31m-[m
[31m-  // When the user presses an operation button without having entered[m
[31m-  // a number first, do nothing.[m
[31m-  // if (!obj.next && !obj.total) {[m
[31m-  //   return {};[m
[31m-  // }[m
[31m-[m
[31m-  // User pressed an operation button and there is an existing operation[m
[32m+[m[32m  // Uøytkownik nacisnπ≥ przycisk operacji i istnieje juø operacja[m
   if (obj.operation) {[m
     return {[m
       total: operate(obj.total, obj.next, obj.operation),[m
[36m@@ -118,14 +109,14 @@[m [mexport default function calculate(obj, buttonName) {[m
     };[m
   }[m
 [m
[31m-  // no operation yet, but the user typed one[m
[32m+[m[32m    // nie ma jeszcze øadnej operacji, ale uøytkownik jπ wpisa≥[m
 [m
[31m-  // The user hasn't typed a number yet, just save the operation[m
[32m+[m[32m  // Uøytkownik nie wpisa≥ jeszcze numeru, po prostu zapisz operacjÍ[m
   if (!obj.next) {[m
     return { operation: buttonName };[m
   }[m
 [m
[31m-  // save the operation and shift 'next' into 'total'[m
[32m+[m[32m    // zapisz operacjÍ i zmieÒ next na total[m
   return {[m
     total: obj.next,[m
     next: null,[m
[1mdiff --git a/labp8/calculator-master/src/logic/calculate.test.js b/labp8/calculator-master/src/logic/calculate.test.js[m
[1mindex 939e833..cb1a683 100644[m
[1m--- a/labp8/calculator-master/src/logic/calculate.test.js[m
[1m+++ b/labp8/calculator-master/src/logic/calculate.test.js[m
[36m@@ -11,7 +11,8 @@[m [mfunction pressButtons(buttons) {[m
   buttons.forEach(button => {[m
     Object.assign(value, calculate(value, button));[m
   });[m
[31m-  // no need to distinguish between null and undefined values[m
[32m+[m
[32m+[m[32m// nie ma potrzeby rozr√≥≈ºniania warto≈õci null i undefined[m
   Object.keys(value).forEach(key => {[m
     if (value[key] === null) {[m
       delete value[key];[m
[36m@@ -69,8 +70,8 @@[m [mdescribe("calculate", function() {[m
     total: "18",[m
   });[m
 [m
[31m-  // When '=' is pressed and there is not enough information to complete[m
[31m-  // an operation, the '=' should be disregarded.[m
[32m+[m[32m// Po naci≈õniƒôciu ‚Äû=‚Äù  nie ma wystarczajƒÖcych informacji do uzupe≈Çnienia[m
[32m+[m[32m// operacje, ‚Äû=‚Äù nale≈ºy zignorowaƒá.[m
   test(["3", "+", "=", "3", "="], {[m
     total: "6",[m
   });[m
[36m@@ -132,7 +133,8 @@[m [mdescribe("calculate", function() {[m
     total: "0.2",[m
   });[m
 [m
[31m-  // should clear the operator when AC is pressed[m
[32m+[m[32m// powinno wyczy≈õciƒá operator po naci≈õniƒôciu AC[m
[32m+[m
   test(["1", "+", "2", "AC"], {});[m
   test(["+", "2", "AC"], {});[m
 [m
[36m@@ -150,12 +152,13 @@[m [mdescribe("calculate", function() {[m
     next: "2",[m
   });[m
 [m
[31m-  // the percentage sign should also act as '='[m
[32m+[m[32m// znak procentu powinien r√≥wnie≈º dzia≈Çaƒá jako ‚Äû=‚Äù[m
   test(["2", "x", "2", "%"], {[m
     total: "0.04",[m
   });[m
 [m
[31m-  //Test that pressing the multiplication or division sign multiple times should not affect the current computation[m
[32m+[m
[32m+[m[32m// Sprawd≈∫, czy wielokrotne naci≈õniƒôcie znaku mno≈ºenia lub dzielenia nie powinno wp≈Çywaƒá na bie≈ºƒÖce obliczenia[m
   test(["2", "x", "x"], {[m
     total: "2",[m
     operation: "x"[m
[1mdiff --git a/labp8/calculator-master/src/logic/isNumber.js b/labp8/calculator-master/src/logic/isNumber.js[m
[1mindex 0f4c40d..98d26fb 100644[m
[1m--- a/labp8/calculator-master/src/logic/isNumber.js[m
[1m+++ b/labp8/calculator-master/src/logic/isNumber.js[m
[36m@@ -1,3 +1,4 @@[m
[32m+[m[32m//Sprawdza czy podany element jest liczbπ[m
 export default function isNumber(item) {[m
   return /[0-9]+/.test(item);[m
 }[m
[1mdiff --git a/labp8/calculator-master/src/logic/operate.js b/labp8/calculator-master/src/logic/operate.js[m
[1mindex 0274e3a..501c4e2 100644[m
[1m--- a/labp8/calculator-master/src/logic/operate.js[m
[1m+++ b/labp8/calculator-master/src/logic/operate.js[m
[36m@@ -1,8 +1,10 @@[m
 import Big from "big.js";[m
 [m
[32m+[m[32m//dzia≈Çanie operator√≥w[m
[32m+[m
 export default function operate(numberOne, numberTwo, operation) {[m
   const one = Big(numberOne || "0");[m
[31m-  const two = Big(numberTwo || (operation === "√∑" || operation === 'x' ? "1": "0")); //If dividing or multiplying, then 1 maintains current value in cases of null[m
[32m+[m[32m  const two = Big(numberTwo || (operation === "√∑" || operation === 'x' ? "1": "0"));[m[41m [m
   if (operation === "+") {[m
     return one.plus(two).toString();[m
   }[m
[36m@@ -20,5 +22,14 @@[m [mexport default function operate(numberOne, numberTwo, operation) {[m
       return one.div(two).toString();[m
     }[m
   }[m
[32m+[m[32m    if (operation === "mod") {[m
[32m+[m[32m        return one.mod(two).toString();[m
[32m+[m[32m    }[m
[32m+[m[32m    if (operation === "sqrt") {[m
[32m+[m[32m        return one.sqrt().toString();[m
[32m+[m[32m    }[m
[32m+[m[32m    if (operation === "^") {[m
[32m+[m[32m        return one.pow(2).toString();[m
[32m+[m[32m    }[m
   throw Error(`Unknown operation '${operation}'`);[m
 }[m
