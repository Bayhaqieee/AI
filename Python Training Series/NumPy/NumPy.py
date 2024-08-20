
# ##### Import the Numpy package under the name np
import numpy as np

# #### Print the numpy version and the configuration
print(np.__version__)
np.show_config()

# #### Create a null vector of size 10
null_vector = np.zeros(10)
print(null_vector)

# #### How to find the memory size of any array
array = np.zeros((100,100))
print("%d bytes" % (array.size * array.itemsize))

# ####  How to get the documentation of the numpy add function from the command line?

# ##### Simply put this command on the terminal
# ###### python -c "import numpy as np; help(np.add)"

# #### Create a null vector of size 10 but the fifth value which is 1

vector = np.zeros(10)
vector[4] = 1
print(vector)

# #### Create a vector with values ranging from 10 to 49
vector = np.arange(10, 50)
print(vector)

# #### Reverse a vector (first element becomes last)
vector = np.arange(1,10)
reversed_vector = vector[::-1]
print(reversed_vector)

# #### Create a 3x3 matrix with values ranging from 0 to 8
matrix = np.arange(9).reshape(3, 3)
print(matrix)

# #### Find indices of non-zero elements from [1,2,0,0,4,0]
array = np.array([1, 2, 0, 0, 4, 0])
non_zero_indices = np.nonzero(array)
print(non_zero_indices)


# #### Create a 3x3 identity matrix
identity_matrix = np.eye(3)
print(identity_matrix)

# #### Create a 3x3x3 array with random values
random_array = np.random.random((3, 3, 3))
print(random_array)

# #### Create a random vector of size 30 and find the mean value
random_vector = np.random.random(30)
mean_value = random_vector.mean()
print(mean_value)


# #### Create a 2D array with 1 on the border and 0 inside
array = np.ones((5, 5))
array[1:-1, 1:-1] = 0
print(array)


# #### How to add a border (filled with 0’s) around an existing array?
array = np.ones((3, 3))
array_with_border = np.pad(array, pad_width=1, mode='constant', constant_values=0)
print(array_with_border)


# #### What is the result of the following expression?
print(0 * np.nan)           
print(np.nan == np.nan)     
print(np.inf > np.nan)      
print(np.nan - np.nan)      
print(np.nan in set([np.nan]))
print(0.3 == 3 * 0.1)       

# #### Create a 5x5 matrix with values 1, 2, 3, 4 just below the diagonal
matrix = np.diag(1 + np.arange(4), k=-1)
print(matrix)


# #### Create an 8x8 matrix and fill it with a checkerboard pattern
checkerboard = np.zeros((8, 8), dtype=int)
checkerboard[1::2, ::2] = 1
checkerboard[::2, 1::2] = 1
print(checkerboard)


# #### Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?
array = np.unravel_index(100, (6, 7, 8))
print(array)

# #### Create a checkerboard 8x8 matrix using the tile function
checkerboard = np.tile(np.array([[0, 1], [1, 0]]), (4, 4))
print(checkerboard)

# #### Normalize a 5x5 random matrix
random_matrix = np.random.random((5, 5))
normalized_matrix = (random_matrix - np.mean(random_matrix)) / np.std(random_matrix)
print(normalized_matrix)

# #### Create a custom dtype that describes a color as four unsigned bytes (RGBA)
color = np.dtype([("r", np.ubyte, 1),
                  ("g", np.ubyte, 1),
                  ("b", np.ubyte, 1),
                  ("a", np.ubyte, 1)])
print(color)

# #### Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)
matrix1 = np.random.random((5, 3))
matrix2 = np.random.random((3, 2))
result = np.dot(matrix1, matrix2)
print(result)

# #### Given a 1D array, negate all elements which are between 3 and 8, in place.
anjay = np.arange(11)
anjay[(3 < anjay) & (anjay <= 8)] *= -1
print(anjay)

# #### What is the output of the following script?
print(sum(range(5), -1))
from numpy import *
print(sum(range(5), -1))

# #### Consider an integer vector Z, which of these expressions are legal?
gggeming = np.arange(5)
print(gggeming**gggeming)
print(2 << gggeming >> 2)
print(gggeming < -gggeming)
print(1j*gggeming)
print(gggeming/1/1)
#print(gggeming < gggeming > gggeming) #this is not legal


# #### What are the results of the following expressions?
print(np.array(0) / np.array(0))
print(np.array(0) // np.array(0))
print(np.array([np.nan]).astype(int).astype(float))

# #### How to round away from zero a float array?
bro = np.random.uniform(-10, +10, 10)
print(np.copysign(np.ceil(np.abs(bro)), bro))

# #### How to find common values between two arrays?
array1 = np.random.randint(0, 10, 10)
array2 = np.random.randint(0, 10, 10)
common_values = np.intersect1d(array1, array2)
print(common_values)

# #### How to ignore all numpy warnings (not recommended)?
import warnings
warnings.filterwarnings('ignore')

# #### Is the following expression true?
print(np.sqrt(-1) == np.emath.sqrt(-1))

# #### How to get the dates of yesterday, today, and tomorrow?
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
today = np.datetime64('today', 'D')
tomorrow = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
print(yesterday, today, tomorrow)
