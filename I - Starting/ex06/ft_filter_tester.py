from ft_filter import ft_filter

nums = [0, 1, 2, 3, 4]


evens = ft_filter(lambda x: x % 2 == 0, nums)
print(list(evens))


truthy = ft_filter(None, nums)
print(list(truthy)) 
original = filter.__doc__
copy = ft_filter.__doc__
print(copy)