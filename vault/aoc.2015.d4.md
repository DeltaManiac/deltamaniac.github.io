---
id: owOmNHbs0ZFkz2ipLXGHE
title: Day 4
desc: ''
updated: 1609223131083
created: 1609156334056
nav_order: 4
---
## The Ideal Stocking Stuffer

## Part I

Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: `1`, `2`, `3`, ...) that produces such a hash.

For example:

> If your secret key is `abcdef`, the answer is `609043`, because the MD5 hash of `abcdef609043` starts with five zeroes (`000001dbbfa...`), and it is the lowest such number to do so.
>
> If your secret key is `pqrstuv`, the lowest number it combines with to make an MD5 hash starting with five zeroes is `1048970`; that is, the MD5 hash of `pqrstuv1048970` looks like `000006136ef....`

## Solution

Brute forcing would be the easiest way to find the solution.

Taking the input we iterate from 1 to the max u32 using `i` and append it to the input.

This would be the content for which we compute the`md5Sum` and check if it starts with five zeroes.

```rust
use md5;

#[aoc(day4, part1)]
pub fn solve_part1(input: &str) -> u32 {
    (1..)
        .filter(|i| format!("{:x}", md5::compute(format!("{}{}", input, i))).starts_with("00000"))
        .next()
        .unwrap()
}
```

## Part II

Now find one that starts with six zeroes.

## Solution

A small change from `.starts_with("00000")` to `.starts_with("000000")` provides the answer.

```rust
#[aoc(day4, part2)]
pub fn solve_part2(input: &str) -> i32 {
    (1..)
        .filter(|i| format!("{:x}", md5::compute(format!("{}{}", input, i))).starts_with("000000"))
        .next()
        .unwrap()
}
```

