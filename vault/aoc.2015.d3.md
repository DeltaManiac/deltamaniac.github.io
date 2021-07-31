---
id: 17fb47c1-bbab-4343-bdb4-3e9910c24944
title: Day 3
desc: ''
updated: 1609121387371
created: 1609120611313
---

# Perfectly Spherical Houses in a Vacuum

## Part I

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (`^`), south (`v`), east (`>`), or west (`<`). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

> `>` delivers presents to 2 houses: one at the starting location, and one to the east.
>
> `^>v<` delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
>
> `^v^v^v^v^v` delivers a bunch of presents to some very lucky children at only 2 houses.

## Solution

A simple XY coordinate system would make this a simple pathing problem.

The `last_pos` variable would hold the (x,y) coordinates of Santa.

A hashmap with the key as the (x,y) coordinate will be used to identify individual houses and store the number of presents delivered at that house.

```rust
#[aoc(day3, part1)]
pub fn part1(input: &str) -> usize {
    let mut last_pos = (0, 0);
    let mut map: HashMap<(i32, i32), u32> = HashMap::new();
    map.insert(last_pos, 0);
    input.chars().for_each(|d| {
        last_pos = match d {
            '^' => (last_pos.0 + 1, last_pos.1),
            'v' => (last_pos.0 - 1, last_pos.1),
            '>' => (last_pos.0, last_pos.1 + 1),
            '<' => (last_pos.0, last_pos.1 - 1),
            _ => unreachable!(),
        };
        map.entry(last_pos).and_modify(|x| *x += 1).or_insert(1);
    });
    map.len()
}
```

## Part II
The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

> `^v` delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
>
> `^>v<` now delivers presents to `3` houses, and Santa and Robo-Santa end up back where they started.
>
> `^v^v^v^v^v` now delivers presents to `11` houses, with Santa going one direction and Robo-Santa going the other.

## Solution

Here we would have to trace 2 paths, one for Santa and another for Robo-Santa.

Since both of them take turns reading the instructions, Santa received all odd numbered instructions and the Robo-Santa receives all even numbered instructions.

```rust
#[aoc(day3, part2)]
pub fn part2(input: &str) -> usize {
    let mut last_pos = (0, 0);
    let mut last_pos_clone = (0, 0);
    let mut map: HashMap<(i32, i32), u32> = HashMap::new();
    map.insert(last_pos, 0);
    input.chars().enumerate().for_each(|(i, d)| {
        if i % 2 == 0 {
            last_pos = match d {
                '^' => (last_pos.0 + 1, last_pos.1),
                'v' => (last_pos.0 - 1, last_pos.1),
                '>' => (last_pos.0, last_pos.1 + 1),
                '<' => (last_pos.0, last_pos.1 - 1),
                _ => unreachable!(),
            };
            map.entry(last_pos).and_modify(|x| *x += 1).or_insert(1);
        } else {
            last_pos_clone = match d {
                '^' => (last_pos_clone.0 + 1, last_pos_clone.1),
                'v' => (last_pos_clone.0 - 1, last_pos_clone.1),
                '>' => (last_pos_clone.0, last_pos_clone.1 + 1),
                '<' => (last_pos_clone.0, last_pos_clone.1 - 1),
                _ => unreachable!(),
            };
            map.entry(last_pos_clone)
                .and_modify(|x| *x += 1)
                .or_insert(1);
        }
    });
    map.len()
}
```
