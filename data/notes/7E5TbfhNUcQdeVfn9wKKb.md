
Interpreted Language

Object Oriented

## Built Ins

| Class     | Desc                                 | Immutable |
|-----------|--------------------------------------|-----------|
| bool      | boolean value                        | True      |
| int       | integer (arbitrary magnitude)        | True      |
| float     | floating-point number                | True      |
| list      | mutable sequence of objects          | False     |
| tuple     | immutable sequence of objects        | True      |
| str       | character string                     | True      |
| set       | unordered set of distinct objects    | False     |
| frozenset | immutable form of set class          | True      |
| dict      | associative mapping (aka dictionary) | False     |

## Bool

Numbers evaluate to False if 0

Sequences Strings Lists Dicts to False if empty

## int

The `int()` constructor returns 0 by default

int(3.14) -> 3

int(-123.3) -> -123

int('5442') -> 5442 : Automatic handling of `atoi`

int('lol')  -> ValueError

int('7f',16) -> 127 ->int(strval,base)

## float

fixed-precision representation

Similar to Double in cpp

The `float()` constructor returns 0 by default

float(2) -> 2.0

float('3.14') -> 3.14

float('meh') -> ValueError

## Sequence Types

- **list** -> array
- **tuple** -> immutable list
- **str** -> immutable sequence of char

### list

- Stores sequence of objects
- Referential Structure -> stores sequence of references to its elements
- zero-indexed

The `list()` constructor produces empty list [ ] by default

The `list()` constructor will accept any parameter that is of **iterable** type

list('hello') -> [h,e,l,l,o]

## set and frozenset

- unordered collection of elements without duplicate
- optimized to check existence of elements -> hashtable
- accepts only immutable types

The `set()` constructor produces an empty set

set('hello') -> { h,e,l,o}

## dicts

mapping of distinct keys to associated values

## Operator precedence

| Type                                                   | Symbol                                                                |
|--------------------------------------------------------|-----------------------------------------------------------------------|
| member access                                          | expr.member                                                           |
| function/method calls <br> container subscripts/slices | expr(...) <br> expr[...]                                              |
| exponentiation                                         | **                                                                    |
| unary operators                                        | +expr, −expr,  ~expr                                              |
| multiplication, division                               | *, /, //, %                                                           |
| addition, subtraction                                  | +, −                                                                  |
| bitwise shifting                                       | <<, >>                                                                |
| bitwise-and                                            | &                                                                     |
| bitwise-xor                                            | ˆ                                                                     |
| bitwise-or                                             | \|                                                                    |
| comparisons <br>  containment                          | **is**, **is** **not**, ==, !=, <, <=, >, >= <br> **in**,** not in ** |
| logical-not                                            | **not** expr                                                          |
| logical-and                                            | **and**                                                               |
| logical-or                                             | **or**                                                                |
| conditional                                            | val1 **if** cond **else** val2                                        |
| assignments                                            | =, +=, −=, =, etc                                                     |

## Built-In Functions

| Call Syntax               | Description                                                                                                               |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------|
| abs(x)                    | Return the absolute value of a number.                                                                                    |
| all(iterable)             | Return True if bool(e) is True for each element e.                                                                        |
| any(iterable)             | Return True if bool(e) is True for at least one element e.                                                                |
| chr(integer)              | Return a one-character string with the given Unicode code point.                                                          |
| divmod(x, y)              | Return (x // y, x % y) as tuple, if x and y are integers.                                                                 |
| hash(obj)                 | Return an integer hash value for the object (see Chapter 10).                                                             |
| id(obj)                   | Return the unique integer serving as an “identity” for the object.                                                        |
| input(prompt)             | Return a string from standard input; the prompt is optional.                                                              |
| isinstance(obj, cls)      | Determine if obj is an instance of the class (or a subclass).                                                             |
| iter(iterable)            | Return a new iterator object for the parameter (see Section 1.8).                                                         |
| len(iterable)             | Return the number of elements in the given iteration.                                                                     |
| map(f, iter1, iter2, ...) | Return an iterator yielding the result of function calls f(e1, e2, ...) for respective elements e1 ∈iter1, e2 ∈iter2, ... |
| max(iterable)             | Return the largest element of the given iteration.                                                                        |
| max(a, b, c, ...)         | Return the largest of the arguments.                                                                                      |
| min(iterable)             | Return the smallest element of the given iteration.                                                                       |
| min(a, b, c, ...)         | Return the smallest of the arguments.                                                                                     |
| next(iterator)            | Return the next element reported by the iterator (see Section 1.8).                                                       |
| open(filename, mode)      | Open a file with the given name and access mode.                                                                          |
| ord(char)                 | Return the Unicode code point of the given character.                                                                     |
| pow(x, y)                 | Return the value xy (as an integer if x and y are integers);<br> equivalent to x**y.                                      |
| pow(x, y, z)              | Return the value (xy mod z) as an integer.                                                                                |
| print(obj1, obj2, ...)    | Print the arguments, with separating spaces and trailing newline.                                                         |
| range(stop)               | Construct an iteration of values 0, 1, . . . ,  stop −1.                                                                  |
| range(start, stop)        | Construct an iteration of values start, start + 1, . . . ,  stop −1.                                                      |
| range(start, stop, step)  | Construct an iteration of values start, start + step, start + 2 step, . . .                                               |
| reversed(sequence)        | Return an iteration of the sequence in reverse.                                                                           |
| round(x)                  | Return the nearest int value (a tie is broken toward the even value).                                                     |
| round(x, k)               | Return the value rounded to the nearest 10−k (return-type matches x).                                                     |
| sorted(iterable)          | Return a list containing elements of the iterable in sorted order.                                                        |
| sum(iterable)             | Return the sum of the elements in the iterable (must be numeric).                                                         |
| type(obj)                 | Return the class to which the instance obj belongs.                                                                       |
