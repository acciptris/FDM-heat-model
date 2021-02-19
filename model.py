import functions
import makeGIF
import variables

#initialising variables
temp_initial = variables.temp_initial
temp_final = variables.temp_final
delta_x = variables.delta_x
delta_y = variables.delta_y
alpha = variables.alpha
k = variables.k
h = variables.h
delta_t = variables.delta_t
t = variables.t
L = variables.L

#number of nodes in each direction,
# i -> horizontal
# j -> vertical
ni = (int)(L/delta_x)
ni += 1
nj = (int)(L/delta_y)
nj += 1
n = nj

rx = (alpha*delta_t)/(delta_x ** 2)
ry = (alpha*delta_t)/(delta_y ** 2)

temp_old = functions.fill_matrix(temp_initial,n,n)
temp_new = functions.fill_matrix(temp_initial,n,n)

current_time = 0

temp_distributions = []
temp_distributions.append(temp_old)

while current_time < t:
    current_time += delta_t/2
    #j-sweep
    for j in range(1,n-1):  
        matrix = functions.fill_matrix(0,n,n)
        c = functions.fill_array(0,n)
        
        matrix[0][0] = -1
        matrix[0][1] = 1
        matrix[n-1][n-2] = (-1*k)/delta_x
        matrix[n-1][n-1] = (k/delta_x)+h
        c[n-1] = h * temp_final

        for i in range(1,n-1):
            matrix[i][i-1] = (-1*rx)/2
            matrix[i][i] = 1 + rx
            matrix[i][i+1] = (-1*rx)/2
            c[i] = temp_old[j][i] + (ry*(temp_old[j+1][i]+((-2)*temp_old[j][i])+temp_old[j-1][i]))/2
        
        temp_new[j] = functions.tdmSolver(matrix,c)

    temp_new[0] = temp_new[1]
    for i in range(n):
        temp_new[n-1][i] = ((h*temp_final*delta_y)+(k*temp_new[n-2][i]))/(k+h*delta_y)
    temp_old = temp_new.copy()

    current_time += delta_t/2
    #i-sweep
    for i in range(1,n-1):
        matrix = functions.fill_matrix(0,n,n)
        c = functions.fill_array(0,n)
        
        matrix[0][0] = -1
        matrix[0][1] = 1
        matrix[n-1][n-2] = (-1*k)/delta_y
        matrix[n-1][n-1] = (k/delta_y)+h
        c[n-1] = h * temp_final

        for j in range(1,n-1):
            matrix[j][j-1] = (-1*ry)/2
            matrix[j][j] = 1 + ry
            matrix[j][j+1] = (-1*ry)/2
            c[j] = temp_old[j][i] + (rx*(temp_old[j][i+1]+((-2)*temp_old[j][i])+temp_old[j][i-1]))/2
        
        #print(*matrix,sep="\n")
        temp_temporary = functions.tdmSolver(matrix,c)
        for j in range(n):
            temp_new[j][i] = temp_temporary[j]

    for j in range(n):
        temp_new[j][0] = temp_new[j][1]
        temp_new[j][n-1] = ((h*temp_final*delta_x)+(k*temp_new[j][n-2]))/(k+h*delta_x)
    temp_old = temp_new.copy()

    temp_distributions.append(temp_old)

for i in range(len(temp_distributions)):
    print("plot_heatmap ",i)
    functions.plot_heatmap(temp_distributions[i],i,temp_final,temp_initial)

makeGIF.makeGIF()
