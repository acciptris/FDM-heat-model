import seaborn as sns
import matplotlib.pyplot as plt

# Return a 2 dimensional list of 'row' rows and 'col' cols all initialised to 'val'
def fill_matrix(val,row,col):
    m = []
    for i in range(row):
        temporary_new = []
        for j in range(col):
            temporary_new.append(val)
        m.append(temporary_new)
    return m

# Return a list of size 'size' all initialised to 'val'
def fill_array(val,size):
    a = []
    for i in range(size):
        a.append(val)
    return a

# Return c/matrix using thomas algorithm and matrix is a tridiagonal matrix
def tdmSolver(matrix,c):
    n = len(c)
    result = fill_array(0,n)
    
    for i in range(n-1):
        matrix[i][i+1] /= matrix[i][i]
        c[i] /= matrix[i][i]
        matrix[i][i] = 1
        
        matrix[i+1][i+1] -= matrix[i+1][i]*matrix[i][i+1]
        c[i+1] -= matrix[i+1][i]*c[i]
        matrix[i+1][i] = 0

    result[n-1] = c[n-1]/matrix[n-1][n-1]
    for i in range(n-2,-1,-1):
        result[i] = (c[i] - matrix[i][i+1]*result[i+1])/matrix[i][i]
    
    return result

def print_text_temperature(file_name,temp):
    with open(file_name,"w") as f:
        for j in range(len(temp)):
            for i in temp[j]:
                f.write(f'{round(i,4):8}\t')
            f.write("\n")

def plot_heatmap(temperature,filename,temp_final,temp_initial):
    
    for i in range(len(temperature)):
        temp_list = temperature[i].copy()
        for j in range(1,len(temperature[i])):
            temp_list.insert(0,temperature[i][j])
        temperature[i] = temp_list.copy()
    
    temp_list = temperature.copy()
    for i in range(1,len(temperature)):
        temp_list.insert(0,temperature[i])
    temperature = temp_list.copy()
    
    plt.figure()
    hmap = sns.heatmap(data = temperature,vmin=min(temp_final,temp_initial),vmax=max(temp_final,temp_initial),cmap="gnuplot")
    hmap.figure.savefig("fig/"+f"{filename:05d}"+".png")