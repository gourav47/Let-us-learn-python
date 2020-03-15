##Showing the result as Pass or Fail##
def decor_result(result_function):
    def distinction(marks):
        for m in marks:
            if m>=75:
                print("Congrats!!, you have got distinction")
        else:
            result_function(marks)
    return distinction    
def result(marks):
    for m in marks:
        if m>=33:
            pass
        else:
            print("Fail")
    else:
        print("Pass")
result([50,60,70,80,90,100])
        
