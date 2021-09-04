---
id: VeoZxynLIY90RkDY4qSQa
title: Day 9
desc: ''
updated: 1609239564760
created: 1609239266974
nav_order: 9
---
## All in a Single Night

## Part I

Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?

For example, given the following distances:

```
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
```

The possible routes are therefore:

```
Dublin -> London -> Belfast = 982
London -> Dublin -> Belfast = 605
London -> Belfast -> Dublin = 659
Dublin -> Belfast -> London = 659
Belfast -> Dublin -> London = 605
Belfast -> London -> Dublin = 982
```

The shortest of these is `London -> Dublin -> Belfast = 605`, and so the answer is `605` in this example.

What is the distance of the shortest route?

## Solution

```rust
use std::collections::HashMap;

struct Graph<'a> {
    nodes: Vec<&'a str>,
    edges: HashMap<(&'a str, &'a str), u16>,
}

impl<'a> Graph<'a> {
    fn new() -> Graph<'a> {
        Graph {
            nodes: Vec::new(),
            edges: HashMap::new(),
        }
    }

    fn permutations<'b>(collection: &[&'b str]) -> Vec<Vec<&'b str>> {
        if collection.len() == 1 {
            return vec![vec![collection[0]]];
        }
        let mut result = vec![];
        for el in collection {
            for tail in Self::permutations(
                &collection
                    .iter()
                    .filter(|x| *x != el)
                    .copied()
                    .collect::<Vec<&'b str>>(),
            ) {
                let mut whole = vec![*el];
                whole.extend(tail);
                result.push(whole.clone())
            }
        }
        result
    }

    fn cheapest(&self) -> u16 {
        Graph::permutations(self.nodes.clone().as_ref())
            .iter()
            .map(|x| {
                let mut last = "";
                x.iter().fold(0, |tot, node| {
                    if last != "" && last != *node {
                        let price = &self.edges[&(last, *node)];
                        last = node;
                        tot + price
                    } else {
                        last = node;
                        tot
                    }
                })
            })
            .min()
            .unwrap()
    }
}

fn input_to_graph(input: &str) -> Graph {
    let mut graph = Graph::new();
    input.lines().for_each(|line| {
        let mut w = line.split_whitespace();
        let s = w.next().unwrap();
        w.next();
        let d = w.next().unwrap();
        w.next();
        let l = w.next().unwrap().to_string().parse::<u16>().unwrap();
        if !graph.nodes.contains(&s) {
            graph.nodes.push(s);
        }
        if !graph.nodes.contains(&d) {
            graph.nodes.push(d);
        }
        graph.edges.insert((s, d), l);
        graph.edges.insert((d, s), l);
    });
    graph
}

#[aoc(day9, part1)]
pub fn part1(input: &str) -> u16 {
    input_to_graph(input).cheapest()
}
```

## Part II

The next year, just to show off, Santa decides to take the route with the longest distance instead.

He can still start and end at any two (different) locations he wants, and he still must visit each location exactly once.

For example, given the distances above, the longest route would be `982` via (for example) `Dublin -> London -> Belfast`.

What is the distance of the longest route?

## Solution

```rust
impl<'a> Graph<'a> {
    //New Method
    fn costliest(&self) -> u16 {
        Graph::permutations(self.nodes.clone().as_ref())
            .iter()
            .map(|x| {
                let mut last = "";
                x.iter().fold(0, |tot, node| {
                    if last != "" && last != *node {
                        let price = &self.edges[&(last, *node)];
                        last = node;
                        tot + price
                    } else {
                        last = node;
                        tot
                    }
                })
            })
            .max()
            .unwrap()
    }
}
#[aoc(day9, part2)]
pub fn part2(input: &str) -> u16 {
    input_to_graph(input).costliest()
}
```

