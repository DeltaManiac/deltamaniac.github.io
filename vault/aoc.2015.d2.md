---
id: dCrlmw2LQFyXx0gtBSeoY
title: Day 2
desc: ''
updated: 1609050828312
created: 1609048951788
nav_order: 2
---
## I Was Told There Would Be No Math

## Part I

The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length `l`, width `w`, and height `h`) of each present, and only want to order exactly as much as they need.

Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is `2*l*w + 2*w*h + 2*h*l`. The elves also need a little extra paper for each present: the area of the smallest side.

For example:

> A present with dimensions `2x3x4` requires `2*6 + 2*12 + 2*8 = 52` square feet of wrapping paper plus `6` square feet of slack, for a total of `58` square feet.
>
> A present with dimensions `1x1x10` requires `2*1 + 2*10 + 2*10 = 42` square feet of wrapping paper plus `1` square foot of slack, for a total of `43` square feet.

All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?

## Solution

A simple structure that can hold the dimensions would be the starting point from which we can solve the problem.

A method `get_area` that would return the area calculated as `2*l*w + 2*w*h + 2*h*l`.

A method `get_smallest_side_area` would calculate all the side areas and return the minimum which would provide the `slack` to be added.

A `text_to_struct` method that would convert the text input to a `Vector` of `Prism`, to enable easy iteration.

To find the answer iterate over the Vector<Prism> calculate the `area` + `smallest_side_area` and sum them all up.

```rust
// Holds the dimensions of the Gift
#[derive(Copy, Clone)]
pub struct Prism {
    x: u32,
    y: u32,
    z: u32,
}

impl Prism {

    pub fn get_smallest_side_area(self) -> u32 {
        *[self.x * self.y, self.y * self.z, self.z * self.x]
            .iter()
            .min()
            .unwrap_or(&0)
    }

    pub fn get_area(self) -> u32 {
        [
            2 * self.x * self.y,
            2 * self.y * self.z,
            2 * self.z * self.x,
        ]
        .iter()
        .sum::<u32>()
    }
}

#[aoc_generator(day2)]
pub fn text_to_struct(input: &str) -> Vec<Prism> {
    input
        .lines()
        .map(|line| {
            let mut chars = line.trim().split('x');
            Prism {
                x: chars.next().unwrap().parse().unwrap(),
                y: chars.next().unwrap().parse().unwrap(),
                z: chars.next().unwrap().parse().unwrap(),
            }
        })
        .collect::<Vec<Prism>>()
}

#[aoc(day2, part1)]
pub fn part1(input: &[Prism]) -> u32 {
    input
        .iter()
        .map(|x| x.get_smallest_side_area() + x.get_area())
        .collect::<Vec<u32>>()
        .iter()
        .sum()
}
```

## Part II

The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about the length they need to order, which they would again like to be exact.

The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.

For example:

> A present with dimensions `2x3x4` requires `2+2+3+3 = 10` feet of ribbon to wrap the present plus `2*3*4 = 24` feet of ribbon for the bow, for a total of `34` feet.
>
> A present with dimensions `1x1x10` requires `1+1+1+1 = 4` feet of ribbon to wrap the present plus `1*1*10 = 10` feet of ribbon for the bow, for a total of `14` feet.

How many total feet of ribbon should they order?

## Solution

A method `get_smallest_perimeter` that would return the smallest perimeter of the prism.

To find the answer iterate over the Vector<Prism> calculate the `smallest_perimeter` + `sum of the sides of the smallest perimeter` and sum them all up.

```rust
impl Prism {
    pub fn get_smallest_side_area(self) -> u32 {
        *[self.x * self.y, self.y * self.z, self.z * self.x]
            .iter()
            .min()
            .unwrap_or(&0)
    }

    pub fn get_area(self) -> u32 {
        [
            2 * self.x * self.y,
            2 * self.y * self.z,
            2 * self.z * self.x,
        ]
        .iter()
        .sum::<u32>()
    }
    // PART 2
    pub fn get_smallest_perimeter(self) -> u32 {
        *[
            2 * (self.x + self.y),
            2 * (self.y + self.z),
            2 * (self.z + self.x),
        ]
        .iter()
        .min()
        .unwrap_or(&0)
    }
}

#[aoc(day2, part2)]
pub fn part2(input: &[Prism]) -> u32 {
    input
        .iter()
        .map(|x| x.get_smallest_perimeter() + (x.x * x.y * x.z))
        .collect::<Vec<u32>>()
        .iter()
        .sum()
}

```

