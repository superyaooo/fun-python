class Hypervolume:
    def __call__(self,*lengths):
        i = iter(lengths)   # iter() creates an iterable object
        v = next(i)    # next() returns the next item from the iterator (the 1st in this case).
        # once next() is called, the returned item(v) no longer exists in the iteration
        for item in i:
            v *= item
        return v

    def volume(length,*lengths):
        v = length  # supply 1st number as 1st argument
        for item in lengths:
            v *= item
        return v