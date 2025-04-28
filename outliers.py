marks = [45,48,49,50,51,52,54,100]


# detecting outliers using IQR

#step 1: Sort the data
#step 2: Find Q1(25th percentile) and Q3(75th percentile)
#step 3: set bounds: 
# Lower bound = Q1 - 1.5*IQR
# Upper bound = Q3 + 1.5*IQR

#Find the Q2 (median)
# Q2 = (50+51)/2 = 50.5

#Split the data into two halves
#Lower Half = [45,48,49,50]
#Upper Half = [51,52,54,100]

#find Q1 and Q3:
#Q1 = (48+49)/2 = 48.5
#Q3 = (52+54)/2 = 53

#Find IQR
#IQR = Q3 - Q1, 53 - 48.5 = 4.5

#Q1 - 1.5*IQR = 48.5 - 1.5*4.5 = 42
#Q3 + 1.5*IQR = 53 + 1.5*4.5 = 60

# takes value from user like: 25 48 96 74 52 
# detect outliers