# Homework #3
## Part one for threads

Write a junk folder processing program that sorts the files in the specified folder by extension using multiple threads. Speed up the processing of large directories with many subfolders and files by doing a parallel traversal of all folders in separate threads. The most time-consuming process is file transfer and getting the list of files in the folder (iterating over the directory contents). To speed up file transfer, it can be done in a separate thread or a pool of threads. This is more convenient because you don't have to process the result of this operation in your application and you don't need to collect any results. To speed up traversal of directory contents with multiple nesting levels, you can perform processing of each subdirectory in a separate thread or pass the processing to a pool of threads.

## The second part is for processes
Write an implementation of the factorize function that takes a list of numbers and returns a list of numbers by which the numbers in the input list are divided without a remainder.

Implement a synchronous version and measure the execution time.

Then improve the performance of your function by implementing the use of multiple processor cores for parallel computation, and measure the execution time again. Use cpu_count() from the multiprocessing package to determine how many cores there are on the machine.

You can use the test to verify that the function itself works correctly:
```
def factorize(*number):
    # YOUR CODE HERE
    raise NotImplementedError() # Remove after implementation


a, b, c, d  = factorize(128, 255, 99999, 10651060)

assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
```