---
id: kcHRJQyYTr5pNXNFRiWsi
title: Object Oriented Programming
desc: ''
updated: 1628038143807
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


| Syntax                                  | Special Method                                              |
|-----------------------------------------|-------------------------------------------------------------|
| a + b                                   | a.__add__(b) or b.__radd__(a)                               |
| a - b                                   | a.__sub__(b) or b.__rsub__(a)                               |
| a * b                                   | a.__mul__(b) or b.__rmul__(a)                               |
| a / b                                   | a.__truediv__(b) or b.__rtruediv__(a)                       |
| a // b                                  | a.__floordiv__(b) or b.__rfloordiv__(a)                     |
| a % b                                   | a.__mod__(b) or b.__rmod__(a)                               |
| a ** b                                  | a.__pow__(b) or b.__rpow__(a)                               |
| a << b                                  | a.__lshift__(b) or b.__rlshift__(a)                         |
| a >> b                                  | a.__rshift__(b) or b.__rrshift__(a)                         |
| a & b                                   | a.__and__(b) or b.__rand__(a)                               |
| a ^ b                                   | a.__xor__(b) or b.__rxor__(a)                               |
| a \| b                                  | a.__or__(b) or b.__ror__(a)                                 |
| a += b <br> a -= b <br> a *= b <br> ... | a.__iadd__(b) <br> a.__isub__(b) <br> a.__imul__(b)<br> ... |
| +a                                      | a.__pos__()                                                 |
| -a                                      | a.__neg__()                                                 |
| ~a                                      | a.__invert__()                                              |
| abs(a)                                  | a.__abs__()                                                 |
| a < b                                   | a.__lt__(b)                                                 |
| a <= b                                  | a.__le__(b)                                                 |
| a > b                                   | a.__gt__(b)                                                 |
| a >= b                                  | a.__ge__(b)                                                 |
| a == b                                  | a.__eq__(b)                                                 |
| a != b                                  | a.__ne__(b)                                                 |
| v in a                                  | a.__contains__(v)                                           |
| a[k]                                    | a.__getitem__(k)                                            |
| a[k]=v                                  | a.__setitem__(k,v)                                          |
| del a[k]                                | a.__delitem__(k)                                            |
| a(arg1, arg2)                           | a.__call__(arg1,arg2)                                       |
| len(a)                                  | a.__len__()                                                 |
| hash(a)                                 | a.__hash__()                                                |
| iter(a)                                 | a.__iter__()                                                |
| next(a)                                 | a.__next__()                                                |
| bool(a)                                 | a.__bool__()                                                |
| float(a)                                | a.__float__()                                               |
| int(a)                                  | a.__int__()                                                 |
| repr(a)                                 | a.__repr__()                                                |
| reversed(a)                             | a.__reversed__()                                            |
| str(a)                                  | a.__str__()                                                 |


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