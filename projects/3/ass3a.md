# Assignment 3: Huffman Encoding

## Description

For this project, you will implement a program to encode text using
[Huffman coding](https://en.wikipedia.org/wiki/Huffman_coding).
Huffman coding is a method of lossless (the original
can be reconstructed perfectly) data compression. Each character is
assigned a variable length code consisting of ’0’s and ’1’s. The length
of the code is based on how frequently the character occurs; more
frequent characters are assigned shorter codes.

The basic idea is to use a binary tree, where each leaf node represents
a character and frequency count. The Huffman code of a character is then
determined by the unique path from the root of the binary tree to that
leaf node, where each ’left’ accounts for a ’0’ and a ’right’ accounts
for a ’1’ as a bit.  Since the number of bits needed to encode a
character is the path length from the root to the character, a character
occurring frequently should have a shorter path from the root to their
node than an “infrequent” character, i.e. nodes representing frequent
characters are positioned less deep in the tree than nodes for
infrequent characters.

The key problem is therefore to construct such a binary tree based on
the frequency of occurrence of characters. A detailed example of how to
construct such a Huffman tree is provided here: [Huffman_Example.pdf](./Huffman_Example.pdf)

Note: 
* You must provide test cases for all functions.
* Use the given names for specified functions, exactly as they appear
  in the assignment.
* Use descriptive names for data structures and helper functions.

## Source Files

Start with the source files provided to you as part of GitHub Classroom.

## Functions

The following bullet points provide a guide to implement some of the
data structures and individual functions of your program. You should
develop incrementally, building test cases for each function as it is
implemented.

### Count Occurrences: cnt_freq(str)

* Implement a function called cnt_freq(str) that accepts a string
  and returns a numpy array that indicates the number of occurrences
  of each character in the string. Use a
  numpy array data structure of size 256 for counting the
  occurrences of characters.  This will provide efficient access to a
  given position in the list. You can use the Python `ord` function
  to map characters (or, more precisely, strings of length one) to
  numeric values. You should discard all values larger than 255.
  (These numbers will then be ASCII codes.)
  This function should return the 256 item list with the counts
  of occurrences.  There can be issues with extra characters in some
  systems.
  * Suppose the file to be encoded contained:	ddddddddddddddddccccccccbbbbaaff
  * Numbers in positions of freq counts 		[96:104] = [0, 2, 4, 8, 16, 0, 2, 0]
  * For an empty file, this function should return a list of size 256 filled with all 0s.


### Data Definition for Huffman Tree

A Huffman Tree or HTree is a binary tree of HNode's and HLeaf's. 

* An HNode contains an occurrence count for that tree, a character, and a
  left and a right HTree.  An HLeaf contains only a character and an
  occurrence count.

(Note: The character in the HNode isn't really necessary... but having
a character here, and using it in the way specified in the PDF, makes it
easier to grade the submissions, by ensuring that there's only
one way to build the tree.)

### Build a Huffman Tree

Since the code depends on the order of the left and right branches take
in the path from the root to the leaf (character node), it is crucial to
follow a specific convention about how the tree is constructed.  To do
this we need an ordering on the Huffman nodes.

* Start by defining the tree_lt(a, b) function that accepts two HTrees
  and returns true if the occurrence count of the first is
  less the occurrence count of the second OR if the two occurrence
  counts are equal and the character contained at the root of the first
  tree is less than the character contained at the rood of the second
  tree. Note that this refinement (checking the characters) does not
  affect the overall compression associated with huffman coding, but
  it ensures that the ordering is a total ordering (at least for sets
  of trees where each tree's root character occurs at most once, which
  is the case for our tree lists).

* Next, define the HTList data definition, which represents a linked
  list of HTrees. This must include an HTNode (N.B.: don't confuse this
  with HNode, the HTree node class). It must be possible to directly
  construct a list as e.g. `HTNode(a,HTNode(b,HTNode(c,None)))` where
  `a`, `b`, and `c` are HTrees.

* Develop the base_tree_list function, that accepts an array of character
  counts (as returned by cnt_freq) and returns an HTList containing
  256 HTLeaf's, one for each ASCII code. These should be in order from
  0 up to 255, where 0 is the first element of the list and 255 is the
  last.

* Develop the tree_list_insert function, that takes an HTList of HTrees
  that is sorted in the order specified by tree_lt (that is, the occurrence
  count of the first tree is less than or equal to the occurrence count
  of the second tree in the list, and so forth), and another HTree, and
  inserts it in the list at its correct location so that the resulting
  HTList is still sorted. The function must return the new list.

* Develop the initial_tree_sort function, that accepts an unsorted list
  and constructs and returns a sorted list by inserting the nodes from the unsorted
  list one at a time into an initially empty sorted list. Write this
  function by following the data definition on HTLists, and do not
  use an accumulator; this will guarantee that the last node in the
  unsorted list is the first one added to the sorted tree. This does
  not affect the correctness of the algorithm, but honestly just makes
  it easier to grade (sorry).

* Develop the coalesce_once function, that accepts a sorted HTList of
  length 2 or more, and forms a new list by joining the first and
  second node together into a new HNode and inserting that new HNode
  into the list containing the remaining elements. The occurrence
  count of the new node should be the sum of the two original ones,
  and the left and right fields of this node should refer to the
  original trees. At the end, the list should be shorter by one, because
  we're taking two elements off of the list and inserting one.
  This function must return the new list.

* Develop the coalesce_all function, that accepts a sorted HTList
  of length one or more and calls `coalesce_once` repeatedly until
  the list contains only a single HTree, then returns that one HTree.

This single tree is what we call the Huffman Tree. Its occurrence count
should be the number of characters in the original file, and each
subtree should have roughly the same number of characters (or as close
as we can get, given our other constraints). This will mean that common
characters are found along short paths, and that uncommon characters
are found along long paths. This gives rise to our encoding scheme, which
is to represent each character as a path down from the root of this
tree to the leaf containing the given character.

In fact, what we really have now is the *decoding* tree; if we are given
a sequence such as "left left right left right right left", we can start
at the root and follow left and right paths to until we get to a leaf node,
which represents a character in the stream; to continue decoding, we start
at the top again.

Next, we need to map this decoding tree into an *encoding* tree; to
do this, we must identify for each character the path that leads to
that character.

This will consist of a function that follows the template for an HTree,
with *two* accumulators. One is an array of 256 strings, which will wind
up being our map from characters to their encodings. The other is a
string containing ones and zeros, that represents the path taken to get
from the root to this particular node; a zero represents a trip down
the left branch, and a one a trip down the right branch. So, for instance,
if a left left right path leads to the character Q, then in location
81 of the array (ord('Q') == 81), we would put the string "001".

* Develop the build_encoder_array function, that performs this construction.

* Develop the function encode_string_one, that accepts a string and an
  encoder array and constructs the string (containing entirely ones
  and zeros) formed by appending the encodings of each of the characters
  in the string.

* Develop the function bits_to_chars, that accepts a string of ones
  and zeros and converts it to a new string that is 1/8 as long by
  taking each 8-char substring of ones and zeros, converting it to
  the corresponding integer in the range 0-255, and then using the
  `chr` function to produce a single character of the output string.
  The input string's length is unlikely to be divisible by eight; you
  can pad the string with zeros to get it up to the final length.

* Finally, tie it all together with a huffman_code_file function that
  accepts a source and target file path, reads the input file, constructs
  a huffman tree, maps this to an encoding tree, uses the encoding tree to
  encode the contents of the input file, converts it to the char representantion,
  then writes this to the new file (replacing any file that was existing at
  this path).

# OPTIONAL

What? You want to decode the stuff? In order to do that, you'll need to have
the decode tree, or something equivalent to it. You could start from the
original string again to construct the tree, but if you have to have the
original file in order to decompress the compressed file... well, that's
a bit pointless.

However, it turns out that all you need in order to reconstruct the 
decode tree is the list of character frequencies.

If you would like to decode your files, then you should develop a
write_char_freqs function that accepts a frequency array and a file path
and writes the integers in the frequency array to the given file path,
separated by spaces. This should be of quite modest size, even for very
large files. To decode a file, you can then use this small frequency
file to reconstruct the decode table, and then use the decode table
to decode the compressed file.

