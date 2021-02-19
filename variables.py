#Initial temperature of the whole block (in Kelvin)
temp_initial = 373.15

#Temperature of the surroundings or final temperature at steady state (in Kelvin)
temp_final = 298.15

#Material parameters (in SI units)
#Thermal Diffusivity
alpha = 1.6e-5
#Thermal Conductivity
k = 61 
#Hear transfer coefficient for convection
h = 400

#mesh-parameters
delta_x = 0.004
delta_y = 0.004
delta_t = 1

#Final time in seconds
t = 10
#Length of Square domain of block
L = 0.04