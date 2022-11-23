class g:
    N = 2
    x_0 = 0
    u_k = [-1, 1]
    x_k = [-1, 0, 1, 2]
    s_N = 1
    x_N = 3 # idkkk

def L(x_k, u_k):
    return x_k*u_k

class system:

    def calculate_final_state(self,x_N, s_N):
        # S_N = 1 so simplifies to x_N squared
        return s_N*x_N**2

    def check_constraint(self,x_k, u_k):
        # return true if the value is in x_k
        return x_k*u_k + u_k**2 in g.x_k

    def calc_state_eq(self,x_k, u_k):
        return x_k*u_k + u_k**2

    def L(self,x_k, u_k):
        return x_k*u_k

def main():

    print("\n\n")
    print("BEGIN PROGRAM\n")

    sys = system()

    # Calculate when K = N = 2
    J_star_N = dict() #create a dictionary

    for x_N in g.x_k:
        J_star_N[x_N] = sys.calculate_final_state(x_N, g.s_N)
    
    print("final J*(N) is:")
    print(J_star_N)
    print("-------------\n\n")
    print("Now Running for J*_N-1")
    

    # Calculate when K = N-1 = 1
    J_star_Nminus1 = dict()
    for x_k in g.x_k: # go through valid value of x
        
        intermediate_results = list() # create a list to store intermediate results 
                                      # this will store all the costs u_k for a given x_k
        for u_k in g.u_k: # go through every valid value of u
            # check if the value of u_k is valid based on system dynamics eq (constraint)
            if sys.check_constraint(x_k, u_k):
                # calculate x_k+1
                x_kplus1 = sys.calc_state_eq(x_k, u_k)
                result = sys.L(x_k, u_k) + J_star_N[x_kplus1]
                # if result < 0: continue
                intermediate_results.append(result)

                # print results
                print(f'x_k ={x_k} and u_k={u_k} so x_k+1 ={x_kplus1} and the cost={result}')
            else:
                print(f"skipped x_k ={x_k} and u_k ={u_k} because it doesnt satisfy constraint")
                continue
        
        # after going through all the u_k's for a given x_k,
        # calculate the minimum and append to J_star_Nminus1
        print(f"for x_k ={x_k} min result is {min(intermediate_results)}")
        print("----")
        J_star_Nminus1[x_k] = min(intermediate_results)

    print("final J*_N-1 is:")
    print(J_star_Nminus1)
    print("-------------\n\n")
    print("Now Running for J*_N-2")

    # Calculate when K = N-2 = 0
    J_star_Nminus2 = dict()
    for x_k in g.x_k: # go through valid value of x
        
        intermediate_results = list() # create a list to store intermediate results 
                                      # this will store all the costs u_k for a given x_k
        for u_k in g.u_k: # go through every valid value of u
            # check if the value of u_k is valid based on system dynamics eq (constraint)
            if sys.check_constraint(x_k, u_k):
                # calculate x_k+1
                x_kplus1 = sys.calc_state_eq(x_k, u_k)
                result = sys.L(x_k, u_k) + J_star_Nminus1[x_kplus1] # now using J_*N-1
                # if result < 0: continue
                intermediate_results.append(result) # this is the cost

                # print results
                print(f'x_k ={x_k} and u_k={u_k} so x_k+1 ={x_kplus1} and the cost={result}')
            else:
                print(f"skipped x_k ={x_k} and u_k ={u_k} because it doesnt satisfy constraint")
                continue
        
        # after going through all the u_k's for a given x_k,
        # calculate the minimum and append to J_star_Nminus1
        print(f"for x_k ={x_k} min result is {min(intermediate_results)}")
        print("----")
        J_star_Nminus2[x_k] = min(intermediate_results)

    print("final J*_N-2 is:")
    print(J_star_Nminus2)

    print("\n\nAll the J stars viewed together starting at N and going to N-2")
    print(f'J_star_N: {J_star_N}')
    print(f'J_star_Nminus1: {J_star_Nminus1}')
    print(f'J_star_Nminus2: {J_star_Nminus2}')
    print("\n")













#######################
#### Main Code
#######################

main()