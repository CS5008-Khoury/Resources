# Technical Interview Questions

A collection of technical interview questions to be explored each module. 
- [Technical Interview Questions](#technical-interview-questions)
  - [Github and Linux](#github-and-linux)
    - [Github](#github)
    - [Linux](#linux)
  - [C and the Stack](#c-and-the-stack)
  - [C, The Heap, and Executables](#c-the-heap-and-executables)
  - [Introduction to Analysis of Algorithms, Quadratic Sorts](#introduction-to-analysis-of-algorithms-quadratic-sorts)
    - [Analysis of Algorithms](#analysis-of-algorithms)
    - [Quadratic Sorts](#quadratic-sorts)
  - [Sort Analysis, Recursion, Efficient Sorting (MergeSort, QuickSort)](#sort-analysis-recursion-efficient-sorting-mergesort-quicksort)
    - [Recursion](#recursion)
    - [Efficient Sorting](#efficient-sorting)
  - [Dynamic Programming](#dynamic-programming)
  - [Stacks, Queues, and Linked Lists](#stacks-queues-and-linked-lists)
    - [Stacks](#stacks)
    - [Queues](#queues)
    - [Linked Lists](#linked-lists)
  - [Trees and Heaps](#trees-and-heaps)
    - [Trees](#trees)
    - [Heaps](#heaps)
  - [Graphs](#graphs)
  - [Greedy Algorithms](#greedy-algorithms)
  - [Hash Tables](#hash-tables)
  - [Primer on Proofs](#primer-on-proofs)
  - [Complex Data Structures/Further Thinking - Additional Questions](#complex-data-structuresfurther-thinking---additional-questions)


## Github and Linux

### Github

* Explain the difference between Git and GitHub. Further, explain the concept of version control and how it can help with collaboration in software development.

* What is the difference between __git add__ and __git commit__?

* How do you clone a github repository? How do you pull and push to a repository?

* You and your partner pull the same file from Github to make changes. You both change the same section of code. Your partner pushes their changes first, then you try to push. What is the result and how do you resolve this?

### Linux

* What exactly is a terminal and why is it important?

* What does the command __ls__ stand for and what does it do? Sometimes files are hidden, how do you use __ls__ to view them?

* What does the command __rm__ do? Using __rm__ on a directory may cause an error if the directory contains files. How do we delete a directory and all of its contents?

* What are the three types of file permissions in Linux and how do you change them using __chmod__?

## C and the Stack
<!-- add more here -->

* What is the difference between a compiled and an interpreted language? Which one is better? Give an example of each.

* What is the difference between a static and a dynamic programming language? What are the pros and cons of each?

* What is a pointer? What is the relationship between pointers and arrays in C?

## C, The Heap, and Executables

<!-- add more -->
* What is the difference between stack and heap memory allocation and when would you use each?
  
* What is a header (.h) file and how does it differ from a source file? Why do we use header files?

* Explain the process of pre-compiling.

* Explain what __#define__ does and how it differs from the use of constants.

* Explain the process of opening, reading, writing, and closing a file in C. What do we need to watch out for?

* What is the fetch-decode-execute cycle, and how does it relate to program execution?

* What is a memory leak and how do you identify it and prevent it?

## Introduction to Analysis of Algorithms, Quadratic Sorts

### Analysis of Algorithms

* What is Big O? How does it help us analyze algorithms?

* When would we want an algorithm with a higher time complexity than another faster algorithm?

### Quadratic Sorts

* Explain the time and space complexity of Bubble, Selection, and Insertion sort.

* Provided with a list of integers sorted in descending order. Which sort would perform the best to sort the list in ascending order?

* Given an array __[1, 5, 4, 6]__ explain how each of the Quadratic Sorts will sort this list.

* Quadratic sorts are extremely slow and not scalable. So why do we learn about them andwhen would we ever use one?

* You are provided with a large data set of student grades for CS 5008. You want to sort the grades in ascending order. Which Quadratic Sort would you choose and why? 
    * Follow up, now that you've sorted the grades, you need to sort alphabetically while preserving the relative order of the sorted grades. Which sort would you use and why?

##  Sort Analysis, Recursion, Efficient Sorting (MergeSort, QuickSort) 

### Recursion

* What is recursion? How does a recursive algorithm exit?

* Describe a scenario when you would want to use recursion and a scenario where you wouldn't.

### Efficient Sorting

* Explain how Merge Sort works and what is its time and space complexity?

## Dynamic Programming

* What is Dynamic Programming and when would we want to use it? When wouldn't we?

* Dynamic Programming solves a common recursive issue of repeated calculations. So, when would we want to use recursion instead of Dynamic Programming?

## Stacks, Queues, and Linked Lists

### Stacks

* Explain LIFO and provide examples of real world applications of LIFO.

* Your're in charge of implementing a web browser's "back" button functionality. How would you implement it and what operations would you need to supply.

### Queues

* Explain FIFO and provide examples of real world applications of FIFO.

* Queues can be implemented using an array or a linked list. What are the trade-offs of each implementation?

* Explain what a priority queue is. How does it differ from a regular queue, and what are its use cases?

### Linked Lists

* Discuss the differences of an array and a linked list. When would you want to use one over the other?

* Discuss how operations such as inserting and deleting nodes works and what are their time complexities?

* A linked list can be singly or doubly linked. What are the tradeoffs of each and when would you use one over the other?

* You've been tasked with implementing a playlist for music app. How would you implement it and what operations would you need to supply?

* Explain how to reverse a linked list without using any additional data structures (in place).

## Trees and Heaps

### Trees

* Discuss what a binary tree is. What is a full and what is a complete binary tree?

* How does a binary tree differ from a binary search tree?

* Discuss the operations used on a binary search tree such as inserting and deleting nodes as well as their runtimes.

### Heaps

* What is a heap and its various types?

* Discuss the operations used on a heap such as inserting and deleting nodes as well as their runtimes.

* How does a heap differ from an array or a linked list? When would you prefer to use a heap?

## Graphs

* What is a graph and its various components? What is a directed vs. undirected graph? Provide some real world uses for each.

* What are some types of graph representation? When would you prefer to use one over the other?

* Explain the difference between BFS and DFS. What are some applications of each?

##  Greedy Algorithms 

* Explain the concept of a greedy algorithm. When would you want to apply one?

* What are some scenarios when you wouldn't want to apply a greedy algorithm?

## Hash Tables

* Explain what a hash table is. What is the process of hashing?

* Discuss the time complexities of the various operations on a hash table.

* When would you prefer to use a hash table of an array or a linked list? When would you not?

* You are provided with a hash table of unique student IDs. The table is full but we have some new students. How do we add them to the hash table?

* Explain what a collision is and what are some techniques for handling collisions?

## Primer on Proofs

* What is the difference between a direct proof, an indirect proof, and proof by induction? When would you use each proof over another?

## Complex Data Structures/Further Thinking - Additional Questions

* Example, asking about a what multiple data structures would be best to recreate a python dictionary