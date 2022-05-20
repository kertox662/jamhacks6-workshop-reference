# Jamhacks 6 - Intro to Python

## Table of contents
1. **[Why Python](#why-python)**
2. **[Running Python](#running-python)**
3. **[Python Shell and Files](#python-shell-and-files)**
4. **[Writing Python Code](#writing-python-code)**
    1. [Arithmetic](#arithmetic)
        1. [Number types](#number-types)
    2. [Variables](#variables)
    3. [Strings](#strings)
    4. [User Input and Output](#user-input-and-output)
    5. [Comments](#comments)
    6. [Booleans](#booleans)
        1. [Comparisons](#comparisons)
        2. [Boolean Operators](#boolean-operators)
    7. [Control Flow](#control-flow)
        1. [Conditional Blocks](#conditional-blocks)
        2. [Loops](#loops)
    8. [Lists](#lists)
        1. [List operations](#list-operations)
        2. [Looping over lists](#looping-over-lists)
        3. [Lists inside lists](#lists-inside-lists)
    9. [Functions](#functions)
    10. [Importing Modules](#importing-modules)
    11. [Opening a File](#opening-a-file)
        1. [Reading from a file](#reading-from-a-file)
        2. [Writing to a file](#writing-to-a-file)
        3. [Closing files and `with`](#closing-files-and-with)
5. **[A Few Takeaways](#a-few-takeaways)**
5. **[Appendix](#appendix)**


## Why Python
There are many reasons why I think Python is a great language to learn. First of all, there are a ton of resources on the internet to learn from. You can find thousands of hours of video tutorials for Python. There are many books about Python you can read, and even more documentation online. Second, I find Python is very quick and intuitive to write. There is no real overhead to starting to write a Python file. It just starts reading from the top and goes line by line. Also, the actual lines of code read much closer to actual English compared to other programming languages, which may be easier to read. A final reason I want to touch on is that there is a lot of available libraries for Python. Many people have written code to be run in Python and made it available for others to use. This is really nice as you don't need to worry about the details about how it works and can just use the existing code.

## Running Python

An option to quickly start up that I like is writing and running Python online. A website I find nice is [replit](https://replit.com) which also works well for collaborating.

Here are a few links to show you how to install and run Python on your computer:
- [Windows](https://docs.microsoft.com/en-us/windows/python/beginners)
- [Mac OS](https://docs.python.org/3/using/mac.html)
- [Linux](https://docs.python.org/3/using/unix.html)

You could also look up something on the lines of "Mac OS install python"

If you want to edit Python locally, here are some popular editors and IDEs that you can consider trying out:
- [Visual Studio Code]() (My favourite right now)
- [Sublime Text]()
- [Atom]()
- [PyCharm]()
- [Wing IDE]() (My first editor)

## Python Shell and Files

When we think of running an application, I feel like the first thing that comes to mind is clicking an icon that starts up some program. This might be a browser, a text editor, or maybe a drawing app. When we run a Python program, we will be running an application too, but probably not the one you expect. What we will run is the Python Interpreter. I will discuss two modes for the interpreter, through a file and the shell.

When you give the interpreter a Python file as input, it will read the code and execute it line by line. Some commands will make it jump around to other lines, but more or less the program runs in a sequential manner.

The shell on the other hand will wait for user input as to what to do. It reads the next line (or sometimes lines if you need to give it a block), executes this most recent code that it's given, then print out what the code evaluates to. It will repeat this process indefinitely, or until the user tells it to stop.

The way I like to treat the difference is when you want to give the interpreter the program. You can write your whole program into a file and give the whole thing to Python right away, or you can give it to it line by line. You will most like be working in the first way a lot more. Using the shell is sometimes tedious, but it may be nice if you have some quick calculations to do or you just want to test how something works. For example, I have extensively used the shell when writing the examples in this file, just to make sure they work.

If you run Python through the command line, you can specify that after the program runs from a file that you want to keep the interpreter alive and open a shell. You do that using the `-it` flag: `python3 -it main.py`.

## Writing Python Code

A quick disclaimer, some parts I mention will not be entirely accurate. This is to make certain parts easier to understand as a full, accurate description would take a lot longer and be harder to follow initially learning Python. There will be a section in the [Appendix](#appendix) which explains some of these concepts.

### Arithmetic

Let's start looking at what Python can do with some arithmetic. You can write an expression like `2 + 3` which will evaluate to the value `5`. Python knows the following operations:

| Operation  | Symbol  | Example  | Explanation |
|:---:|:---:|:---:| --- |
| Addition         | +  | `2 + 3` → `5`  |
| Subtraction       | -  |  `10 - 4` → `6` |
| Multiplication   | *  |  `1.2 * 2.8` → `3.36` |
| Division         | /  |  `5 / 2` → `2.5` |
| Floor Division   | // |  `5 // 2` → `2` | `5 / 2` is `2.5`, `2` is that largest integer smaller than `2.5` |
| Modulo/Remainder | %  |   `23 % 7` → `2`| `7*3 = 21`, `23` is `2` larger than `21`, so the remainder is `2`|
| Exponentiation   | ** |   `3**5` → `243` |

Arithmetic in Python follows the standard order of operations. For example the expression `3 * 2 + 64 / 2**4` would evaluate as follows:
`3 * 2 + 64 / 2**4` → `3 * 2 + 64 / 16` → `6 + 64 / 2**4` → `6 + 4` → `10`.
You can add parentheses into arithmetic expressions to give the inner expressions higher priority: `2 * (3 + 4)` → `14`

Something to keep in mind about division by zero results in an error. There are ways to recover from it, but the simplest will be to check whether the divisor is 0, which we will see later.

#### Number Types
Something important in Python is numbers with a decimal part are not actually the same as those without. You might notice something with the expression `4 // 2` which results in `2`, compared to `4 / 2`, resulting in `2.0`. We can check the type of an expression using the `type` function. Using it on both, we will see `type(4//2)` → `<class 'int'>` and `type(4 / 2)` → `<class 'float'>`.

What this shows is that the result of `4//2` is an integer type (shortened to `int`) while `4/2` is a floating point number (shortened to `float`).

There are a few difference between the two types. The most obvious one is floats will print with a decimal point while integers will not. Another difference is the maximum value. Integers in Python do not actually have an upper (nor lower) limit. Floats on the other hand go up to around `10^300` in absolute value. There are also some cases where you have to use one over the other, some which we will see later. There are probably some other differences, but the main point is that these values are not the same.

We can convert between floats and ints. Similar to using `type`, we can give what type we want to convert to, followed by the expression wrapped in parentheses. For example, `float(153)` → `153.0`. The more interesting conversion is from float to int. We cannot represent a decimal number as an integer. In this case, it was decided to just drop the decimal point and everything after it. For example `int(3.1415)` → `3`. 

### Variables
Sometimes we want to store a value for later. This is where variables comes into play. We can make a new variable by assigning a value to a variable name using the `=` assignment operator. For example `x = 8` will store the value `8` in the variable `x`. We can now use `x` in expressions, like `x + 3`, which results to `11` in this case.

There are some rules for variable names which can be found [here](https://www.w3schools.com/python/gloss_python_variable_names.asp).

If you apply the assignment operator again the value will be updated.
```python
x = 8
x = 12
x + 3 # Results in 15
```

Something to keep in mind is that a variable must exist before it can be used in an expression.
For example, if we try to evaluate `y + 1` (or just `y` even), we would get an error saying that `y` is not defined.

There will be times where you will need to update some variable. It is common to have a statement like `x = x + 1`. In algebra, this statement does not have any solutions for `x`, since that would mean that `0 = 1`. Here though, the `=` symbol means something different.
We have seen above the general format `LHS = RHS` (Left/Right Hand Side). Unlike in math where the `=` symbol says that two expressions have the same value, in Python it means "Evaluate the expression for the RHS, then put the result in the variable on the LHS."

For example:
```python
x = 4
x = x + 2
```

The statement `x = x + 2` will run as follows:
* We want to evaluate the right hand side `x + 2`.
* `x` currently has value 4, so `x + 2` is 6
* The right hand side evaluates to 6, so we will store the value 6 in the variable `x`.

There are a few small shortcuts for doing arithmetic assignment added in the [Appendix](#appendix).

### Strings
Up until now we've been using the `int` and `float` types which are great for numbers. Now it's time to introduce a new type for text, strings (shortened to `str`).

Basic string values are written by surrounding text with quotation marks. Here are a few examples:
```python
s1 = "A String"
s2 = 'Another String'
s3 = '''A
Multiline
String'''
```
You can use some of the arithmetic operations with strings as well. For example, using `+` will concatenate two strings: `"cat" + "dog"` → `"catdog"`. You can multiply a string by an integer, which repeat the string that many times: `"Hello!"*3` → `"Hello!Hello!Hello!"`.

Something to keep in mind is that multiplying a string that contains digits will not convert the string to a number. `3 * "2"` → `"222"` and not `6`.

Sometimes though we have numbers stored as strings. We are able to try to convert between them. Converting from int or float to a string is easy, like before just put the number inside `str()` like `str(1.23)`, resulting in `"1.23"`. Converting from string to one of the number types might cause problems though. Normally it works like the other conversions, `int("4")` results in `4` and `float("1.23")` results in `1.23`. Sometimes though the text you are trying to convert does not make sense. For example `float("Apple")` will result in error since Python does not know `"Apple"` to a float. Even something like `int("1.23")` will cause an error. The integer conversion by itself expects a number in base 10. This can be specified though, see the [Appendix](#appendix) for more details. The [Appendix](#appendix) will also contain some info on additional string operations.

### User Input and Output
We've covered ints, floats, string and some operations that can be applied to them. These are great to play around with in the shell, but to interact with the user in an actual program you'll need a way to get input from them and display some output. 

You can display something to the user using the `print` function. Let's write a simple program that prints something to the screen:
```python
print("Hello World!")
```

Running this program will display `Hello World!` to the screen.
So why do we need a print function? The Python shell runs a "Read-Evaluate-Print" loop (REPL). It reads the next lines, runs them and prints out what was evaluated. Just running a Python program does not print out what is evaluated. So a program like
```python
x = 3
x + 4
```
would not print `7`, instead it will not print anything at all. To be able to see the result of `x+4` we need to print it: `print(x+4)`.

The print function can also take in multiple values to print, for example:
```python
fruit = "apple"
print("An", fruit, "is a fruit.")
```

To get user input we can use the `input` function. When it runs, it will wait for the user to type some text and hit Enter. It will evaluate to the text which the user typed as a string.
```python
userInput = input()
```

You can give the function a string which it will display before it starts to wait for the user's input. This is useful to use as a prompt to tell the user that the program expects them to type something as well as a find as to what to type.
```python
name = input("What is you name?")
age = input("How old are you?")
```
We may now want to print something like:
```python
print("In 10 years", name, "will be", age+10, "years old")
```
There is a problem though! Since age is the result of the `input` function, it is a string. Python does not know how to add an a string with 10, an integer. What we want to do is to convert the age to an integer. We can do that in multiple ways:
```python
age = int(input("How old are you?"))
or
age = input("How old are you?")
age = int(age)
or
print("In 10 years", name, "will be", int(age)+10, "years old")
```
I usually opt for the first option, but all of these would achieve the goal.

### Comments
Just as a quick note, we can add extra information to our code which is not meant to be run. If line contains a # symbol which is not in a string, all characters on that line after (and including) the # character will be ignored. This allows you to give more details such as what the code is doing. For example:
```python
print("Hello World!") # Prints "Hello World!" to the display.
```
It might not be necessarily to put in a comment like this in actual code, but a comment in important places goes a long way in communicating ideas to others.

### Booleans
A fourth very useful type to know about is a `boolean`, which take on either `True` or `False`.  We can set variables to these values directly like `myBoolean = True`, but this in many cases isn't too useful. Instead, it is often much more useful to get boolean values from comparisons and functions. Booleans can also be combined using boolean operators.

We have seen some functions like `input` which evaluate to a string. We also have functions that evaluate to boolean which often answer a question. For example, the string type can have a `startswith` and `isdigit` function run on them.
```python
startsWithABC = "bcdefg".startswith("abc")
isInt = "12345".isdigit()
```

#### Comparisons
If we have two or more values, we may want to compare them to see their relationships.
| Operation  | Symbol  | Example |
|:---:|:---:|:---:|
| Equal                    | ==  | `"abc" == "def"`  |
| Not Equal                | != or <>  | `"abc" != 123` |
| Less Than                | <  |  `10 < 12` |
| Less Than or Equal to    | <=  | `"apple" <= "banana"` |
| Greater Than             | > | `0 > -3`  | 
| Greater Than or Equal to | >=  | `"jam" >= "hacks"` |

When comparing two strings like `"apple" <= "banana"`, it will use lexicographic order, or in other words, "Would 'apple' come before 'banana' in a dictionary?"
Something to note is that not all types can be compared to each other in all ways. For example, `"abc" == 123` is valid and would always evaluate to `False`. On the other hand, `"abc" < 123` is not valid and would cause an error.

#### Boolean Operators
There are three boolean operators in Python: `not, and, or`. `not` takes a boolean value and inverts it. If the original value, `A`, is true, then `not A` is `False` and vice versa. `and` takes in two boolean values and evaluates to `True` if both values are `True`. `or` is similar but it evaluates to `True` if either of the two original values are `True`. 

### Control Flow
The programs we can write so far can't react much to the inputs that we give it, apart from displaying slightly different values. The next goal for us will be to look at some ways to control the flow of the program. I will show first conditional blocks, which control which code is run, and then loops which can repeat code more than once.

#### Conditional Blocks
Some of the most powerful uses for boolean is to add conditions to running certain code. We might want to run one piece of code in one situation, while some other in another.

The general format is
```python
if test1:
    some code
    ...
elif test2:
    some code
    ...
...
else:
    some code
    ...
```

For example:
```python
friend1 = "Alice"
friend2 = "Bob"
friend3 = "Casey"

friend = input("What is your friend's name?")

if friend == friend1:
    print("Hey",friend+"!")
elif friend == friend2:
    print("Howdy,",friend)
elif friend == friend3:
    print("Hi",friend)
else:
    print("Hello",friend)
```

The idea with if/elif/else is we test each condition in order. We first look at the test for the if, then for the first elif, and so on. If any of tests are true, we will run the code for that condition and skip all tests and code after it.

What this means is that even if there would be an error in a future test case, it will not be evaluated:
```python
if 2 > 1:
    print("This will run!")

# This will not cause an error since 2 > 1 is always true
elif 1/0 > 0:
    print("This test case should be skipped")

else:
    print("The else")
```

This may come in handy in case of checking for values that may cause an error:
```python
a = int(input("First Number?"))
b = int(input("Second Number?"))
if b == 0:
    print("Cannot divide by 0")
elif a / b >= 5:
    print("a is at least 5 times b")
else:
    print("a is less than 5 times b")
```

The elif and else statements are optional for if blocks. All of the following are valid:
``` python
if test:
    some code
    ...

if test:
    ...
else:
    ...

if test:
    ...
elif test2:
    ...
...
```

It is not uncommon to write something called nested if statements. These are if statements inside of other if statements. This is often useful when you need to check multiple conditions and run specific code for each combination of results.

For example:
```python
a = int(input("First Number?"))
b = int(input("Second Number?"))
if b == 0:
    if a == 0:
        print("Both a and b are 0")
    else:
        print("b is 0")
else:
    if a == 0:
        print("a is 0")
    else:
        print("Neither a nor b are 0")
```

There are some additional information on blocks which is added to the [Appendix](#appendix). This part specifically might be quite useful and I would recommend checking out.

#### Loops
Loops are used to repeat some code multiple times. Python has two types of loops: `while` loops and `for` loops.

While loops will have a condition and while the condition is true, it will run the loop.

```python
a = 5
while a > 0: # This will run 5 times
    print("a is now", a)
    a = a - 1
```

The condition will be checked each time after the inner block is done, in this case after the `a = a - 1` statement.

The following code will also produce the same results:
```python
a = 5
while a > 0:
    print("a is now", a)
    a = a * -1
    # a is less than 0 here, but since we only check
    # the condition at the top it won't affect it
    a = -1 - a
```

Each time that you go through the code inside of the loop is called an iteration.

There are two useful statements that can be used inside of loops, `break` and `continue`. `break` will immediately exit out of the loop. It is useful if you want to stop a loop prematurely. `continue` will skip the rest of the statements in a block and go back to the condition. It is good when you want to go to the next iteration.

An example:
```python
a = 6
while a > 0:
    print(a)
    a = a - 1
    print("a has decreased")

    # If a < 2 we will exit the loop
    if a < 2:
        break
    print("a is least 2")

    # If a now odd we want to print it out
    # One way to do that is to always print it
    # but to skip the print when a is even.
    if a % 2 == 0:
        continue
    print("a is now odd")
```
Running this will result in:
```
6
a has decreased
a is at least 2
a is now odd
5
a has decreased
a is at least 2
4
a has decreased
a is at least 2
a is now odd
3
a has decreased
a is at least 2
2
a has decreased
```

A neat "trick" to run a loop infinitely is to do:
```python
while True:
    code
    ...
```
The second type of loop is a `for` loop. The first version of the for loop I will show will just repeat a block some number of times. It will look like this:
```python
# Will print "Hello!" 5 times
for i in range(5):
    print("Hello!")
```
In this for loop, `i` will have a different value every single time, let's print it out:
```python
for i in range(5):
    print("i =",i)
```
which results in
```
i = 0
i = 1
i = 2
i = 3
i = 4
```

There are two things to notice here, first, the first value for `i` is 0! This might be unexpected since normally we start counting at 1, but it will make sense in a little bit. The second thing is that we ended at the value right before the one we specified in the range.

We can give `range` some extra values. If it gets two values, it will start at the first one, and increase by one until it reaches the value one less than the second one. If it has three values, the third value will be the amount `i` gets increased by.

For example:
```python
for i in range(10,15):
    print("i =",i)
print("===")
for i in range(5,0,-1):
    print("i =",i)
```
results in:
```
i = 10
i = 11
i = 12
i = 13
i = 14
===
i = 5
i = 4
i = 3
i = 2
i = 1
```
Two quick final remarks about loops. First, `break` and `continue` work similarly in for loops as they do in while loops. Second, just like if statements, loops can be nested.


### Lists
The variables we've been using like ints and strings only a single value, a single number or a single piece of text. We will now look at a way to store multiple values in a single variable. For this we will be using what Python calls a list.

Let's look at how we can make a list:
```python
colours = ["red", "green", "blue"]
```
Here the list contains 3 strings representing 3 colours.

Sometimes, especially for long lists, it may be useful and cleaner to put the elements on multiple lines:
```python
colours = [
    "red", 
    "green", 
    "blue"
]
```

We can also make a an empty list by not putting anything inside the brackets: `colours = []`

We access the elements of the list using square brackets with an integer inside.

```python
print("A colour:", colours[1])
```
If we run this now, we will see that it prints `green`. Why is this? We gave it 1, so we would expect it to give the first element back from the list. Well, lists in Python (and similarly in many languages) start counting at 0! This should remind you of the `range` function we saw earlier.

We can print the three colours as follows:
```python
print("First colour:",  colours[0]) # red
print("Second colour:", colours[1]) # green
print("Third colour:",  colours[2]) # blue
```

You might be wondering what happens if we put in some other number. We can try `colours[3]`, but then we get `IndexError: list index out of range`. We cannot use a number greater or equal to the number of elements in the list. Let's try `colours[-1]`. You might be surprised, but this works, and evaluates to `blue`! What it's doing is counting from the end of the array. The snippet of code above can also technically be rewritten to the following to get the same results:
```python
print("First colour:",  colours[-3]) # red
print("Second colour:", colours[-2]) # green
print("Third colour:",  colours[-1]) # blue
```
Trying `colours[-4]` will also give an index error.

We can also use this index to modify the elements inside of the list. For example, we can now run:
```python
colours[1] = "yellow"
print(colours)
```
which will display `['red','yellow','blue']` since we changed the 2nd element (index 1) from green to yellow.

Something interesting is that in Python we can have all kinds of different types in a single list:
```python
mixedList = ["a", 1, 3.14, True]
```
Although it may be easier to keep only one type in a particular list whenever possible.

We can also get a sublist using these square brackets. This syntax can also be applied to get a substring in a string. You can check it out on [GeeksForGeeks](https://www.geeksforgeeks.org/python-list-slicing/).

#### List operations
There are several more useful operations for lists. You can check out a more comprehensive list on [W3Schools](https://www.w3schools.com/python/python_ref_list.asp), but I here I will give four examples.

First is `append`, which will add an element to the end of list. Next is `pop`, which will remove the element at the index you specify. A third operation is `index`, which finds the first index in the list that has the value you specified. A fourth and final operation is `copy`, which returns a new list with the same elements. 

```python
nums = [1,2,3,4,5]
nums.append(6)
print(nums) # [1,2,3,4,5,6]
nums.pop(2)
print(nums) # [1,2,4,5,6]
print(nums.index(4)) # 3
nums2 = nums.copy()
```

Many operations like getting the element at some index or `pop` need to be in the bounds for the array. A great function for this is the `len` function, which returns the number of elements in a list.
```python
print(len([1,2,3,4])) # 4
```

Another interesting operation is checking if an element is in a list. This can be done with the `in` keyword.
```python
nums = [1,2,3,4,5]
if 3 in nums:
    print("3 is in nums")
if "a" not in nums:
    print("a is not in nums")
# both will print
```

There is a nice operation to concatenate/merge two lists together. It just uses the `+` symbol.
```python
print([1,2,3] + [2,3,4]) # results in [1, 2, 3, 2, 3, 4]
```

A final operation I will show you is a way to repeat lists. We can multiply a list by an integer, which will repeat the elements in a list that many times.
```python
print([1,2]*3) # results in [1, 2, 1, 2, 1, 2] 
```

Something to notice here is that these two list operations are very similar that those for strings. We will see something that will also be applicable to strings that we haven't talked about.

#### Looping over lists
Something we often do is run some code on each element in the list. Let's say we get three numbers from the user and print each element plus 5 two times.

We have two great tools for this, `range` and `len`!
We combine the two to make a loop:
```python
nums = []
num1 = int(input("First number:"))
nums.append(num1)
num2 = int(input("Second number:"))
nums.append(num2)
num3 = int(input("Third number:"))
nums.append(num3)

for i in range(2):
    for j in range(len(nums)):
        print(nums[j] + 5)
```

This is a great way to loop over lists. But we also have another option. We can use the list itself instead of `range`! Let's also move the prompts into a loop, we don't really need to repeat a lot of the code there:

```python
nums = []
prompts = [
    "First number:",
    "Second number:",
    "Third number:"
]

for prompt in prompts:
    num = int(input(prompt))
    nums.append(num)

for i in range(2):
    for num in nums:
        print(num + 5)
```
I hinted at this before, but we can actually do this with strings. That will loop over the characters in the string:
```python
for c in "abc":
    print(c) # will print a, b, and c on separate lines
```

#### Lists inside lists

I mentioned before that the types inside lists can be of different types, this includes other lists. For example, we can make a list like this:
```python
nums = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
```
The inner lists don't even need to be the same length:
```python
nums = [
    [1,2,3],
    [4,5,6,7],
    [8,9,10,11,12]
]
```

Now when we access the first element in `nums`, instead of an int or a string we get a list:
```python
print(nums[0]) # [1, 2, 3]
```
From here we can access an element in this 3 element list using another index. For example, we can print out the 2:
```python
print(nums[0][1]) # 2
```

The way I like to think about this is using the order that it simplifies by, similar to how numbers simplify in arithmetic. We can put brackets around the order. Let's use the first version to make it easier:
`nums[0][1]` → `((nums)[0])[1]` → `(([[1,2,3],[4,5,6],[7,8,9]])[0])[1]` → `(([1,2,3])[1]` → `2`
We first evaluate `nums`, then index 0 in that list, then index 1 in the next to finally produce 2.

### Functions

As I have been slowly hinting at throughout, we have already seen one aspect of functions: using them. We've seen `print`, `input` and several others. The idea behind a function is to group a piece of code together and be able to use it by specifying the function's name. This is known as "calling" the function. We do this in code by writing out the function's name, followed by parentheses, like `print()`. A powerful aspect of functions is that you can give them information to work with. This information is called the "arguments" to the function. For print, we have put what we want to display in the parentheses. For example, we can do `print("Hello World!")`. When you want to pass more than one argument, you separate them with commas:

```python
n = 5
print("n is equal to", n)
```

Note that calling `print` a function is slightly inaccurate in the general sense. In Python it will be called a function (you can even run `type` on it), but there is a better word for it. Please see the [Appendix](#appendix) for details.

Something else that functions can do is evaluate to some value. We have seen this for the `input` function, which will evaluate to a string. We have seen this like `name = input("What is your name?")`. What the function will give is just an expression. It can be used in assignment like for name, in conditional expressions, or even as arguments to other functions. Here are a few examples:

```python
if input("Give me a number:") > 5:
    print("Your number is greater than 5")
else:
    print("Your number is not greater than 5")

print("Your name is", input("What is your name?"))
```

We can also write our own functions. The overall format looks like this:
```python
def function_name(arg1,arg2,...):
    code
```
For the arguments, we can also have 0 arguments by just having nothing in between the parentheses.

For example, putting the name prompt code into a function:
```python
def askForName():
    name = input("What is your name?")
    print("Hello", name + "!")
```
We can then run call this function by running `askForName()`.

When calling a function, we will need to give the exact number of arguments that is in the definition. For example, for the following function, we will need to specify exactly two arguments.
```python
def add(a,b):
    return a + b
```
We can define the arguments slightly differently to change this behaviour, check out the [Appendix](#appendix) for more details.

We also want a way that specifies what value a function evaluates to. This is done through the `return` keyword. For example, we can write a `square` function which returns a number squared. This of course can be done with the `**` operator, but this is useful to demonstrate returning a value:

```python
# square takes in a number and return that
# number squared.
def square(n):
    return n * n
```

Now `print(square(5))` will print `25`. Something interesting to note is that if there is not return statement the function call will evaluate to a special value `None`. 

A function can also have multiple return statements. There is a famous function related to the Collatz conjecture. It takes in an integer, if it is even it returns half and 3 times the integer plus 1 if odd. We can write this function as follows:

```python
def next_collatz(n):
    if n % 2 == 0: # even case
        return n // 2
    # odd case
    return 3 * n + 1
```

A return statement can also be used to immediately exit a function. An empty return, with no expression, will return the special `None` value.

```python
# prints a / b
def print_quotient(a,b):
    if b == 0:
        print("undefined")
        return # will immediately exit the function

    # since there is a return after the b == 0 if
    # then we know that b is not 0
    print(a / b)
``` 

A final remark for functions is that they work with variables a bit differently. When you define a variable in a function it will by default treat it as a new and separate variable. Take this for example:
```python
x = 2
def f():
    x = 3
f()
print(x) # prints 2
```
We see here that even though in the function `f` we assigned the variable `x` to 3, it did not change outside of the function. The variable is available only inside of the function block. Interestingly though, we can still access the outside variable inside of the function:
```python
x = 2
def f():
    print(x)
f() # prints 2
```
There is a caveat though, if we would later define `x` locally, it would result in an error. Python will try to reference a local version of the variable, but we will be using it before it is defined:
```python
x = 2
def f():
    print(x) # Results in UnboundLocalError
    x = 3
f()
```

There is a way to get the function to update the variable though. That is through the `global` keyword. In practice it may be bad to keep everything globally, but in a pinch it works well. You will want to specify what variables you want global like so:
```python
x = 0
y = 1
def f():
    global x,y # Can be split into multiple lines too
    x = y + 4
    y = 2 * x - 1
f()
print(x,y) # 5,9
```

### Importing Modules

Many simple programs can often be written in a single file. Eventually though, our programs will get too big to cleanly fit into a single file. Another situation we might find ourselves in is that we want speed up development and use someone else's code library. This is where imports come in. The purpose is to be able to run and access code that exists in other files. Imports come in three basic forms. Let's take a look at importing the math library:

```python
import math
or
import math as STD_math # alias to "standard math"
or
from math import sqrt,pi,log # import specific variables/functions/etc.
```
The final version can also be done like `from math import *` which gives you direct access to all defined names from the math module.

To access something after importing using the first two formats you write `module.name`, for example `math.pi` or `STD_math.sqrt(25)`. The third variation you can just access it direction just writing it `pi` or `sqrt(25)`.

You can find a large list of standard modules in the [python docs](https://docs.python.org/3/library/). There are also many download modules from online, such as by using `pip`. See the [Appendix](#appendix) for an example.

You can also split your own program into multiple files. Let's say you define a function `foo(n)` in a file you call `foo.py`. You want to import the `foo` function into another file, `main.py`, which is in the same folder as `foo.py`. You can do so with `import foo`, and now you access the foo function using `foo.foo(5)`.

You can also organize your files into multiple folders. For example if we have a folder called `sub` with a file `baz.py` inside, it can be imported using `import sub.baz`. You will need use `sub.baz` for all references to the module though, so it may be useful to alias this one like `import sub.baz as baz`.

One thing to note is that when you import a file, all code in that file is run. For example, if you have print statements that would normally run when run a file, they will also run when you import it! Depending on what you're doing, it may be a good idea to only have functions in separate files. There are ways to avoid this, see the [Appendix](#appendix) for details.

### Opening a File
At times we will want to interact with files using Python. We might want to read the data inside of a file, or possibly write to one. This can be done with the `open` function.

#### Reading from a file

The first interaction I will show you is reading from a file. We can open a file using `open("path/to/file")` and setting it to a variable. Make sure that the file actually exists or else you will get an error!

There are several ways to read form a file. A comprehensive list of what you can do with a file can be found in the [Python Docs](https://docs.python.org/3/library/io.html#i-o-base-classes).

The first way is to use the `read` function, which just returns a string:
```python
f = open("file.txt")
s = f.read()
```
`read` will exhaust all of the characters in the file, so you can only run `read` once (doing so multiple time returns an empty string). This will read all of the text in the file, including all of the newline characters.

Another method is using `readline`, which returns only the next line of the file:
```python
f = open("file.txt")
print("First line in file:", f.readline())
```
You can read all lines at once using `readlines`, which returns a list of strings where each string is one line.

The last method I'll show you is to just iterate through the file in a for loop:
```python
f = open("file.txt")
i = 1
for line in f:
    print("Line",1,"is:",line)
```

#### Writing to a file
The way we opened a file for reading will not allow us to write to that file. Instead, we need to pass in a second argument to `open`, either "w" for overwriting or "a" for appending, like `open("file.txt", "w")`. There are other possible parameters, see the [Python Docs](https://docs.python.org/3/library/functions.html#open) for the `open` function.

After, we can use `write` or `writelines` with the file to output to the file. These are described in the same [Python Docs](https://docs.python.org/3/library/io.html#i-o-base-classes) as the reading methods.

For example:
```python
names = ["Alice", "Bob", "Claire", "Daniel", "Elise"]
f = open("names.txt", "w")
for name in names:
    f.write(name)
    f.write("\n") # Write a newline
```

Although we run the `write` function on a file, it may not actually be written to the file system right away. If that needs to happen immediately, you can use `file.flush()` to do so. Otherwise you could wait for the file to close and it will automatically flush.

#### Closing files and `with`
What we've been doing with files hasn't actually been very safe. By that I mean we have been opening files, but the operating system also expects us to close it. Some reasons to close a file have been documented on [StackOverflow](https://stackoverflow.com/questions/25070854/why-should-i-close-files-in-python), feel free to read up on it.

The basic way to close a file is just with the file's `close` function. For example:
```python
f = open("file.txt")
s = f.read()
f.close()
```
This runs into some issues though, what if we never reach the line that closes the file? This could happen if an error occurs while the file is open:
```python
f = open("file.txt")
print(1 / 0)
f.close()
```
The preferred way to open a file is by using a `with` statement:
```python
with open("file.txt") as f:
    s = f.read()
```
Whenever the block in the `with` statement is done the file will automatically be closed, even if an error occurs. Reading and writing works the same, it's just the opening of the file that is slightly different.

## A Few Takeaways
At this point you know some Python basics. You know about arithmetic, functions, lists, and much more. So what happens now?

I believe the first step is to cement the knowledge bit better in your mind. I find for me a great way to do this is to actually make something. It might a some project, or just some script that helps you do something easier. 

Now, even though remembering how to write everything in Python would be great, you shouldn't sweat it if you can't recall how to do something. As I mentioned in the beginning, there are so many resources for Python, you can easily look up what you need. The point is, the exact details, like syntax or function names, don't really matter. It's so much more important to understand the concepts and logic behind how to do something. 

Finally, it is very important to stay curious, but patient. The fact is, learning is hard; We might not understand every part of something we learn right away, but that's okay. We can always take a step back and return to the ideas later. But, even though we need to understand that learning is difficult, we need to be ready to pursue it. I find the easiest way start learning about something is to look up if someone has some sort of lesson on it. For example, searching up "python game tutorial" would be a great way to start off making games.

Hopefully you keep at least a few of these ideas in mind as you continue to learn Python. Happy coding!

<!-- ================================ -->
<!-- ================================ -->
<!-- ================================ -->



## Appendix

### Clearing up the lies
Throughout this document I referred to all "commands" that you call as functions. Although it is easier to understand and true in how they are defined, the naming is not usually this general.

The first difference is the distinction between standalone functions and those tied to some variable. We have seen them with the different types, for example lists have `append`, `pop`, and more. When attached to a variable like this these functions are called methods. This comes from a coding technique called Object Oriented Programming (OOP). Here is an introductory [article](https://realpython.com/python3-object-oriented-programming/) for OOP. 

Another distinction is between functions that return a value (other than `None`) and those that do not. If a Python function does not return anything it is more accurate to call it a procedure. The goal of calling it is to get the effects that come from it, like displaying text or updating a variable. With this description we can see that `print` is a procedure while `input` is a function. This of course does not mean that we can't run normal functions just for their effects. Sometimes we may want to pause and wait for the user's go-ahead to continue with the program. `input` is a great way to do that as it will wait for the user to put a newline (or end their own input) before it continues.

Finally, we've been using the type names like `int`,`float`, and `str` to convert between the different types. Although they are implemented as functions, they are a special type called constructors. This is again part of OOP, so it would be good to look at the article linked above.

### Installing with pip
`pip` is a package manager tool for Python. It helps manage and install modules for you to use. Here are a few useful commands, but for a full list run the `pip -h` for the help menu or check out the [pip docs](https://pip.pypa.io/en/stable/):
- `pip install <package1> <package2> ...`  will try to install all of the packages if available. E.g. `pip install numpy`
- `pip install --upgrade <package1> ...` will install the latest versions of the package.
- `pip uninstall <package1> ...` uninstalls packages.
- `pip search <package1>` will search for available packages with the name that you provided.
- `pip list` shows you the packages you have installed.
### Arithmetic assignment

I've shown you the simple way of updating a variable with arithmetic operators. For example:
```python
x = 4
x = x + 3
```
There is a small shortcut though to not need to write the `x` in the expression, available for the arithmetic operators.

```python3
x = 4
x += 3
x -= 1
x **= 4
...
```

It is also available for other types as well, such as strings:
```python
s = "Hello"
s += " World!"
```

### String operations and Integer conversion
Here are some string methods I often use in Python. For a more comprehensive list see the [Python Docs](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str):
- `startswith` and `endswith` return whether or not the string starts/ends with the given string. Ex. `"Hello World".startswith("Hello")` → `True`
- `upper` and `lower` return a string where all letters of the original string were turned to upper/lowercase. Ex. `"Hello".upper()`→`"HELLO"`
- `count` returns the number of occurrences of a substring in the string. Ex. `"abc123abcabc".count("abc")` → `3`
- `replace` replaces all occurrences of a substring by another string. Ex. `"Banana Boat".replace("a","o")` → `"Bonono Boot"`
- `split` returns a list of strings where each element was originally split by a given delimiter. The default delimiter is a space if none is specified. Ex. `"a,b,c".split(",")` → `["a", "b", "c"]`
- `join` joins a given list of strings using the string as a separator. Ex. `",".join(["a", "b", "c"])` → `"a,b,c"`
### Blocks of Code
Something else that's required for if statements is that all lines in the block are indented the same amount. Otherwise this will cause an error:

```python
# This is good
if a > 5:
    print("a is more than 5")
    print(a)

# This will give an IndentationError
if a > 5:
    print("a is more than 5") # 4 spaces
   print(a)                   # 3 spaces
```

Another, sometimes annoying, aspect of if statements is that there must be a statement inside of the if block. There may be times where you will not want a statement to run, for example if you are still working of the code that will run there. In this case, you can put it `pass` in the block as follows:

```python
if a > 5:
    pass
...
```

### A Mystery with Lists (and other objects)
A long time ago I ran into something unexpected. It is best demonstrated using the following:
```python
l = [1,2,3]
def myAppend(l,elem):
    l.append(elem)
myAppend(l,4)
print(l) # [1, 2, 3, 4]
```
What happened here. We passed in a list to the function, and even though it wasn't specified as global it still modified the list! The reason why: we used a method that modified the list. When you pass in a list or object, it is (likely, I haven't looked at the actual implementation) passed in as a reference to the original object. This means that using a method that updates that variable will update the original as well. This was not a problem with the number and string methods as they do not modify the original string (at least not the ones I have shown, maybe some do).

This can also become an issue when repeating lists. For example we can try to make a 2-dimensional list like this:
```python
l = [[]]*3
print(l) # [[],[],[]]
l[0].append(1)
print(l) # [[1],[1],[1]]
```
We see here that all three lists in `l` actually refer to the same list! This may be what we want, but not in this case. We can do this a different way using a loop:
```python
l = []
for i in range(3):
    l.append([])
l[0].append(1)
print(l) # [[1],[],[]]
```

### More Types to Look Into
There are two useful types that I use quite a bit. They are sets and dictionaries. A set is just a collection of values. The point is to hold a record of whether some value is in the set or not. A set will have no duplicates. We can make a set as follows:
```python
favouriteNumbers = {1,42,64}
emptySet = set()
```
We can add/remove items, and check whether they are in the set or not. We can also see how many items are in the set:
```python
favouriteNumbers.add(6)
favouriteNumbers.remove(42)
if 1 in favouriteNumbers:
    print("1 is a favourite number!")
print("I have", len(favouriteNumbers), "favourite numbers!")
```

Dictionaries are a mapping from one value, called a key, to another. This is analogous to a word dictionary where we have a word and its definition. We can make a dictionary as follows:
```python
numbers = {1: "one", 2: "two", 3: "three"}
emptyDict = {}
```

We can check if a key is in the dictionary, get what it maps to, and add/change the values to the dictionary:
```python
if 1 in numbers:
    print("1 in dictionary!")
print(numbers[1])
numbers[1] = "One" # update value
numbers[4] = "four" # new value
```

I recommend reading up a bit more about these types, but this should give you a good start.

### More on Function Arguments
You might have noticed that for some functions we have options as to how many arguments we pass in. `print` is the most obvious example, we can give it an arbitrary amount of arguments, 0, 10, 100, etc. Another is `input`, we can give it an optional prompt, but is not necessary. So how does Python do this?

Python actually has several types of arguments which I will refer to as positional, variadic and keyword arguments.
A Python function can have the following arguments:
```python
def f(arg1,arg2,...,defarg1=val1,defarg2=val2,...,*args,**kwargs):
    ... # note args and kwargs are just conventional names. You can call them whatever you want.
```
The positional arguments are all of the arguments from `arg1` up to but not including `*args`. `arg1`,`arg2`,... are the required positional arguments. You must pass values for these to be able to call the function. The `defarg1`... have a default value if none is specified. It is optional to pass a value for these. If you do want to pass a value you can do it like a normal positional value or directly specifying the argument name:
```python
def add(a, b=1, c=2):
    return a + b + c
print(add(1,2)) # 5 since b = 2
print(add(1,c=3)) # 5 since c = 3
```

The variadic and keyword arguments I will mention together. For these two we can specify an arbitrary number of arguments. Variadic args are passed in like a list, similar to how `print` works. Keyword arguments are passed in like explicitly setting the positional arguments explicitly. Variadic args are passed in as a tuple (you can treat it as a list that can't be modified) and keyword arguments as a dictionary.
```python
def f(*args, **kwargs):
    ...
f(1, 2, 3, "a"="1", "b"="2")
```
When passing in arguments, you must specify all positional arguments you want to give, then all variadic, and then all keyword arguments. If you have positional arguments with default values you have to give a value for each before any go to the variadic arguments.
### Function Definition and Recursion
Similar to variables, a function must be defined before it is used. Something to keep it mind is that a if you call a function inside another you are not using it immediately, it is only ever called when you run the second function (the one that's using the other one). This means that code like this is valid:
```python
def f(n):
    return 4 * g(n) + 3

def g(n):
    return n * n

print(f(2)) # 19
```
Another consequence is being able to call the the function inside of itself! This is called recursion, which I will not go into, but here is an [article](https://www.freecodecamp.org/news/recursion-is-not-hard-858a48830d83/) that goes over it.
An example of recursion is the following:

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)
```