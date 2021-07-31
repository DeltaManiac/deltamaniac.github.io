---
id: c326423e-90f9-46ef-a806-85d050741da2
title: Day 10
desc: ''
updated: 1609240088330
created: 1609239663124
nav_order: 10
---

# Elves Look, Elves Say

## Part I

Today, the Elves are playing a game called look-and-say. They take turns making sequences by reading aloud the previous sequence and using that reading as the next sequence. For example, 211 is read as "one two, two ones", which becomes `1221` (`1` `2`, `2` `1`s).

Look-and-say sequences are generated iteratively, using the previous value as input for the next step. For each step, take the previous value, and replace each run of digits (like `111`) with the number of digits (`3`) followed by the digit itself (`1`).

For example:

>`1` becomes `11` (`1` copy of digit `1`).
>
>`11` becomes `21` (`2` copies of digit `1`).
>
>`21` becomes `1211` (one `2` followed by one `1`).
>
>`1211` becomes `111221` (one `1`, one `2`, and two `1`s).
>
>`111221` becomes `312211` (three `1`s, two `2`s, and one `1`).

Starting with the digits in your puzzle input, apply this process 40 times.

 What is the length of the result?

## Solution

```rust
#[aoc(day10, part1)]
pub fn part1(input: &str) -> usize {
    let mut s = input.to_string();
    for _ in 0..40 {
        let mut v: Vec<(u16, char)> = Vec::new();
        let mut iter = s.chars();
        let mut curr = (1, iter.next().unwrap());
        for i in iter {
            if i != curr.1 {
                v.push(curr);
                curr = (1, i);
            } else {
                curr.0 += 1;
            }
        }
        v.push(curr);
        s.clear();
        for i in v {
            s.push_str(&i.0.to_string());
            s.push(i.1)
        }
    }
    s.chars().count()
}
```
## Part II

Neat, right? You might also enjoy hearing John Conway talking about this sequence (that's Conway of Conway's Game of Life fame).

Now, starting again with the digits in your puzzle input, apply this process 50 times. What is the length of the new result?

## Solution

```rust
#[aoc(day10, part2)]
pub fn part2(input: &str) -> usize {
    let mut s = input.to_string();
    for _ in 0..50 {
        let mut v: Vec<(u16, char)> = Vec::new();
        let mut iter = s.chars();
        let mut curr = (1, iter.next().unwrap());
        for i in iter {
            if i != curr.1 {
                v.push(curr);
                curr = (1, i);
            } else {
                curr.0 += 1;
            }
        }
        v.push(curr);
        s.clear();
        for i in v {
            s.push_str(&i.0.to_string());
            s.push(i.1)
        }
    }
    s.chars().count()
}
```
