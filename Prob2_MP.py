from math import *
import numpy as bi


x1 = float(input("\nEnter first X coordinate: "));
y1 = float(input("\nEnter first Y coordinate: "));
x2 = float(input("\nEnter secomd X coordinate: "));
y2 = float(input("\nEnter secomd Y coordinate: "));
x3 = float(input("\nEnter third X coordinate: "));
y3 = float(input("\nEnter third Y coordinate: "));

#Get the coordinates of the center of the circle (x,y): 

a = ((x1-x2)**2) + ((y1-y2)**2);
b =((x2-x3)**2) + ((y2-y3)**2);
c = ((x3-x1)**2) + ((y3-y1)**2);

eq = ((a*b + b*c + c*a)*2) - ((a**2) + (b**2) + (c**2));

h = (a*(b+c-a)*x3 + b*(c+a-b)*x1 + c*(a+b-c)*x2)/eq;
k = (a*(b+c-a)*y3 + b*(c+a-b)*y1 + c*(a+b-c)*y2)/eq;

# Get the radius (r) of the circle:

r = sqrt(((x1-h)**2) + ((y1-k)**2));


#Get D,E,F using determinants


A = bi.array([((((x1)**2)+((y1)**2)), y1, 1),
              ((((x2)**2)+((y2)**2)), y2, 1),
              ((((x3)**2)+((y3)**2)), y3, 1)]);

B = bi.array([((((x1)**2)+((y1)**2)), x1, 1),
              ((((x2)**2)+((y2)**2)), x2, 1),
              ((((x3)**2)+((y3)**2)), x3, 1)]);

C = bi.array([((((x1)**2)+((y1)**2)), x1, y1),
              ((((x2)**2)+((y2)**2)), x2, y2),
              ((((x3)**2)+((y3)**2)), x3, y3)]);

Z = bi.array([(x1, y1, 1),
              (x2, y2, 1),
              (x3, y3, 1)]);

D = (-1*bi.linalg.det(A))/bi.linalg.det(Z);
E = (bi.linalg.det(B))/bi.linalg.det(Z);
F = (-1*bi.linalg.det(C))/bi.linalg.det(Z);


print("\nThe central coordinates (x,y) of the circle is located at: (",h,", ",k,")");  
print("It has a radius of: ", r);
print("With coefficients \nD: ",D,"\nE:",E,"\nF:",F);
