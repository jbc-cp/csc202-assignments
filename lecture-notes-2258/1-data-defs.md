
## Kinds of data / Data Definitions

This is a data structures class! Let's talk about different kinds of
data.

A "Data Definition" is a piece of a program that gives a name to a
kind of data. It can be a new kind of data, in the case of a class
declaration, or a new name for an existing kind of data, in the case
of a Type Alias. There are other kinds of data definitions, we will
discuss them later.

Before talking about any of those, though, let's talk about kinds of
data that don't need data definitions, because they're already defined:

### Built-in data

What kinds of Python data do you know about?

(Write answers on board; numbers, strings, booleans, probably lists, maybe objects.
Ask students for examples of each one that they come up with.)

(Next, ask students for operations that they can apply to each kind of data.
In some cases, of course, certain operations require arguments of multiple
different kinds.)

Is there a difference between infix operators like + and * and functions like
pow(x,y) ?

(discussion)

So: no, not really. Well, syntactically maybe.

### Objects / Classes

Can you define your own kinds of data?

(Discussion)

Sure you can; you can use "Classes" to define new kinds of "Objects".

What's a class?

What's an object?

What's the difference?

Okay, so we define classes, and then we can create objects of those classes.

Let's try it. Suppose I have a Point class, with two fields, x and y.

What does this look like?

(They should be able to define this. They'll probably come up with

```python
class Point:
  def __init__(self, x: float, y: float):
    self.x = x
    self.y = y

  def __repr__(self):
    return "Point({},{})".format(x,y)

  def __eq__(self, other):
    return (type(other) == Point and
            other.x == self.x and
            other.y == self.y)
```

Whew! that's exhausting. How about this, instead:

```
@dataclass
class Point:
  x: float
  y: float
```

That's ... a lot shorter!

It turns out that these two do the same thing. That is, the `@dataclass`
decorator will automatically construct an __init__ and a __repr__ and an
__eq__ method, and actually a bunch more as well.

Quick side question for those of you know Java but not Python: what's different?

(no explicit field declarations.) How do you feel about that? (It's scary.)

### Type Aliases

Another kind of data definition is much simpler; it's just giving a new
name to an existing type, with a "Type Alias".

Here are some examples:

1)

age: TypeAlias = float # an age in years

age_1 : age = 44
age_2 : age = 17

2)

capacity: TypeAlias = int # the number of eggs that fit in a carton

carton_size_1 : capacity = 36
carton_size_2 : capacity = 12

3)

color: TypeAlias = string # a color name

color_1 : color = "LightBrown"
color_2 : color = "Turquoise"

4)

color: TypeAlias = int # a pantone #

color_1 : color = 720
color_2 : color = 640

Type alises are nearly never necessary, but they can make your code
more readable. If you have a function with a ton of integers
flying around, and maybe some of them are ages and some of them
are heights and some of them are ids, it can be useful to give
intermediate variables types named "age" or "height" rather than,
say, just making everything an int.


--

Copyright (C) 2017-2025, John Clements (clements@racket-lang.org)
