#author__uy_thea
#date__october_3_2024
#section_bscpe_2-2


list_num_one = [] #create a list1
list_num_two = [] #create a list2

def get_number_of_values(): # a function that get the number of values
    while True:
        try:
            number_of_values = int(input("Enter the number of values: "))
        
        except:
            print("Invalid Input")
            continue

        else:
            return number_of_values

def create_list_of_tuple(list1,list2): #this function will combine the two lists
    result = []

    for i in range(len(list1)):
        tuple_element = (list1[i], list2[i])

        result.append(tuple_element)
    
    return result

value = get_number_of_values()

while True: #get all the values of the list 1
    try:
        for list1 in range(value):
            list1 = input(f"List Number One \n{list1 +1}) Enter the value: ")
            list_num_one.append(list1)


        break
    except:
        print("Invalid Input")
        continue



while True: #get all the values for the list 2
    try:
        for list2 in range(value):
            list2 = input(f"List Number Two \n{list2+1}) Enter a value: ")
            list_num_two.append(list2)
        
        break
        
    except:
        print("Invalid Input")
        continue


#combine the two lists using the create_list_of_tuple function
list_tuples = create_list_of_tuple(list_num_one,list_num_two)

#print the result
print(list_tuples)

#end of the program 