import matplotlib.pyplot as plt
#import matplotlib.patches as mpatches
import numpy as np
import csv

#Opens first file
csvfile1 = open("CloudFraction1_2002.csv", 'r')
#Reads the file
reader02 = csv.reader(csvfile1, delimiter =',')
#Turns first file into list
data1 = list(reader02)

#Opens second file
csvfile2 = open("CloudFraction1_2017.csv", 'r')
#Reads the file
reader17 = csv.reader(csvfile2, delimiter = ',')
#Turns second file into list
data2 = list(reader17)

#list of lists; counting rows, then columns
row1 = len(data1)
#When the computer opens it, it reads the column first then the row
col1 = len(data1[0])
row2 = len(data2)
col2 = len(data2[0])

#Creates an empty NumPy array with three dimensions: 
#data rows, #data columns and 3 (for the three values of each RGB color). 
grid02 = np.empty([row1, col1, 3], dtype=np.uint8)
grid17 = np.empty([row2, col2, 3], dtype=np.uint8)

#Resets the CSV reader to the start of the file
csvfile1.seek(0)

#Iterates over the values in the CSV file 
#assignes the proper color to the appropriate spot in the grid array(using RGB colors)
rownum = -1
for row in reader02:
    rownum += 1
    colnum = -1
    #print(rownum)
    for value in row:
        colnum += 1
        #print (colnum)
        if float(value) <= 0.1:
            grid02[rownum, colnum] = [0, 34, 89]
        elif float(value) <= 0.2:
            grid02[rownum, colnum] = [0, 48, 127]
        elif float(value) <= 0.3:
            grid02[rownum, colnum] = [3, 72, 183]
        elif float(value) <= 0.4:
            grid02[rownum, colnum] = [11, 93, 226]
        elif float(value) <= 0.5:
            grid02[rownum, colnum] = [47, 120, 237]
        elif float(value) <= 0.6:
            grid02[rownum, colnum] = [72, 137, 242]
        elif float(value) <= 0.7:
            grid02[rownum, colnum] = [127, 170, 239]
        elif float(value) <= 0.8:
            grid02[rownum, colnum] = [147, 181, 237]
        elif float(value) <= 0.9:
            grid02[rownum, colnum] = [174, 199, 239]
        elif float(value) <= 1.0:
            grid02[rownum, colnum] = [232, 232, 242]
        else:
            grid02[rownum, colnum] = [229, 18, 25]
 
    
#closes our csv file        
csvfile2.seek(0)
  
rownum = -1
for row in reader17:
    rownum += 1
    colnum = -1
    for value in row:
        colnum += 1
        if float(value) <= 0.1:
            grid17[rownum, colnum] = [0, 34, 89]
        elif float(value) <= 0.2:
            grid17[rownum, colnum] = [0, 48, 127]
        elif float(value) <= 0.3:
            grid17[rownum, colnum] = [3, 72, 183]
        elif float(value) <= 0.4:
            grid17[rownum, colnum] = [11, 93, 226]
        elif float(value) <= 0.5:
            grid17[rownum, colnum] = [47, 120, 237]
        elif float(value) <= 0.6:
            grid17[rownum, colnum] = [72, 137, 242]
        elif float(value) <= 0.7:
            grid17[rownum, colnum] = [127, 170, 239]
        elif float(value) <= 0.8:
            grid17[rownum, colnum] = [147, 181, 237]
        elif float(value) <= 0.9:
            grid17[rownum, colnum] = [174, 199, 239]
        elif float(value) <= 1.0:
            grid17[rownum, colnum] = [232, 232, 242]
        else:
            grid17[rownum, colnum] = [229, 18, 25]
            
#closes our csv file     
csvfile1.close()
csvfile2.close()

plt.clf()#to clear all prebvious graphs
#creat the grid/map
plt.suptitle("Cloud Coverage 2002", y=.92, x=.4)
plt.imshow(grid02)
plt.axis('off')
plt.show()

#printes our plot
plt.suptitle("Cloud Coverage 2017", y=.92, x=.4)
plt.imshow(grid17)
plt.axis('off')
plt.show()