# $`\textcolor{blue}{\text{Python Basics - Algorithms}}`$
An illustration of a doubly linked list.  
Richard Ay (April 2026, *updated *)

## $`\textcolor{blue}{\text{Table of Contents}}`$  
* [Reference](#reference)
* [Objective](#objective)
* [Acceptance Criteria](#acceptance-criteria)
* [File List](#file-list)
* [Output](#output)

## Reference
Hands-On Data Structures and Algorithms with Python, Dr. Basant Agarwal, @2022.

## Objective
The objective of the files in this directory is to illustrate the setup and usage (including testing)
of a doubly linked list. 

## Acceptance Criteria
The test file (double_list.py) will perform all operations, based on the classes and functions found
in (basics.py).  The operations performed are:
- list creation
- list count (size)
- list append at start
- list append
- list insert (append) at a location based on data
- list search
- list item deletion based on data
- list item deletion based on location (index)
- list clear (empty)

## File List
**basics.py** - a module containing the class definitions and basic functions   
**double-list.py** - the main (driver) routine to illustrate the doubly linked list

## Output

PS C:\Python_Work\Algorithms\Single_Linked_List> python double_list.py  

The initial list.  
The list size is:  3  

The nodes data is:  eggs  
The nodes data is:  ham  
The nodes data is:  spam  

The list after appending "bacon" at the start of the list.  
The list size is:  4  

The nodes data is:  bacon  
The nodes data is:  eggs  
The nodes data is:  ham  
The nodes data is:  spam  

The list after inserting "ham" at the location of existing "ham".  
The list size is:  5  

The nodes data is:  bacon  
The nodes data is:  eggs  
The nodes data is:  ham  
The nodes data is:  ham  
The nodes data is:  spam  

Is "cheese" in the list? False  
Is "ham" in the list? True  

After deleting "ham" based on its value, the list is:  
The nodes data is:  bacon  
The nodes data is:  eggs  
The nodes data is:  ham  
The nodes data is:  spam  

The current list size is:  4  


After deleting "ham" based on its index (3)  
The nodes data is:  bacon  
The nodes data is:  eggs  
The nodes data is:  spam  

The current list size is:  3  

The list has too few nodes for this deletion.  
After deleting a location past the end of the list.  
The nodes data is:  bacon  
The nodes data is:  eggs  
The nodes data is:  spam  

The current list size is:  3  

After clearing the list, its size is:  0  
Is "eggs" in the list? False  