## Day 12: JSAbacusFramework.io

# Part I

Santa's Accounting-Elves need help balancing the books after a recent order. Unfortunately, their accounting software uses a peculiar storage format. That's where you come in.

They have a JSON document which contains a variety of things: arrays (`[1,2,3]`), objects (`{"a":1, "b":2}`), numbers, and strings.

 Your first job is to simply find all of the numbers throughout the document and add them together.

For example:

> `[1,2,3]` and `{"a":2,"b":4}` both have a sum of `6`.
>
> `[[[3]]] and {"a":{"b":4},"c":-1}` both have a sum of `3`.
>
> `{"a":[-1,1]} and [-1,{"a":1}]` both have a sum of `0`.
>
> `[]` and `{}` both have a sum of `0`.

You will not encounter any strings containing numbers.

What is the sum of all numbers in the document?

## Solution

## Without Serde

```rust
pub fn part1(input: &str) -> i32 {
    let mut value = 0i32;
    let mut tmp_val = 0i32;
    let mut last: char = '\x00';
    let mut multiplier = 1;
    for ch in input.chars() {
        value += match ch {
            '0'...'9' => {
                if last == '-' {
                    multiplier = -1;
                }
                tmp_val = tmp_val * 10
                    + match ch.to_string().parse::<i32>() {
                        Ok(x) => x,
                        Err(e) => panic!("Help! {}", e),
                    };

                0
            }
            _ if last.is_digit(10) => {
                let tmp = tmp_val * multiplier;
                tmp_val = 0;
                multiplier = 1;

                tmp
            }
            _ => 0,
        };
        last = ch;
    }
    value
}
```

### With Serde

```rust
fn sum(v: Value, use_red: bool) -> i64 {
    match v {
        Value::Null => 0,
        Value::Bool(_) => 0,
        Value::Number(n) => n.as_i64().unwrap(),
        Value::String(_) => 0,
        Value::Array(v) => v.into_iter().map(|e| sum(e, use_red)).sum(),
        Value::Object(v) => {
            let mut max = 0;
            for v in v.values() {
                if (v == "red") && !use_red {
                    return 0;
                }
                max += sum(v.clone(), use_red);
            }
            return max;
        }
    }
}

#[aoc(day11, part1, Serde)]
pub fn part1_serde(input: &str) -> i64 {
    let a = serde_json::from_str(&input).unwrap();
    sum(a, true)
}

```

## Part II

Uh oh - the Accounting-Elves have realized that they double-counted everything red.

Ignore any object (and all of its children) which has any property with the value `"red"`. Do this only for objects (`{...}`), not arrays (`[...]`).

> [1,2,3] still has a sum of 6.
>
> [1,{"c":"red","b":2},3] now has a sum of 4, because the middle object is ignored.
>
> {"d":"red","e":[1,2,3,4],"f":5} now has a sum of 0, because the entire structure is ignored.
>
> [1,"red",5] has a sum of 6, because "red" in an array has no effect.

## Solution

```rust
fn sum(v: Value, use_red: bool) -> i64 {
    match v {
        Value::Null => 0,
        Value::Bool(_) => 0,
        Value::Number(n) => n.as_i64().unwrap(),
        Value::String(_) => 0,
        Value::Array(v) => v.into_iter().map(|e| sum(e, use_red)).sum(),
        Value::Object(v) => {
            let mut max = 0;
            for v in v.values() {
                if (v == "red") && !use_red {
                    return 0;
                }
                max += sum(v.clone(), use_red);
            }
            return max;
        }
    }
}

#[aoc(day11, part2, Serde)]
pub fn part2_serde(input: &str) -> i64 {
    let a = serde_json::from_str(&input).unwrap();
    sum(a, false)
}
```

