---
id: xyhWsTJOM1CdKck9dPGZw
title: Day 7
desc: ''
updated: 1609238679234
created: 1609236534979
nav_order: 7
---

# Some Assembly Required

## Part I

This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from `0` to `65535`). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together: `x AND y -> z` means to connect wires `x` and `y` to an AND gate, and then connect its output to wire `z`.

For example:

>`123 -> x` means that the signal 123 is provided to wire `x`.
>
>`x AND y -> z` means that the bitwise AND of wire `x` and wire `y` is provided to wire `z`.
>
>`p LSHIFT 2 -> q` means that the value from wire `p` is left-shifted by `2` and then provided to wire `q`.
>
>`NOT e -> f` means that the bitwise complement of the value from wire `e` is provided to wire `f`.

Other possible gates include `OR` (bitwise OR) and `RSHIFT` (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

For example, here is a simple circuit:
```
123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
```

After it is run, these are the signals on the wires:

```
d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456
```

In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire `a`?

## Solution
```rust
use std::collections::HashMap;
#[derive(Debug)]
pub enum Gate {
    Value(u16, String),
    Source(String, String),
    And(String, String, String),
    AndValue(u16, String, String),
    Or(String, String, String),
    LShift(String, u16, String),
    RShift(String, u16, String),
    Not(String, String),
}

#[aoc_generator(day7)]
pub fn input_to_struct(input: &str) -> Vec<Gate> {
    input
        .lines()
        .map(|line| {
            let words = line.split_whitespace().collect::<Vec<_>>();
            if words[0] == "NOT" {
                Gate::Not(words[1].to_string(), words[3].to_string())
            } else if words[1] == "LSHIFT" {
                Gate::LShift(
                    words[0].to_string(),
                    words[2].to_string().trim().parse::<u16>().unwrap(),
                    words[4].to_string(),
                )
            } else if words[1] == "RSHIFT" {
                Gate::RShift(
                    words[0].to_string(),
                    words[2].to_string().trim().parse::<u16>().unwrap(),
                    words[4].to_string(),
                )
            } else if words[0].to_string().trim().parse::<i64>().is_ok() && words[1] == "AND" {
                Gate::AndValue(
                    words[0].to_string().trim().parse::<u16>().unwrap(),
                    words[2].to_string(),
                    words[4].to_string(),
                )
            } else if words[1] == "AND" {
                Gate::And(
                    words[0].to_string(),
                    words[2].to_string(),
                    words[4].to_string(),
                )
            } else if words[1] == "OR" {
                Gate::Or(
                    words[0].to_string(),
                    words[2].to_string(),
                    words[4].to_string(),
                )
            } else if words[0].to_string().trim().parse::<i64>().is_ok() && words[1] == "->" {
                Gate::Value(
                    words[0].to_string().trim().parse::<u16>().unwrap(),
                    words[2].to_string(),
                )
            } else if words[1] == "->" {
                Gate::Source(words[0].to_string(), words[2].to_string())
            } else {
                unreachable!()
            }
        })
        .collect::<Vec<Gate>>()
}

fn solve_circuit(gates: &[Gate], values: &mut HashMap<String, u16>) -> HashMap<String, u16> {
    let mut unresolved = true;
    let constants = values.clone();
    while unresolved {
        let values_prev = values.clone();
        gates.iter().for_each(|item| {
            for (k, v) in &constants {
                values.insert(k.clone(), *v);
            }
            match item {
                Gate::Value(ref num, ref dst) => {
                    values.insert(dst.to_string(), *num);
                }
                Gate::Source(ref src0, ref dst) => {
                    if values.contains_key(src0) {
                        let v0 = *values.get(src0).unwrap();
                        values.insert(dst.to_string(), v0);
                    }
                }
                Gate::And(ref src0, ref src1, ref dst) => {
                    if values.contains_key(src0) && values.contains_key(src1) {
                        let v0 = *values.get(src0).unwrap();
                        let v1 = *values.get(src1).unwrap();
                        values.insert(dst.to_string(), v0 & v1);
                    }
                }
                Gate::AndValue(ref v0, ref src1, ref dst) => {
                    if values.contains_key(src1) {
                        let v1 = *values.get(src1).unwrap();
                        values.insert(dst.to_string(), *v0 & v1);
                    }
                }
                Gate::Or(ref src0, ref src1, ref dst) => {
                    if values.contains_key(src0) && values.contains_key(src1) {
                        let v0 = *values.get(src0).unwrap();
                        let v1 = *values.get(src1).unwrap();
                        values.insert(dst.to_string(), v0 | v1);
                    }
                }
                Gate::LShift(ref src0, ref num, ref dst) => {
                    if values.contains_key(src0) {
                        let v0 = *values.get(src0).unwrap();
                        values.insert(dst.to_string(), v0 << *num);
                    }
                }
                Gate::RShift(ref src0, ref num, ref dst) => {
                    if values.contains_key(src0) {
                        let v0 = *values.get(src0).unwrap();
                        values.insert(dst.to_string(), v0 >> *num);
                    }
                }
                Gate::Not(ref src0, ref dst) => {
                    if values.contains_key(src0) {
                        let v0 = *values.get(src0).unwrap();
                        values.insert(dst.to_string(), !v0);
                    }
                }
            }
            unresolved = values_prev != *values;
        });
    }
    values.clone()
}

#[aoc(day7, part1)]
pub fn part1(input: &[Gate]) -> u16 {
    *solve_circuit(input, &mut HashMap::new()).get("a").unwrap()
}
```

## Part II

Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a).

What new signal is ultimately provided to wire `a`?

## Solution

```rust
#[aoc(day7, part2)]
pub fn part2(input: &[Gate]) -> u16 {
    let mut map = HashMap::new();
    map.insert(
        "b".to_string(),
        *solve_circuit(&input, &mut HashMap::new()).get("a").unwrap(),
    );
    *solve_circuit(&input, &mut map).get("a").unwrap()
}
```
