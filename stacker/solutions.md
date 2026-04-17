--Python

### Part 1: Build a stack

```python
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
stack.pop()
print(stack)  # [1, 2]
```

### Part 2: Stack class

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()

    def print_stack(self):
        print(self.items)

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.pop()
s.print_stack()  # [1, 2]
```

--JavaScript

### Part 1: Build a stack

```javascript
let stack = [];
stack.push(1);
stack.push(2);
stack.push(3);
stack.pop();
console.log(stack);  // [1, 2]
```

### Part 2: Stack class

```javascript
class Stack {
  constructor() {
    this.items = [];
  }

  push(item) {
    this.items.push(item);
  }

  pop() {
    return this.items.pop();
  }

  printStack() {
    console.log(this.items);
  }
}

const s = new Stack();
s.push(1);
s.push(2);
s.push(3);
s.pop();
s.printStack();  // [1, 2]
```

--Java

### Part 1: Build a stack

```java
import java.util.ArrayList;

public class StackDemo {
    public static void main(String[] args) {
        ArrayList<Integer> stack = new ArrayList<>();
        stack.add(1);
        stack.add(2);
        stack.add(3);
        stack.remove(stack.size() - 1);
        System.out.println(stack);  // [1, 2]
    }
}
```

### Part 2: Stack class

```java
import java.util.ArrayList;

public class Stack {
    private ArrayList<Integer> items = new ArrayList<>();

    public void push(int item) {
        items.add(item);
    }

    public int pop() {
        return items.remove(items.size() - 1);
    }

    public void printStack() {
        System.out.println(items);
    }

    public static void main(String[] args) {
        Stack s = new Stack();
        s.push(1);
        s.push(2);
        s.push(3);
        s.pop();
        s.printStack();  // [1, 2]
    }
}
```
