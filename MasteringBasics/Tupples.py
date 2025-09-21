'''# A set of fixed coordinates that should not change
pune_coords = (18.5204, 73.8567)
print(f"Latitude is: {pune_coords[0]}")

# This would cause an error:
pune_coords[0] = 19.0  # TypeError: 'tuple' object does not support item assignment

'''

# A set of unique tags for a blog post
tags = set(['python', 'coding', 'tech', 'python'])
tags.add('programming') # Add a new tag
print(tags) # Notice 'python' only appears once