Spring 2020 Lab 6

**Lab 6: Basic Comparison Sorts**

A comparison sort is a type of sorting algorithm that compares elements in a list (array, file, etc) using a comparison operation that determines which of two elements should occur first in the final sorted list. The operator is almost always a **total order** :

1. a ≤ a for all a in the set

2. if a ≤ b and b ≤ c then a ≤ c (transitivity)

3. if a ≤ b and b ≤ a then a=b

4. for all a and b, either a ≤ b or b ≤ a // any two items can be compared (makes it a total order)

In situations where three does not strictly hold then, it is possible that a and b are in some way different and both a ≤ b and b ≤ a; in this case either may come first in the sorted list. In a **stable sort** , the input order determines the sorted order in this case.

A metaphor for thinking about comparison sorts in the abstract is that someone has a set of unlabeled weights and a balance scale. Their goal is to line up the weights in order by their weight without any information except that obtained by placing two weights on the scale and seeing which one is heavier (or if they weigh the same).

The following link is helpful.

Comparison Sorting Visualizations: https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html

Your goal for this lab is to implement simple versions of Insertion Sort - **insertion\_sort(alist)**, Selection Sort - **selection\_sort(alist),** that will sort an array of integers and **count the number of comparisons**. Include your test cases as lists in the same file as your functions. Each function takes as input a list of integers, sorts the list counting the comparisons at the same time, **and returns the number of comparisons**. After the function completes, the " **alist**" should be sorted.

Submit three files – **insertion\_sort.py** , **selection\_sort.py and the pdf described below** to Canvas.

The worst-case runtime complexity is O(n^2) for selection and insertion sort. Why? Write out the summation that represents the number of comparisons. You should write test cases that illustrate that the number of comparisons is O(n^2) and **include those testcases in your submissions to PolyLearn**. Note you will need to run test cases of different sizes to show that Insertion and Selection sort are O(n^2). To do this, plot the number of comparisons (y-axis) vs. the size of the list (x-axis). Since the plot is shaped like a parabola for selection and insertion sort this indicates that it is quadratic. In a separate file submitted as pdf, for each Insertion and Selection sort submit a table showing list size and number of comparisons from your test cases and a plot of that data.

**Also include a comment with your test cases explaining why the testcases for the worst case are the worst case!**

Note: There is a fundamental limit on how fast (on average) a comparison sort can be, namely
O(n\*log n). We will discuss the reasons for this in class.
