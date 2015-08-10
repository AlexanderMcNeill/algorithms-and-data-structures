__author__ = 'mcnear1'


import ctypes  # provides low-level arrays


class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""

    def __init__(self):
        """Create an empty array."""
        self._n = 0  # count actual elements
        self._capacity = 1  # default array capacity
        self._A = self._make_array(self._capacity)  # low-level array

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n

    def __getitem__(self, k):
        """Return element at index k."""
        if not 0 <= k < self._n:
            raise IndexError("invalid index")
        return self._A[k]  # retrieve from array

    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity:  # not enough room
            self._resize(2 * self._capacity)  # so double capacity
        self._A[self._n] = obj
        self._n += 1

    def pop(self):
        """Pop the last item off the array and return it"""
        last_item = self._A[self._n]  # getting a reference of the item I'm popping off

        self._A = None  # Removing the reference from the array
        self._n -= 1  # Updating the number of elements in the array

        if self._n <= self._capacity / 4:  # Checking if the items in the array is a quarter of its capacity
            self._resize(self._capacity/2)

        return last_item

    def _resize(self, c):  # nonpublic utility
        """Resize internal array to capacity c."""
        B = self._make_array(c)  # new (bigger) array
        for k in range(self._n):  # for each existing value
            B[k] = self._A[k]
            self._A = B  # use the bigger array
            self._capacity = c

    def _make_array(self, c):  # nonpublic utility
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()  # see ctypes documentation


class SortedArray(DynamicArray):
    """Array class that maintains an ordered list"""

    def __init__(self):
        DynamicArray.__init__(self)

    def append(self, obj):
        """Overriding the append method to keep the array contents sorted"""
        pass

    def sorted_index(self, value):
        """returns the index where the value would fit in"""

