# Define the dot_prod function to calculate dot product between two vectors
def dot_prod(vector1, vector2):
    # Check if the lengths of the vectors are the same
    if len(vector1) != len(vector2):
        print("Error: Vectors must have the same length for dot product calculation.")
        return None
    
    # Calculate the dot product
    result = sum(x * y for x, y in zip(vector1, vector2))
    return result

# Test the dot_prod function with example vectors
vector_a = [1, 2, 3]
vector_b = [4, 5, 6]

# Calculate the dot product of the example vectors
dot_product = dot_prod(vector_a, vector_b)

# Print the result
if dot_product is not None:
    print("Dot product of vectors:", dot_product)
