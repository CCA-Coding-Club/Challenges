--Python

We use `range(1, 101)` to loop from 1 to 100. The modulo operator `%` checks for divisibility — we check 15 first because it covers both 3 and 5.

```python
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

--JavaScript

Same logic as Python. Note that JavaScript uses `===` for strict equality and `let` for loop variables.

```javascript
for (let i = 1; i <= 100; i++) {
  if (i % 15 === 0) console.log("FizzBuzz");
  else if (i % 3 === 0) console.log("Fizz");
  else if (i % 5 === 0) console.log("Buzz");
  else console.log(i);
}
```

--Java

Java requires a class and a `main` method to run. `System.out.println` is the equivalent of `print` in Python.

```java
public class FizzBuzz {
    public static void main(String[] args) {
        for (int i = 1; i <= 100; i++) {
            if (i % 15 == 0) System.out.println("FizzBuzz");
            else if (i % 3 == 0) System.out.println("Fizz");
            else if (i % 5 == 0) System.out.println("Buzz");
            else System.out.println(i);
        }
    }
}
```

--Bash
Implement '#!/bin/bash' for most linux operating. The #! symbol is called the shebang sign.

'''bash
while [ i < 100]
$i=0
//ignore this solution for now
do
    if [ (i % 3 == 0) ]

    then
        x
        x
    fi
done
'''