def reverse_string():
    user_input = input("Enter the word you want to be reversed: ")
    reverse = user_input [:: -1]
    print(reverse)
    
def reverse_list():
    list = [2, 4, 6, 8, 10, 12 , 14, 16, 18, 20]
    reverse_num = list [:: -1]
    print(reverse_num)
    
def reverse_tuple():
    tuple = ("Porshe", "Mercedes", "Ferarri", "Aston Martin", "Lamboghini")
    reverse_tuple = tuple [:: -1]
    print(reverse_tuple)

# def reverse_set():
#     set = {"steak and kidney pie", "chicken and mushrom pie", "mutton curry pie", "burger pie"}
#     reverse_set = set [:: -1]
#     print(reverse_set)
    
    

if __name__ == "__main__":   
    reverse_string()
    reverse_list()
    reverse_tuple()