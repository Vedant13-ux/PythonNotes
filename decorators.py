# Decorator Function-When we wish to add some functionalities to our originally 
# existing function and then may be turn it of later for some reason,then Decorators comes into play.
def new_decorator(main_func):    
    def wrap_func():
        print('Some code before the main function')
        main_func()
        print('Some code after the main function')

    return wrap_func()

@new_decorator
def hello():
    print('Hello from Main Function') 


#Generators