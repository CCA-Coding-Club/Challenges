--Python

```python
def reverse_string(s):
    result = ""
    for i in range(len(s) - 1, -1, -1):
        result += s[i]
    return result

print(reverse_string("hello"))        # olleh
print(reverse_string("coding club"))  # bulc gnidoc
print(reverse_string("racecar"))      # racecar
```

--JavaScript

```javascript
function reverseString(s) {
  let result = "";
  for (let i = s.length - 1; i >= 0; i--) {
    result += s[i];
  }
  return result;
}

console.log(reverseString("hello"));        // olleh
console.log(reverseString("coding club")); // bulc gnidoc
```

--Java

```java
public class ReverseString {
    public static String reverse(String s) {
        StringBuilder result = new StringBuilder();
        for (int i = s.length() - 1; i >= 0; i--) {
            result.append(s.charAt(i));
        }
        return result.toString();
    }

    public static void main(String[] args) {
        System.out.println(reverse("hello"));        // olleh
        System.out.println(reverse("coding club")); // bulc gnidoc
    }
}
```
