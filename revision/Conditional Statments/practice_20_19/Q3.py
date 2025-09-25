'''Generator when you are working with a very large dataset (like reading a huge file or generating millions of numbers) because it processes one item at a time, which is incredibly memory-efficient. You use a normal function that returns a list when the dataset is small and you need to have it all at once.'''
def million():
    for i in range(1000000):
        yield i 
num_generator = million()
for num in num_generator:
    print(num)