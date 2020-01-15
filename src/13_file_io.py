"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""
import sys
# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE

with open('foo.txt', 'r') as f:
    print(f.read())
    f.close()
    print(f.closed)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE

print(type(sys.argv))
a = sys.argv

with open('bar.txt', 'a') as b:
    x = b.write('foobarban\n')
    print(x)
    b.close()
    print(b.closed)