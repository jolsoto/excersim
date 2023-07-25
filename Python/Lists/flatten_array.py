'''
Take a nested list and return a single flattened list with all values except nil/null.
The challenge is to write a function that accepts an arbitrarily-deep nested list-like structure and returns a flattened structure without any nil/null values.

For example:
input: [1,[2,3,null,4],[null],5]
output: [1,2,3,4,5]
'''
def flatten(iterable):
    flattened_list = []
    for item in iterable:
        if item is not None:
            if isinstance(item, list):
                flattened_list.extend(flatten(item))
            else:
                flattened_list.append(item)
    return flattened_list
