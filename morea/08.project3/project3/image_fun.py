
#
# image_fun.py
#

from png_helper import *

def change( p ):
    """ change takes in a pixel (an [R,G,B] list)
        and returns a new pixel to take its place!
    """
    red = p[0]
    green = p[1]
    blue = p[2]
    return [ 255-red, 255-green, 255-blue ]


def invert(file_in, file_out):
    """ run this function to read in the in.png image,
        change it, and write out the result to out.png
    """
    Im_pix = getRGB( file_in )  # read in the in.png image
    print "The first two pixels of the first row are",
    print Im_pix[0][0:2]
    # remember that Im_pix is a list (the image)
    # of lists (each row) of lists (each pixel is [R,G,B])
    New_pix = [ [ change(p) for p in row ] for row in Im_pix ]
    # now, save to the file 'out.png'
    saveRGB( New_pix, file_out )

# You can also unroll the list comprehension to create New_pix
# instead of [ [ change(p) for p in row ] for row in Im_pix ]
#     New_pix = []
#     for row in Im_pix:
#     	new_row = []
#     	for p in row:
#     		new_row.append(change(p))
#     	New_pix.append(new_row)

invert('spam.png', 'out2.png') # test & compare with out.png
#invert('trees.png', 'trees_inverted.png')
#invert('arch.png', 'arch_inverted.png')


