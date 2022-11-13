## Classes

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

| Syntax                                   | Special Method                                                          |
| ---------------------------------------- | ----------------------------------------------------------------------- |
| a + b                                    | a.\_\_add\\**(b) or b.\_\_radd\\**(a)                                   |
| a - b                                    | a.\_\_sub\\\_\_(b) or b.\_\_rsub\_\_(a)                                 |
| a \* b                                   | a.\_\_mul\_\_(b) or b.\_\_rmul\_\_(a)                                   |
| a / b                                    | a.\_\_truediv\_\_(b) or b.\_\_rtruediv\_\_(a)                           |
| a // b                                   | a.\_\_floordiv\_\_(b) or b.\_\_rfloordiv\_\_(a)                         |
| a % b                                    | a.\_\_mod\_\_(b) or b.\_\_rmod\_\_(a)                                   |
| a \*\* b                                 | a.\_\_pow\_\_(b) or b.\_\_rpow\_\_(a)                                   |
| a &lt;&lt; b                             | a.\_\_lshift\_\_(b) or b.\_\_rlshift\_\_(a)                             |
| a >> b                                   | a.\_\_rshift\_\_(b) or b.\_\_rrshift\_\_(a)                             |
| a & b                                    | a.\_\_and\_\_(b) or b.\_\_rand\_\_(a)                                   |
| a ^ b                                    | a.\_\_xor\_\_(b) or b.\_\_rxor\_\_(a)                                   |
| a \| b                                   | a.\_\_or\_\_(b) or b.\_\_ror\_\_(a)                                     |
| a += b <br> a -= b <br> a \*= b <br> ... | a.\_\_iadd\_\_(b) <br> a.\_\_isub\_\_(b) <br> a.\_\_imul\_\_(b)<br> ... |
| +a                                       | a.\_\_pos\_\_()                                                         |
| -a                                       | a.\_\_neg\_\_()                                                         |
| ~a                                       | a.\_\_invert\_\_()                                                      |
| abs(a)                                   | a.\_\_abs\_\_()                                                         |
| a &lt; b                                 | a.\_\_lt\_\_(b)                                                         |
| a &lt;= b                                | a.\_\_le\_\_(b)                                                         |
| a > b                                    | a.\_\_gt\_\_(b)                                                         |
| a >= b                                   | a.\_\_ge\_\_(b)                                                         |
| a == b                                   | a.\_\_eq\_\_(b)                                                         |
| a != b                                   | a.\_\_ne\_\_(b)                                                         |
| v in a                                   | a.\_\_contains\_\_(v)                                                   |
| a[k]                                     | a.\_\_getitem\_\_(k)                                                    |
| a[k]=v                                   | a.\_\_setitem\_\_(k,v)                                                  |
| del a[k]                                 | a.\_\_delitem\_\_(k)                                                    |
| a(arg1, arg2)                            | a.\_\_call\_\_(arg1,arg2)                                               |
| len(a)                                   | a.\_\_len\_\_()                                                         |
| hash(a)                                  | a.\_\_hash\_\_()                                                        |
| iter(a)                                  | a.\_\_iter\_\_()                                                        |
| next(a)                                  | a.\_\_next\_\_()                                                        |
| bool(a)                                  | a.\_\_bool\_\_()                                                        |
| float(a)                                 | a.\_\_float\_\_()                                                       |
| int(a)                                   | a.\_\_int\_\_()                                                         |
| repr(a)                                  | a.\_\_repr\_\_()                                                        |
| reversed(a)                              | a.\_\_reversed\_\_()                                                    |
| str(a)                                   | a.\_\_str\_\_()                                                         |

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

