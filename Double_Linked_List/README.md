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
- list append
- list insert (append) at a location
- list search
- list item deletion
- list clear (empty)

## File List
**basics.py** - a module containing the class definitions and basic functions   
**double-list.py** - the main (driver) routine to illustrate the singly linked list


## Output

PS C:\Python_Work\Algorithms\Single_Linked_List> python double_list.py  
 
The initial list.  
The list size is:  3   

The nodes data is:  eggs  
The nodes data is:  ham  
The nodes data is:  spam  
 
The list after appending "bacon" as the 2nd item.  
The list size is:  4   

The nodes data is:  eggs  
The nodes data is:  bacon  
The nodes data is:  ham  
The nodes data is:  spam  

Appending to the list start.  
The list after appending "cheese" to the beginning.  
The list size is:  5  

The nodes data is:  cheese  
The nodes data is:  eggs  
The nodes data is:  bacon   
The nodes data is:  ham  
The nodes data is:  spam  

The list has too few nodes for this insertion.  
Tried to append "tomatoes" at location 10.  
The list size is:  5  


Is "cheese" in the list? True  
Is "tomatoes" in the list? False  
After deleting the last node (spam), the list is:  
The nodes data is:  cheese  
The nodes data is:  eggs  
The nodes data is:  bacon  
The nodes data is:  ham  

The current list size is:  4  

After deleting "ham" based on its value, the list is:  
The nodes data is:  cheese  
The nodes data is:  eggs  
The nodes data is:  bacon  

The current list size is:  3  

After clearing the list, its size is:  0  
Is "eggs" in the list? False  