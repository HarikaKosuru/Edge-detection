from helper_functions import *

#-----------------------FILL IN THE FOLDER WHERE YOUR IMAGE EXISTS--------------------------
datafolder = "C:/Users/spj/workspace-python/teaching-material/assgn1code/images/"
imgpath = datafolder + "1.jpg" 
#----------------------------------------STARTER CODE----------------------------------------
# Convert the color image to grayscale and returns the grayscale pixels 
pixel_values = read_colorimg(imgpath)
# The returned pixel values INCLUDE 2 boundary rows and 2 boundary colns. Therefore,
numb_rows = len(pixel_values) - 2
numb_colns = len(pixel_values[0]) - 2
#
#----------------------------------------WRITE YOUR CODE HERE----------------------------------------
# Create a data structure to store updated pixel information
#Initializing all tne values of new pixels to zero
n_r=numb_rows
n_c=numb_colns

new_pixel_values = [[0 for i in range(n_c)]for j in range(n_r)]
# Define the 3 x 3 mask as a tuple of tuples
mask = [[-1,0,1], [-2,0,2], [-1,0,1]]

# Implement a function to slice a part from the image as a 2D list
def get_slice_2d_list(p,r,c):
    """This function takes pixel values, row and columns as input,
       and returns output as 3x3 patch of surrounding pixels as a list of lists"""
    slice_list=[m[c-1:c+2] for m in p[r-1:r+2]]
    return slice_list

# Implement a function to flatten a 2D list or a 2D tuple
def flatten(np):
    """This function converts a 2D list into 1D list""" 
    flatten_list=[j for i in np for j in i]
    return flatten_list
a=len(pixel_values)
b=len(pixel_values[0])
for row in range(1,a-1):
    for col in range(1,b-1):
    

# For each of the pixel values, excluding the boundary values
    # Create little local 3x3 box using list slicing
        neighbour_pixels = get_slice_2d_list(pixel_values,row,col)
    # calling the function  for flattenning the neighbour_pixels and mask values
        flatten_msk=flatten(mask)
        flatten_np=flatten(neighbour_pixels)    
    # Apply the mask
        mult_result =  list(map(lambda x,y: x*y , flatten_np, flatten_msk))      
    # Sum all the multiplied values and set the new pixel value
        np_sum=0
        m=len(mult_result)
        w=0
        while w!=m:
            w=w+1
            np_sum=np_sum+mult_result[w+1]
        #initialising the new pixel values by appraximate indexing 
        new_pixel_values[row-1][col-1] = np_sum     
#----------------------------------------END YOUR CODE HERE----------------------------------------
# Verify your result
verify_result(pixel_values, new_pixel_values, mask)
# View the original image and the edges of the image
view_images(imgpath, new_pixel_values)