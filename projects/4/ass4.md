
# Concordance (An application of hash tables)

This assignment has several parts: implementing a hash table similar to
those described in the text (with some additional functionality) and
writing an application that builds a concordance.  A Webster’s
dictionary definition of concordance is: “an alphabetical list of the
main words in a work.”  In addition to the main words, your program will
keep track of all the line numbers where these main words occur.

### Word and Line Concordance Application  

The goal of this assignment is to process a textual data file to
generate a word concordance with line numbers for each main word.  A
Hash Table ADT is perfect to store the word concordance with the word
being the key and a list of its line numbers being the associated value
for the key. Since the concordance should only keep track of the “main”
words, there will be another file containing words to ignore, namely a
stop-words file (stop_words.txt).  The stop-words file will contain a
list of stop words (e.g., “a”, “the”, etc.) -- these words will not be
included in the concordance even if they do appear in the data file.
You should also not include strings that represent numbers. e.g. “24” or
“2.4” should not appear.

### Sample Text File

```
This is a sample data ((text)) file, to be 
processed by your word-concordance program!!!

A REAL data file is MUCH bigger. Gr8!
```

### Sample Stop-Words File

```
a
about
be
by
can
do
i
in
is
it
of
on
the
this
to
was
```

### Sample Result File

```
bigger: 4
concordance: 2
data: 1 4
file: 1 4
much: 4
processed: 2
program: 2
real: 4
sample: 1
text: 1
word: 2
your: 2
```

Notes: 

1. Words are defined as sequences of characters delimited by any non-letter (whitespace, punctuation).
1. There is no distinction made between upper and lower case letters (`CaT` is the same word as `cat`)
1. Blank lines are counted in line numbering.


The general algorithm for the word-concordance program is:

1. Read the stop-words file into your implementation of a hash table
   containing the stop words. For the initial table size, start with
   default of 128 and let the table grow as described below, if
   necessary. Note: You should use the same hash table implementation
   for the stop-words and the concordance. In the case of the
   stop-words, you just won’t use the line number information (can
   either store the actual line number from the file, or just use a
   default value).
1. The word-concordance will be in a separate hash table from the stop
   words hash table. Process the input file one line at a time to build
   the word-concordance.  This hash table should only contain the
   non-stop words as the keys (use the stop words hash table to "filter
   out" the stop words).  Associated with each key is its value where
   the value consists of a list containing the line numbers where the
   key appears.  Do not include a given line number more than once; there
   should be no duplicates in the list of line numbers.
1. Generate a text file containing the concordance words printed out in
   alphabetical order along with their line numbers.  One word per line
   (followed by a colon), and spaces separating items on each line:
   
   data: 1 4
   
   Note there is no space after the last line number - make sure to match the sample output files.

It is strongly suggested that the logic for reading words and assigning
line numbers to them be developed and tested separately from other
aspects of the program.  This could be accomplished by reading a sample
file and printing out the words recognized with their corresponding line
numbers without any other word processing.

### Collision resolution:

Your implementation should use separate chaining. Each hash cell contains a linked
list of key-value pairs.

Note that you do not have to support deletion of items from your hash table.

The hash function should take a string containing one or more characters
and return an integer.  Here is the hash function you should use:

h(str) = ∑_(i=0)^(n-1)〖ord(str[i])* 〖31〗^(n-1-i) 〗  where n = len(str)

In order to keep the number of multiplications down, you should use Horner's rule to
compute the output of this hash function for each key. This means
alternating additions and multiplications, rather than raising 31 to
many different powers.

As usual, mapping the large integers that result from this to bin numbers will
require a modulo operation.

Also, your hash table size should have the capability to grow if the
input file is large.  After insertion of an item, if the number of entries
is greater than or equal to the hash table size, you should grow the hash table size.

Start with a default hash table size of 128. When increases are necessary, double
the size of the table and be sure to re-hash all items in the table.
(Words that collide in a table of size 128 may not collide in a table of
size 256.)

### Removing Punctuation

It is recommended that you process the input file one line at a time.

For each line in the input file, do the following:

* Remove all occurrences of the apostrophe character (‘) (so the word "don't" would simply become "dont")
* Convert all characters in string.punctuation to spaces.
* make all characters lower-case, using the `lower()` function
* Split the string into tokens using the .split() method.
* Each token that returns True when the isalpha() method is called should be considered a “word”.  All other tokens should be ignored.

### Using Python data structures

Please do not use a Python `dict` for this assignment. It's a hash table,
so that's pretty much the whole assignment done right there.

You will be using a Python `List` in several  places; to represent the Hash Table
itself, and also as the return type of several functions defined below.

### Data Definitions

For this assignment, you will need a bunch of small data definitions, including
the following:

```
IntList # a linked list of integers, used to store lists of line numbers

WordLines # including a word, and a mutable field containing IntList of the lines on which it appears

WordLinesList # a linked list of WordLines structures

HashTable # an array (Python's `List`) of `WordLinesList`s, and a count of
 the number of `WordLines`es stored in the hash table.
```

The HashTable should be mutable. The second field of the `WordLines` should be mutable.
The other structures and fields should not be mutable.



### Testable Functions

In order to make your code testable, we're requiring the following set of functions. 


```
# Make a fresh hash table with the given size, containing no elements
def make_hash(size: int) -> HashTable:
  pass

# Return the size of the given hash table
def hash_size(ht: HashTable) -> int:
  pass

# Return the number of elements in the given hash table
def hash_count(ht: HashTable) -> int:
  pass

# Does the hash table contain a mapping for the given word?
def has_key(ht: HashTable, word: str) -> bool:
  pass

# What line numbers is the given key mapped to in the given hash table?
# this list should not contain duplicates, but need not be sorted.
def lookup(ht: HashTable, word: str) -> List[int]:
  pass

# Add a mapping from the given word to the given line number in
# the given hash table
def add(ht: HashTable, word: str, line: int) -> None:
  pass

# What are the words that have mappings in this hash table?
# this list should not contain duplicates, but need not be sorted.
def hash_keys(ht: HashTable) -> List[str]:
  pass

# given a list of stop words and a list of strings representing a text,
# return a hash table
def make_concordance(stop_words: List[str], text: List[str]) -> HashTable:
  pass

# given an input file and an output file, overwrite the output file with
# a sorted concordance of the input file
def full_concordance(in_file: str, out_file: str) -> None:
  pass
```

Note that nearly all of these methods should not require traversing the
whole hash table. The exceptions are: `hash_keys`, `make_concordance`,
`full_concordance`, and (occassionally) `add` (when a resize is required).

All of these should be defined in the file `main.py`, in such a way that
one can write 

```
from main import make_hash, hash_size, hash_count, has_key, lookup, add, hash_keys, make_concordance
```


### Implementation Report

Your project must include a short implementation writeup or
"lab report", containing the following information:

* instructions on how to call your program with a text of the user's choice.
* the data definitions, and first lines & purpose statements of every
  function & method that you wrote.
* A description of running the program on a large text file (> 1 Megabyte),
  including the total length of the output, and a quasi-random chunk of
  five consecutive lines of the textual output. Choose one of these lines, and verify
  by hand that the given word does in fact occur in the specified locations
  within the file.
* the name of an animal that does not occur anywhere in your input text.

This writeup should be in the form of a pdf with the name "writeup.pdf",
submitted as part of your Git repo.

### How To Hand In

Hand in your code by pushing to the git repo corresponding to this project.

You should turn in all source code, testing files, including at least
one that is more that 1 megabyte in size, and the writeup. If you test
on a file that is not in English, you will want to provide a
stop_words.txt file specifically for that language, which may be
difficult unless you are a native speaker of that language.


