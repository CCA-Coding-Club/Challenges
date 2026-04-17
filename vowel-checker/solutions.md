--Python

```python
words = ["apple", "banana", "orange", "grape", "umbrella", "kiwi", "elephant"]

# Part 2: Create binary flags
vowels = "aeiou"
flags = []
for word in words:
    if word[0].lower() in vowels:
        flags.append(1)
    else:
        flags.append(0)

print(flags)  # [1, 0, 1, 0, 1, 0, 1]

# Part 3: Print vowel-starting words using flags
for i in range(len(words)):
    if flags[i] == 1:
        print(words[i])
```

--JavaScript

```javascript
const words = ["apple", "banana", "orange", "grape", "umbrella", "kiwi", "elephant"];

// Part 2: Create binary flags
const vowels = "aeiou";
const flags = [];
for (let i = 0; i < words.length; i++) {
  if (vowels.includes(words[i][0].toLowerCase())) {
    flags.push(1);
  } else {
    flags.push(0);
  }
}

console.log(flags);  // [1, 0, 1, 0, 1, 0, 1]

// Part 3: Print vowel-starting words using flags
for (let i = 0; i < words.length; i++) {
  if (flags[i] === 1) {
    console.log(words[i]);
  }
}
```

--Java

```java
public class VowelChecker {
    public static void main(String[] args) {
        String[] words = {"apple", "banana", "orange", "grape", "umbrella", "kiwi", "elephant"};
        String vowels = "aeiou";

        // Part 2: Create binary flags
        int[] flags = new int[words.length];
        for (int i = 0; i < words.length; i++) {
            if (vowels.indexOf(Character.toLowerCase(words[i].charAt(0))) != -1) {
                flags[i] = 1;
            } else {
                flags[i] = 0;
            }
        }

        // Part 3: Print vowel-starting words using flags
        for (int i = 0; i < words.length; i++) {
            if (flags[i] == 1) {
                System.out.println(words[i]);
            }
        }
    }
}
```
