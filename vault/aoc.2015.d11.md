---
id: 1bd833a4-2735-45bc-80b0-d7fe5e62c96c
title: Day 11
desc: ''
updated: 1609240548729
created: 1609240107099
---
# Corporate Policy

## Part I
Santa's previous password expired, and he needs help choosing a new one.

To help him remember his new password after the old one expires, Santa has devised a method of coming up with a password based on the previous one. Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons), so he finds his new password by incrementing his old password string repeatedly until it is valid.

Incrementing is just like counting with numbers: `xx`, `xy`, `xz`, `ya`, `yb`, and so on. Increase the rightmost letter one step; if it was z, it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.

Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:

>Passwords must include one increasing straight of at least three letters, like `abc`, `bcd`, `cde`, and so on, up to `xyz`. They cannot skip letters; `abd` doesn't count.
>
>Passwords may not contain the letters `i`, `o`, or `l`, as these letters can be mistaken for other characters and are therefore confusing.
>
>Passwords must contain at least two different, non-overlapping pairs of letters, like `aa`, `bb`, or `zz`.

For example:

>`hijklmmn` meets the first requirement (because it contains the straight `hij`) but fails the second requirement requirement (because it contains `i` and `l`).
>
>`abbceffg` meets the third requirement (because it repeats `bb` and `ff`) but fails the first requirement.
>
>`abbcegjk` fails the third requirement, because it only has one double letter (`bb`).
>
>The next password after `abcdefgh` is `abcdffaa`.
>
>The next password after `ghijklmn` is `ghjaabcc`, because you eventually skip all the passwords that start with `ghi...`, since `i` is not allowed.

Given Santa's current password (your puzzle input), what should his next password be?

## Solution
```rust
fn condition_3(string: &str) -> bool {
    !string.chars().any(|c| match c {
        'i' | 'o' | 'l' => true,
        _ => false,
    })
}

fn condition_2(string: &str) -> bool {
    string
        .as_bytes()
        .windows(3)
        .any(|w| w[0] + 1 == w[1] && w[1] + 1 == w[2])
}

fn condition_1(string: &str) -> bool {
    let a = string.as_bytes().iter();
    let b = string.as_bytes()[1..].iter();
    let mut i = a.zip(b);
    let mut c = 0;
    while c < 2 {
        if let Some((x, y)) = i.next() {
            if x == y {
                c += 1;
                i.next();
                i.next();
            }
        } else {
            break;
        }
    }
    c >= 2
}

fn next(string: &str) -> String {
    let mut result = String::new();
    for (i, c) in string.chars().rev().enumerate() {
        match c {
            'z' => result.push('a'),
            _ => {
                result.push(((c as u8) + 1) as char);
                result.extend(
                    string
                        .chars()
                        .rev()
                        .skip(i + 1)
                        .take(string.len() - i)
                        .collect::<Vec<_>>(),
                );
                break;
            }
        }
    }
    result.chars().rev().collect::<String>()
}

#[aoc(day11, part1)]
pub fn part1(input: &str) -> String {
    let mut password = input.to_string();

    while !(condition_1(&password) && condition_3(&password) && condition_2(&password)) {
        password = next(&password);
    }
    password
}
```
## Part II

Santa's password expired again. What's the next one?

```rust
#[aoc(day11, part2)]
pub fn part2(input: &str) -> String {
    let mut password = part1(input);
    password = next(&password);
    while !(condition_1(&password) && condition_3(&password) && condition_2(&password)) {
        password = next(&password);
    }
    password
}
```