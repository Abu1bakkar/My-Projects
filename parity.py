
#define main function
def main():
    x= int(input("Whats x?"))
    #call is_even here and output accordingly
    if is_even(x):
        print("Even")
    else:
        print("Odd")

#define is_even function
def is_even(n):
    #returns true if remainder 0 otherwise returns false
    return True if n%2==0 else False
        
    
#call main
main()



