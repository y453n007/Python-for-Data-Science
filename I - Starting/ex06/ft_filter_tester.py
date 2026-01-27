from ft_filter import ft_filter

nums = [0, 1, 2, 3, 4]

# Test with a lambda
evens = ft_filter(lambda x: x % 2 == 0, nums)
print(list(evens))  # [0, 2, 4]

# Test with None (removes 0)
truthy = ft_filter(None, nums)
print(list(truthy)) # [1, 2, 3, 4]