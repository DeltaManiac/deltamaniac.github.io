---
id: z3nQKvaJ2yB7hqaRlslpO
title: Day 6
desc: ''
updated: 1609236479964
created: 1609235321198
nav_order: 6
---

# Probably a Fire Hazard

## Part I

Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at `0,0`, `0,999`, `999,999`, and `999,0`. The instructions include whether to `turn on`, `turn off`, or `toggle` various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like `0,0 through 2,2` therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

For example:

> `turn on 0,0 through 999,999` would turn on (or leave on) every light.
>
> `toggle 0,0 through 999,0` would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
>
> `turn off 499,499 through 500,500` would turn off (or leave off) the middle four lights.

After following the instructions, how many lights are lit?

## Solution


```rust
enum Action {
    On,
    Off,
    Toggle,
}

pub struct Instruction {
    start: (usize, usize),
    end: (usize, usize),
    action: Action,
}

#[aoc_generator(day6)]
pub fn input_to_struct(input: &str) -> Vec<Instruction> {
    input
        .lines()
        .map(|line| {
            let mut c = line.split_whitespace().rev();
            let mut d = c.next().unwrap().split(',');
            let end = (
                d.next().unwrap().parse::<usize>().unwrap(),
                d.next().unwrap().parse::<usize>().unwrap(),
            );
            c.next();
            let mut d = c.next().unwrap().split(',');
            let start = (
                d.next().unwrap().parse::<usize>().unwrap(),
                d.next().unwrap().parse::<usize>().unwrap(),
            );
            let action = match c.next().unwrap() {
                "on" => Action::On,
                "off" => Action::Off,
                "toggle" => Action::Toggle,
                _ => unreachable!(),
            };

            Instruction {
                start: start,
                end: end,
                action: action,
            }
        })
        .collect::<Vec<Instruction>>()
}

#[aoc(day6, part1)]
pub fn part1(input: &Vec<Instruction>) -> i64 {
    let mut switch: [[u8; 1000]; 1000] = [[0; 1000]; 1000];
    let mut count: i64 = 0;
    for x in input {
        for i in x.start.0..=x.end.0 {
            for j in x.start.1..=x.end.1 {
                match x.action {
                    Action::Off => {
                        if switch[i][j] == 1 {
                            count -= 1;
                            switch[i][j] = 0;
                        }
                    }
                    Action::On => {
                        if switch[i][j] == 0 {
                            count += 1;
                            switch[i][j] = 1;
                        }
                    }
                    Action::Toggle => {
                        if switch[i][j] == 0 {
                            count += 1;
                            switch[i][j] = 1;
                        } else {
                            count += -1;
                            switch[i][j] = 0;
                        }
                    }
                }
            }
        }
    }
    count
}
```

## Part II


You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

The phrase `turn on` actually means that you should increase the brightness of those lights by `1`.

The phrase `turn off` actually means that you should decrease the brightness of those lights by `1`, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of those lights by `2`.

What is the total brightness of all lights combined after following Santa's instructions?

For example:

> `turn on 0,0 through 0,0` would increase the total brightness by `1`.
>
> `toggle 0,0 through 999,999` would increase the total brightness by `2000000`.

## Solution

```rust
#[aoc(day6, part2)]
pub fn part2(input: &Vec<Instruction>) -> i64 {
    let mut switch: [[i16; 1000]; 1000] = [[0; 1000]; 1000];
    let mut bright: i64 = 0;
    for x in input {
        for i in x.start.0..=x.end.0 {
            for j in x.start.1..=x.end.1 {
                match x.action {
                    Action::Off => {
                        if switch[i][j] > 0 {
                            bright -= 1;
                            switch[i][j] -= 1;
                        }
                    }
                    Action::On => {
                        bright += 1;
                        switch[i][j] += 1;
                    }
                    Action::Toggle => {
                        bright += 2;
                        switch[i][j] += 2;
                    }
                }
            }
        }
    }
    bright
}
```
