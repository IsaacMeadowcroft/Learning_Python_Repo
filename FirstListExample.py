import random

def print_list(a_list):
    for i in a_list:
        print(i,end=' ')

def increment_list_by_index(a_list):
    for i in range(len(a_list)):
        a_list[i]+=i
    return a_list

def smallest_element(a_list):
    if(len(a_list)<1):
        print("Empty list")
    min=a_list[0]
    for i in a_list[1:]:
        if(i<min):
            min=i
    return min

def n_random_numbers(n):
    l=[]
    for i in range(n):
        l.append(round(random.random(),2))
    return l

if __name__ == "__main__":
    a_list = [5,2,-3,1,15]
    #print(increment_list_by_index(a_list))
    #pet_list = []
    #pet_list[0:0] = ['cat','dog','monkey','bird','fish']
    #print_list(pet_list)
    #print(smallest_element(a_list))
    print(n_random_numbers(5))
    
