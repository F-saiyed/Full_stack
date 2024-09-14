# Creating a set
original_set = {1, 2, 3}

# Aliasing the set
alias_set = original_set

# Modifying the alias set
alias_set.add(4)

# Both sets reflect the change
print("Original Set:", original_set)  # Output: {1, 2, 3, 4}
print("Alias Set:", alias_set)        # Output: {1, 2, 3, 4}
