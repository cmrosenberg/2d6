# 2d6
A simple command line utility for finding probabilities for Charges, Casting and Dispelling in Warhammer: Age of Sigmar.

## Usage

`2d6` has a basic interface best demonstrated via examples:

*What is the probability of landing a 9" charge?*
```shell
$ ./2d6 9
27.78% (exact: 5/18)
```
*... with rerolls?*
```shell
$ ./2d6 9 r
47.84% (exact: 155/324)
```

*... and, say, a +3 to charge?*
```shell
$ ./2d6 9 r +3
92.28% (exact: 299/324)
```

*What's the chance of successfully casting a spell with casting value of 8, with rerolls, +2 to cast and assuming the opponent can dispell me?*
```shell
$./2d6 8 r +2 d
81.93% (exact: 6371/7776)
```

If you find `r` and `d` to terse, you can replace them with `reroll` and `dispell` as you see fit.
You can also mix and match ordering and abbrevations. For example,

```shell
$ ./2d6 10 dispell +2 reroll
63.65% (exact: 9899/15552)
```
is equivalent to

```shell
$ ./2d6 10 r +2 d
63.65% (exact: 9899/15552)
```

Negative modifiers are also obviously supported:

*What is the probability of completing a 9" charge with -2 to charge?*
```shell
$ ./2d6 9 -2
8.33% (exact: 1/12)
```

## Installation

All you need is a python 3 runtime. There are no dependencies.
You invoke the command by running `./2d6` or `python3 twodeesix.py`.

There are some unit tests in `tests.py`. Also, a crude monte carlo
simulation to sanity-check the tool is found in `verify_montecarlo.py`.

## TODO

- Add support for modifiers on Dispell attempts.
- Add support for rerolling Dispell attempts.
- Add support for Lord of Change's *Mastery of Magic*
