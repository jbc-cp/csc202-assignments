# Code Analysis

In this assignment, it's time to take what you've learned, and
see how it applies in real-world projects. Specifically, you'll
be working in teams, and taking a look at the source code of an
existing open-source tool, to see how data structures are
used in larger projects.

Specifically, you'll be looking at the source code of a project
that you've already been using, directly or indirectly: the
`coverage.py` coverage tester for python.

## Teams

For this project, you'll be working in teams. Your instructor will
decide how the teams are to be formed.

This project has a time limit; your team should spend no more than
four hours working on it, including the writeup. Furthermore, you
should work together, if at all possible; the goal is for you to
teach & learn from your teammates.

The total writeup for this project is limited to 800 words.

## Procedure

### Before Examining the Code

Before you begin, you should spend a few minutes thinking about what
data structures you'd be likely to need if *you* were implementing
a coverage tester. Write up your results (what data structures you think
you'd need, what they'd be used to represent) in about 150 words.

### Initial Code Examination

Next, download the source code. Take a look at the files in
the project, try to get a feel for what the structure of the
source tree is, what files appear in what directories. Is
there a useful README? Is most of the project source
code? How much of the source code is for testing? Use a tool
like `wc` to count lines and words and get a sense of how
big each part of the project is.


Next, take a look at two randomly chosen files in the `test`
subdirectory, and five randomly chosen files in the `coverage`
subdirectory. For each one, try to figure out what it does. Which
is more valuable: the code, or the comments? 

Write up your findings in about 200 words, including a one- or
two-sentence summary for each source file you look at.

### Detailed Code Examination

Pick a file that you think might be likely to make use of data
structures in an interesting way. You should probably be guided by
your initial speculation about how data structures might be used
in this project. Read through this file carefully, and try to
understand how it works, and how it uses data structures. If the
file that you've chosen turns out not to make interesting use of
data structures, you're welcome to choose another. If the use of
a particular data structure is spread across two files, you can
look at both of them, but try not to get wound up in reading a whole
bunch of files.

If possible, narrow down to a particular data structure. Take a look
at where it's created, where it's used, and where it's mutated (if
applicable). Where do the values of this data structure flow?

Write up your findings in about 300 words.

### Summary

Finally, take some time to reflect on the quality of the code in
the project. Is it readable? Is it clear what every function does?
How are comments used? How would you feel about maintaining or
updating this code? How does this code compare to your own code?
You're welcome to answer other questions than these, and comment
on anything you found particularly noteworthy.

Write up your findings in about 150 words.

### Are you done?

No! You're not done. Now you need to go back and *edit*
what you've written. Did you write too much? That's fine, it just
means that you need to go back and tighten things up, polishing
your text until it shines.

## Writeup Formatting

Format your writeup as a text file. You should use standard Markdown
format, where section titles are formatted using a single leading
hash. See this [example file](./writeup-example.md). Name
the file `writeup.md`.

## Source Code

Here's the link to the
[source code](https://github.com/nedbat/coveragepy/archive/master.zip).

## Submitting your writeup

TBA
