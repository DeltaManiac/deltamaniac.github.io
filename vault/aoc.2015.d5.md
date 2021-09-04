---
id: qiqmYUbwRjOhJPc3wLO3B
title: Day 5
desc: ''
updated: 1609223448432
created: 1609222547165
nav_order: 5
---
## Doesn't He Have Intern-Elves For This?

## Part I

Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

> It contains at least three vowels (`aeiou` only), like `aei`, `xazegov`, or `aeiouaeiouaeiou`.
>
> It contains at least one letter that appears twice in a row, like `xx`, `abcdde` (`dd`), or `aabbccdd` (`aa`, `bb`, `cc`, or `dd`).
>
> It does not contain the strings `ab`, `cd`, `pq`, or `xy`, even if they are part of one of the other requirements.

For example:

> `ugknbfddgicrmopn` is nice because it has at least three vowels (`u...i...o...`), a double letter (`...dd...`), and none of the disallowed substrings.
>
> `aaa` is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
>
> `jchzalrnumimnmhp` is naughty because it has no double letter.
>
> `haegwjzuvuyypxyu` is naughty because it contains the string xy.
>
> `dvszwmarrgswjxmb` is naughty because it contains only one vowel.

How many strings are nice?

## Solution

Iterating the input line by line we can pass it through filters which would apply the conditions so as to eliminate all strings that are not `nice`.

The answer is the count of all the remaining strings.

```rust
#[aoc(day5, part1)]
pub fn part1(input: &str) -> usize {
    input
        .lines()
        .filter(|w| !(w.contains("ab") || w.contains("cd") || w.contains("pq") || w.contains("xy")))
        .filter(|x| {
            x.chars()
                .filter(|c| *c == 'a' || *c == 'e' || *c == 'i' || *c == 'o' || *c == 'u')
                .count()
                > 2
        })
        .filter(|y| {
            let mut c = y.chars().collect::<Vec<char>>();
            let l = c.len();
            c.dedup();
            l != c.len()
        })
        .count()
}
```

## Part II

Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

> It contains a pair of any two letters that appears at least twice in the string without overlapping, like `xyxy` (`xy`) or `aabcdefgaa` (`aa`), but not like `aaa` (`aa`, but it overlaps).
>
> It contains at least one letter which repeats with exactly one letter between them, like `xyx`, `abcdefeghi` (`efe`), or even `aaa`.

For example:

> `qjhvhtzxzqqjkmpb` is nice because is has a pair that appears twice (`qj`) and a letter that repeats with exactly one letter between them (`zxz`).
>
> `xxyxx` is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
>
> `uurcxstgmygtbstg` is naughty because it has a pair (`tg`) but no repeat with a single letter between them.
>
> `ieodomkazucvgmuy` is naughty because it has a repeating letter with one between (`odo`), but no pair that appears twice.

How many strings are nice under these new rules?

## Solution

A recursive function `repeat_xx` provides the check for condition we then filter out on the strings that match.

The answer is the count of all the remaining strings after the filters have been applied.

```rust
fn repeat_xx(string: &str) -> bool {
    if string.len() < 4 {
        return false;
    }

    let pair = &string[0..2];
    let remain = &string[2..];

    remain.contains(pair) || repeat_xx(&string[1..])
}

#[aoc(day5, part2)]
pub fn part2(input: &str) -> usize {
    input
        .lines()
        .filter(|y| repeat_xx(y))
        .filter(|z| z.chars().zip(z.chars().skip(2)).any(|(a, b)| a == b))
        .count()
}
```

