# Python Expression Calculator

A simple **Python calculator** that evaluates mathematical expressions following **PEMDAS rules** (Parentheses, Exponents, Multiplication/Division, Addition/Subtraction).  

This project does **not** use Python’s built-in `eval()` function. Instead, it implements:  

- **Tokenization** of the input expression  
- **Shunting Yard Algorithm** to convert infix expressions to **Reverse Polish Notation (RPN)**  
- **RPN evaluation** using a stack  

---

## **Features**

- Supports **integers and decimal numbers**  
- Handles **basic arithmetic operators**: `+`, `-`, `*`, `/`, `^`  
- Respects **PEMDAS order of operations**  
- Supports **parentheses** for grouping  

---

## **Usage**

1. Run the script:

```bash
python calculator.py
````

2. Enter a mathematical expression when prompted:

```
Enter an expression: 2 + 3 * (4 - 1)^2
```

3. The result will be displayed:

```
Result: 29.0
```

---

## **Examples**

| Expression         | Result |
| ------------------ | ------ |
| `2 + 3 * 4`        | 14     |
| `(2 + 3) * 4`      | 20     |
| `-5 + 3`           | -2     |
| `2 ^ 3 ^ 2`        | 512    |
| `2.5 * 4 - (-3)^2` | 8.5    |

---

## **Validation**

Before evaluating, the program validates expressions for:

* Invalid characters (anything other than `0-9`, `+ - * / ^ . ( )`)
* Mismatched parentheses
* Consecutive operators (like `++` or `*/`)
* Expressions starting or ending with invalid operators

---

## **Future Improvements**

* Better handling of **complex unary minus cases** (expressions and exponents)
* Handle **division by zero** and other exceptions gracefully

