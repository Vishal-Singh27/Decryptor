from sys import argv
from basic_functions import get_int
from decryptor import decrytor_normal, decrytor_advanced

def main():
    if len(argv) == 2:
        cyphercode = argv[1]
    else:
        cyphercode = input("Enter the cyphercode: ")
        
    key = -1
    
    while key < 0:
        key = get_int("Enter the key: ")
        if key < 0:
            print("Key must be greater than or equal to 0!")
    
    # Getting input of the choice
    choice = 1
    
    # while choice != 1 and choice != 2:
    #     print("Way of decyption:")
    #     print("1: Basic Encryption")
    #     print("2: Advanced Encryption")
    #     choice = get_int("Your Answer: ")
    
    if choice == 1:
        decypheredcode = decrytor_normal(cyphercode=cyphercode, key=key)
    
    else:
        decypheredcode = decrytor_advanced(cyphercode=cyphercode, key=key)
    
    print(decypheredcode)
    
if __name__ == "__main__":
    main()