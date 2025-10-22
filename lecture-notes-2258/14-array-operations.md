# Arrays

Prefatory remark: Python mashes together "arrays" and "lists". We're going to
pull out only the "array" pieces, and talk about them as "arrays". In all of the
Python documentation, you'll see them called "lists".

## Array Operations

So, back to arrays. What operations do we have on them?

Many operations we're familiar with already:

get : a[4]
set : a[4] = 34

Both of these are constant-time.

The new one is creation. We're going to see a few different
ways to create arrays.

1) bracket-with-commas:

Here's the one you already know about:

[4,6,787]

It creates lists of a length that is fixed by the code.

2) multiplication:

34*[None]
22*["abc"]

these create arrays of the given size, entirely filled with the given value.

3) list comprehension:

Here's another one, called a "list comprehension", which is really nice, when it's applicable:

[ i*2 for i in range(20) ]

This creates the array

[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

To explain this just a bit more; a list comprehension contains three pieces
inside the brackets: a value expression, a name, and a "value producer", also
known as an "iterator". (We did not discuss iterators any further). The resulting
array has the same length as the number of elements produced by the iterator, and
each element of the array is the result of evaluating the value expression with
the given name set to the corresponding element of the iterator.

These are the three ways we're going to create arrays in this course.

The first kind of array creation is of constant time. That's because the length
of the list is fixed by the program code.

The second and third, though, are not; each of them is O(n) in the
length of the list.

## Array Types

Python has a type for lists, it's called List. It takes a type parameter,
in the same way that Union does, to specify what type is in the list. So, for instance,

List[int]

... is a list of ints.

List[List[str]]

... is a list of lists of strings.

## Functions on Arrays

Let's talk about functions on arrays. Specifically, let's see if we can
implement Python's "append()" method. We'll implement it as a function,
because .. well, it's a bit easier.

Following the design recipe: Step one is done, we don't need to design new data.
Here's step two:

# append an element to the end of a list
def my_append(val : Any, l : List[Any]) -> List[Any]:

Step three, some tests:

s.aE(my_append(3,[],[3])
s.aE(my_append(3,[7,8,9]),[7,8,9,3])

step four... the template for arrays (and also, recopying step 2, so it reads better):

# append an element to the end of a list
def my_append(val : Any, l : List[Any]) -> List[Any]:
  acc = ...
  for i in range(len(l)):
    ...
    acc = ...
  ...
  return ...

There are actually a *lot* of different ways to write functions on arrays, this
is by no means the only one. In fact, you can often get by with just a list
comprehension, and be done! However, the template given here is probably the most
"standard" one, and it does work for the majority of the functions on arrays.

Step five: fill it in.


# append an element to the end of a list
def my_append(val : Any, l : List[Any]) -> List[Any]:
  acc = len(l) * [None]
  for i in range(len(l)):
    acc[i] = l[i]
  acc[len(l)] = val
  return acc

What's the running time of this?

Well, our existing methods don't work that well; loops are
another not-constant-time operation. In order to understand
the running time of code with loops, we need to treat each loop
in our count as though it were another function call.

So, calling the my_append method on a list of length l gives us
a count of

1 + n (the first 'n' is for the array initialization) + n * 1 (each loop body is constant time)

so that's 1 + 2n ... which is O(n). So my_append is O(n).

But ... that's kind of not that great. If I were to write code like this:

def my_array_range(n : int):
  acc = []
  for i in range(100):
    acc.append(i)
  return acc

It would turn out to be

1 + n * ( O(n) ) ... which is O(n^2). Wow, that's pretty bad!

It turns out that there's a trick that makes this better. But we won't talk about it today!





