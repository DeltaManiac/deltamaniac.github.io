
# Intro
Dynamic programming is a powerful tool because it can break a complex problem into manageable subproblems, avoid unnecessary recalculation of overlapping subproblems, and use the results of those subproblems to solve the initial complex problem.

Most common features of a dp problem

- The problem can be broken down into "overlapping subproblems" - smaller versions of the original problem that are re-used multiple times

- The problem has an "optimal substructure" - an optimal solution can be formed from optimal solutions to the overlapping subproblems of the original problem


# Two Ways for DP

## Memoization

> **memoizing** a result means to store the result of a function call, usually in a hashmap or an array, so that when the same function call is made again, we can simply return the memoized result instead of recalculating the result.

- Top Down approach
- Implemented via recursion and optimized via memoization


## Tabulation

- Bottom Up Approach
- Implemented via iteration

# Identifying DP

The **first characteristic** that is common in DP problems is that the problem will ask for the optimum value (maximum or minimum) of something, or the number of ways there are to do something.

For example:

> What is the minimum cost of doing...
> What is the maximum profit from...
> How many ways are there to do...
> What is the longest possible...
> Is it possible to reach a certain point...


The **second characteristic** that is common in DP problems is that future "decisions" depend on earlier decisions. Deciding to do something at one step may affect the ability to do something in a later step.
This characteristic is what makes a greedy algorithm invalid for a DP problem - we need to factor in results from previous decisions.


# The Framework

1. A function or data structure that will compute/contain the answer to the problem for every given state.
2. A recurrence relation to transition between states.
3. Base cases, so that our recurrence relation doesn't go on infinitely.