# Design Recipe, Testing

## Learning Outcomes

* knowing that the design recipe consists of a set of steps, and
  knowing the first 3 steps (Data defs, purpose stmt and header, tests)
* being able to construct data definitions for simple data
* being able to construct data definitions for compound data (objects)
* writing simple functions on compound data


Okay, this is the lecture where we talk about being responsible
citizens. Specifically, I'm going to try to present to you a *process*
for developing software.

Here's the process: go crazy and do whatever you like!

No? That's not a process? Ah well, I guess we have to pick a real process.

## The Design Recipe

Here's the goal: get the program written *efficiently* so you have the
time you need to sleep, eat, play, and do all your other homework.

Sound good?

As usual, getting things done efficiently means being careful and
working methodically. It means planning ahead, and thinking before
you type.

There are six steps in our design recipe (which, by the way, is
taken one hundred percent from the excellent book ``How To Design
Programs'', which is a totally amazing book---disclaimer: I know
the book's authors extremely well).

### Step One: Data Definitions (30 minutes)

Choosing how to represent your data is the single most important
decision you'll make when you begin to design a program.

This is a class about data structures, so it shouldn't be surprising
here, but in fact this applies to all of the work that you do.

Nearly everything else that you do stems from the decisions that you
make here.

Often, these decisions are made for you; for most of this class, I'll
be telling you what data structures to use for each of the labs. In
later assignments, you may be making these decisions yourself.

The basic question that you're trying to answer is this: "What values
in my programming language will I use to represent the elements of
my problem?"

#### Simple Data

Some decisions are (relatively) easy: if you're trying to represent
the height of a person, you probably want to use a floating-point
number. If you're trying to represent a pet's name, you probably
want to use a string.

Tell me about some *basic* kinds of python values:

(strings, ints, floats, booleans; try to fend off lists and
objects. Have them supply examples, too.)

These simple decisions give rise to simple data definitions. A data
definition is a piece of code that starts with a comment of the form
`A <whatever> is...`. So, for instance, if you decide that a pet
name should be represented as a string, you might write

```
PetName: TypeAlias = str
```

or

```
Income: TypeAlias = int # dollars/year of family income
```

Note that in these two cases, we're just giving more meaningful names
to existing data definitions. You should write this kind of data
definition only when it makes your code clearer and more readable.
There's absolutely no reason that you have to have a data definition for
every problem you solve. If your program just takes a number, that's fine,
and there's no need for a data definition specific to that program.

#### Compound Data

Other times, you may want to represent values that contain other values,
using objects. So, for instance, if you're operating on census data, you
migeht want to represent a household as an object with a location, a list
of people, and an income.

In Python, we can describe a set of objects using a `class`, as
you already know:

```python
@dataclass(frozen=True)
class Household:
  location: Loc
  people: int
  income: Income
```

Note that using the @dataclass decorator here means that we don't
have to write the __eq__ and __repr__ and __init__ methods.


Note that in the case of the location, we're referring to other data
definitions that are presumably defined separately.

For the sake of class, let's assume that these are both very simple:

```python
Location: TypeAlias = str # city name
```


#### Mixed Data

Sometimes, you want data that can be one of two different things.
This is going to be very important in our discussions of later data
structures, but for now, we're going to skip over it.

### Step Two: Purpose Statement, Contract, Header (15 minutes)

Okay, let's imagine we're writing a program, now. It's going to do
something simple. Let's suppose that we're trying to classify households
according to whether they're low, medium, or high-income households.
These divisions might come from statistics that we gather about the
distribution of incomes in the area, but let's assume that this part of
the program is just going to accept the divisions as inputs, and compute
which category a given household belongs to.

What kind of data will this program require? Well, it will take households
as inputs, and also numbers, and it might return a string. We'll use
the data definition for Households that we came up with earlier. Okay,
that was step 1, data definition. Now we're ready for step 2:


First, we need a purpose statement. This is a one-line comment
that states what the function will do:

```python
# return the income category for a given household
```

Writing purpose statements is incredibly important. There are two reasons
for this.

First, and more obvious: purpose statements help your graders and your
co-workers understand what a function is supposed to do. You would be
absolutely amazed at how hard it is to understand what a function called
"helper_thingy" is supposed to do.

Second, and less obvious: if you can't write the purpose statement, you
shouldn't be writing the function. Often you'll start writing a
function, saying to yourself, "I need a function here that does something
mumble mumble here lemme just start writing it." If you can't say ahead
of time what the function is supposed to do, then you shoudn't be writing
it. For Heaven's sake don't make Purpose statements an afterthought.

There is one obvious exception to this: if you are engaged in a creative
endeavor--writing a piece of music, playing with art--none of the rules
apply. You're just exploring and tinkering. It's fine to have "exploring
and tinkering" mode. However, you will find that "exploring and tinkering
mode" is *not* an effective way to get programs written in this class, or
any time when you know exactly what it is tht you need to get done.


Finally, we need to write the first line of the function, and a dummy
for the body:

```python
def income_level(household: Household, low_mid: int, mid_high: int) -> str:
    pass
```

What decisions are we making here? (discuss) Yep: the name of the function,
the names of the arguments, the types of the arguments. Okay, so here's the whole program so far:

```python
from typing import *
from dataclasses import dataclass

@dataclass(frozen=True)
class Household:
  location: Loc
  people: int
  income: Income

# return the income category for a given household
def income_level(household: Household, low_mid: int, mid_high: int) -> str:
    pass
```


--

Copyright (C) 2017-2025, John Clements (clements@racket-lang.org)
