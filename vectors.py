import math

test_vector1 = [56,12,35]
test_vector2 = [2,8,3]

def vector_add(v,w):
    # adds matching elements from two vectors
    # returns vector containing sums
    return [v_i + w_i for v_i,w_i in zip(v,w)]

def vector_sub(v,w):
    # Substracts 2nd vector elements from 1st one
    # returns vector containing substractions
    return [v_i - w_i for v_i,w_i in zip(v,w)]

def vector_sum(vectors):
    # Sum of all vectors in -vectors- parameter
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result,vector)
    return result

def scalar_multiply(scalar,vector):
    # Really need an explanation ??
    return [scalar*cur_val for cur_val in vector]

def vector_mean(vectors):
    # Calculate a vector mean
    cnt_vectors = len(vectors)
    result = scalar_multiply(1/cnt_vectors,vector_sum(vectors))
    return result

def dot(v,w):
    return sum(v_i * w_i for v_i,w_i in zip(v,w))

def sum_of_squares(v):
    # """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v,v)

def magnitude(v):
    return math.sqrt(sum_of_squares(v));

def squared_distance(v, w):
    # """(v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
    return sum_of_squares(vector_sub(v, w))

def distance(v, w):
    return magnitude(vector_sub(v, w))

# print("Vector Add : " + str(vector_add(test_vector1,test_vector2)))
print("Vector Sum : " + str(vector_sum([test_vector1,test_vector2])))
# print("Scalar Multiply : " + str(scalar_multiply(0.5,test_vector2)))
print("Mean : " + str(vector_mean([test_vector1,test_vector2])))
print("Squarred Distance : " + str(squared_distance(test_vector1,test_vector2)))
print("Distance through magnitude : " + str(distance(test_vector1,test_vector2)))
