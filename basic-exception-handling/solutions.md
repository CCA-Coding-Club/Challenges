--Python

Part 1: In the try block, create a list of items and prompt the user for an index number. Use the index to access and print an item from the list.

This should throw an error if the user attempts to access an index that does not exist
```python
try:
    fruits = ["apple", "banana", "orange"]

    index = int(input("Enter an item number: "))
    item = fruits[index]

    print(f"The item is: {item}")

except:
    print("Something went wrong. Please try again.")
```

Part 2: In try, prompt the user for their birth year and typecast the input as an integer. This should throw an error if the age is anything but a number. 

Also, add a condition so if the birth year is less than 0, it will raise a value error.
```python
try:
    birth_year = int(input("Enter your birth year: "))

    if birth_year <= 0:
        raise ValueError

    age = 2026 - birth_year #current year minus birth year
    print(f"You are {age} years old.")

except ValueError:
    print("Please enter a valid birth year.")

except TypeError:
    print("There was a problem processing your information.")
```

--JavaScript

Part 1: In the try block, create an array of fruits, then prompt the user for an index number. Use that index to access an item from the array.

JavaScript will return undefined if an index does not exist instead of automatically throwing an error, so we manually check for that case. If the item is undefined, use throw new Error() to create an exception that will be caught by the catch block.
```javascript
try {
    const fruits = ["apple", "banana", "orange"];

    const index = prompt("Enter an item number: ");
    const item = fruits[index];

    if (item === undefined) {
        throw new Error("Item does not exist.");
    }

    console.log(`The item is: ${item}`);

} catch {
    console.log("Something went wrong. Please try again.");
}
```

Part 2: The try block prompts the user for their birth year and uses Number() to convert the input into a number.

JavaScript does not automatically throw an error when converting invalid strings into numbers. Instead, Number() returns NaN ("Not a Number"), so we use isNaN() to check if the conversion failed.

If the birth year is invalid or less than 0, use throw new TypeError() to create an exception. The catch block receives the error object and uses instanceof to check what type of error occurred.
```javascript
try {
    const birthYear = Number(prompt("Enter your birth year: "));

    if (isNaN(birthYear) || birthYear <= 0) {
        throw new TypeError("Invalid birth year.");
    }

    const age = 2026 - birthYear;
    console.log(`You are ${age} years old.`);

} catch (error) {
    if (error instanceof TypeError) {
        console.log("Please enter a valid birth year.");
    } else {
        console.log("There was a problem processing your information.");
    }
}
```