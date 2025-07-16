# The Fibonacci Sequence — My Personal Exploration

## Why Fibonacci?

This repository is my attempt to dig deeper into the Fibonacci sequence—not just as a list of numbers, but as a mathematical idea that keeps showing up in unexpected places. I always found it interesting how something so simple could have so many connections, from nature to algorithms.

## What is the Fibonacci Sequence?

The Fibonacci sequence is a series of numbers where each number is the sum of the two before it. Usually it starts with 0 and 1:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

The formula is pretty simple:  
F(n) = F(n-1) + F(n-2), with F(0) = 0 and F(1) = 1.

## A Bit of History

Fibonacci, whose real name was Leonardo of Pisa, introduced this sequence to Europe in 1202, though it was actually known much earlier in India. That kind of cross-cultural mathematical history is something I find fascinating.

## Mathematical Properties

- **Recursion:** At its core, the sequence is recursive, which makes for interesting coding exercises.
- **Closed Form:** There is Binet’s formula, which surprisingly gives Fibonacci numbers directly using the golden ratio (φ = (1 + √5)/2). 
- **Growth Rate:** The ratio of one Fibonacci number to the previous approaches the golden ratio pretty fast.
- **Divisibility and Patterns:** There are a lot of neat patterns, some of which I’ve tried to explore in code and notes.

## Algorithms I Explored

See `fibonacci_algorithms.py` for several ways to compute Fibonacci numbers:

- Recursive (clean, but slow)
- Iterative (efficient)
- Memoization (with Python’s lru_cache)
- Bottom-up dynamic programming
- Matrix exponentiation (fast, but less intuitive at first)
- Binet’s formula (mathematically elegant, not always reliable for very large n due to floating-point issues)

## Fibonacci in Nature and Beyond

It’s often claimed that Fibonacci numbers show up in nature (sunflowers, pinecones, spiral shells, etc). The more I look, the more I see these patterns, though sometimes I wonder if it’s just us finding order where we want to.

## What’s in this Repo

- `fibonacci_algorithms.py`: Implementations of several algorithms, with notes and some personal commentary.
- `FIBONACCI_REPORT.md`: A deeper dive into the math, derivations, and observations.
- `PERSONAL_NOTES.md`: My ongoing thoughts, questions, and things I’m curious about.

---

This project is mostly for my own learning, but if anyone else finds it useful (or just wants to discuss Fibonacci), that would be great.
