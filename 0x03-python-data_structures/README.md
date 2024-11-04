DATA STRUCTURES
Methods of List objects:
list.append(x) - similar to a[len(a):] = [x]
list.extend(iterable) - extends the list by appending all items from the iterable
list.insert(i, x) - insert at given position(i)
list.remove(x) - remove item of value x
list.pop(x) - remove the first item from a list whose value is equal x
list.clear() - removes all items. equivalent to del a[:]
list.index(x[, start[, end]]) - return zero-based index in the list of the item whose value is equal to x
- The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.
list.count(x) - returns the number of times x appears in the list.
list.sort(*, key=None, reverse=False) - sort items of the list in place
list.reverse() - reverse the items
list.copy() - returns a shallow copy of the list. Similar to a[:]

TUPLES
Though tuples may seem similar to lists, they are often used in different situations and for different purposes. Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking (see later in this section) or indexing (or even by attribute in the case of namedtuples). Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.

A special problem is the construction of tuples containing 0 or 1 items: the syntax has some extra quirks to accommodate these. Empty tuples are constructed by an empty pair of parentheses; a tuple with one item is constructed by following a value with a comma (it is not sufficient to enclose a single value in parentheses). Ugly, but effective.
To unpack a tuple, you asign variables on the left side:
x, y, z = my_tuple
Sequence unpacking requires that there are as many variables on the left side of the equals sign as there are elements in the sequence. Note that multiple assignment is really just a combination of tuple packing and sequence unpacking.

SETS
A set is an unordered collection with no duplicate elements. It is used for membership testing and eliminating duplicate entries.
Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.
the set() func or curly braces (not empty) is used to create sets.
- sets can be support comprehension.

DICTIONARIES
- A set of key:value pairs with keys being unique within a dictionary.
Performing list(d) on a dictionary returns a list of all the keys used in the dictionary, in insertion order (if you want it sorted, just use sorted(d) instead). To check whether a single key is in the dictionary, use the in keyword.
- supports comprehension.
The dict() constructor builds dictionaries directly from sequences of key-value pairs:

Looping.

When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the items() method.
To loop over two or more sequences at the same time, the entries can be paired with the zip() function.
To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the reversed() function.
To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the source unaltered.

Learning objectives:
Why Python programming is awesome
What are lists and how to use them
What are the differences and similarities between strings and lists
What are the most common methods of lists and how to use them
How to use lists as stacks and queues
What are list comprehensions and how to use them
What are tuples and how to use them
When to use tuples versus lists
What is a sequence
What is tuple packing
What is sequence unpacking
What is the del statement and how to use it
