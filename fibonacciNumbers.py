"""
Created on Mon Oct 10 18:19:36

@author: tyler nelson
"""
import numpy as np
import matplotlib.pyplot as plt

def make_Fibonacci(n):
    """
    
    Parameters
    ----------
    n : TYPE integer
        Description. the lenth of the fibinocci sequence returned 
    
    Returns 
    --------
    F: a list that contwains the first n fibonocci number    
    
    """ 
#%%  you can use this to make a cell which you can run alone
    n = 10
    F=[1,1]  
    if n == 1:
        F = [1]#F.append(1)
        return F
    '''   
    elif n==2:
        #F.append(1)
        #F.append(1)
        F.append((1,1))
        #return F
        ''' 
    for i in range(2,n):
        F.append(F[i-1]+F[i-2])   
    return F


def converging_ratios(F):
    import numpy as np
    golden_ratio = (1+np.sqrt(5))/2
    n = len(F)
    print(f"Length of F is {n}")
    #n = F.length
    e =[]
    for i in range(1,n-1):
        error = F[i+1]/F[i] - golden_ratio
        e.append(error)
        #print(f"the error of F{n+1}/F[{n}] is ratio")
    ''''''
    return e
    #e{N} = C*e{N}**q
    #q = np.log(e[N+1]/e[N]) / np.log
    
def computer_ratee(e):
    n = len(e)
    e=[abs(x) for x in e]
    q=[]
    for i in range(n-1):
        q.append(objectnp.log(e[i+1]/e[i]) / np.log(e[i]/e[i-1])) #= np.log(e[i+1]/e[i]) / np.log(e[i]/e[i-1])
    return q

if __name__ == '__main__':
    print(make_Fibonacci(20))
    B=make_Fibonacci(20)
    print(converging_ratios(B))
