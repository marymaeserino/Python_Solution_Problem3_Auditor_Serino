import numpy as np
print("Enter ordered pair in np format as nx2 matrix")
print("Use function leastnorm() to run")
def leastnorm(val):
    a = val[:,0] #to get x coordinates of user input matrix
    b = val[:,1] #to get y coordinates of user input matrix
    lim=np.inf
    l=len(a) #size of matrix
    for i in range(0,10): #to limit up to 10th degree
        if i>=l:
            break
        reg=np.polyfit(a,b,i) #linear regression where i is the degree
        y=np.polyval(reg,a) #substituting x on p
        e=b-y #least norm error formula
        error=np.linalg.norm(e)
        bestfit=reg
    print('Coefficients of Best Fit Polynomial: ',bestfit) #output

