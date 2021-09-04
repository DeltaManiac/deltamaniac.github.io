---
id: bKosBjYdFUM5XpRKYA0MT
title: Object Oriented Programming
desc: ''
updated: 1628100102303
created: 1628035170150
nav_order: 2
---

# Classes

## Sample

```python
class CreditCard:
 """ A CC for consumer """
    def __init__(self,customer,bank,acn,limit):
        self._customer = customer
        self._bank = bank
        self._account = acn
        self._limit = limit

    def get_customer(self):
        return self._customer

    def make_payment(self,amount):
        self.account -= amount
```

## Special Methods


| Syntax                                  | Special Method                                                    |
|-----------------------------------------|-------------------------------------------------------------------|
| a + b                                   | a.\__add\\__(b) or b.\__radd\\__(a)                               |
| a - b                                   | a.\__sub\\__(b) or b.\__rsub\__(a)                                |
| a * b                                   | a.\__mul\__(b) or b.\__rmul\__(a)                                 |
| a / b                                   | a.\__truediv\__(b) or b.\__rtruediv\__(a)                         |
| a // b                                  | a.\__floordiv\__(b) or b.\__rfloordiv\__(a)                       |
| a % b                                   | a.\__mod\__(b) or b.\__rmod\__(a)                                 |
| a ** b                                  | a.\__pow\__(b) or b.\__rpow\__(a)                                 |
| a << b                                  | a.\__lshift\__(b) or b.\__rlshift\__(a)                           |
| a >> b                                  | a.\__rshift\__(b) or b.\__rrshift\__(a)                           |
| a & b                                   | a.\__and\__(b) or b.\__rand\__(a)                                 |
| a ^ b                                   | a.\__xor\__(b) or b.\__rxor\__(a)                                 |
| a \| b                                  | a.\__or\__(b) or b.\__ror\__(a)                                   |
| a += b <br> a -= b <br> a *= b <br> ... | a.\__iadd\__(b) <br> a.\__isub\__(b) <br> a.\__imul\__(b)<br> ... |
| +a                                      | a.\__pos\__()                                                     |
| -a                                      | a.\__neg\__()                                                     |
| ~a                                      | a.\__invert\__()                                                  |
| abs(a)                                  | a.\__abs\__()                                                     |
| a < b                                   | a.\__lt\__(b)                                                     |
| a <= b                                  | a.\__le\__(b)                                                     |
| a > b                                   | a.\__gt\__(b)                                                     |
| a >= b                                  | a.\__ge\__(b)                                                     |
| a == b                                  | a.\__eq\__(b)                                                     |
| a != b                                  | a.\__ne\__(b)                                                     |
| v in a                                  | a.\__contains\__(v)                                               |
| a[k]                                    | a.\__getitem\__(k)                                                |
| a[k]=v                                  | a.\__setitem\__(k,v)                                              |
| del a[k]                                | a.\__delitem\__(k)                                                |
| a(arg1, arg2)                           | a.\__call\__(arg1,arg2)                                           |
| len(a)                                  | a.\__len\__()                                                     |
| hash(a)                                 | a.\__hash\__()                                                    |
| iter(a)                                 | a.\__iter\__()                                                    |
| next(a)                                 | a.\__next\__()                                                    |
| bool(a)                                 | a.\__bool\__()                                                    |
| float(a)                                | a.\__float\__()                                                   |
| int(a)                                  | a.\__int\__()                                                     |
| repr(a)                                 | a.\__repr\__()                                                    |
| reversed(a)                             | a.\__reversed\__()                                                |
| str(a)                                  | a.\__str\__()                                                     |


## Operator Overloading

```python
class Vector:

    def __init__(self,d):
        self._coords = [0] * d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self,j):
        return self._coords[j]

    def __setitem__(self,j,val):
        self._coords[j] = val

    def __add__(self,other):
        if len(self) != len(other):
            raise ValurError('Dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self,other):
        self._coords == other._coords

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return '<' + str(self._coords)[1:-1] +'>'

```

## Iterators
