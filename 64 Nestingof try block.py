try:
    print("line1")
    print("line2")
    try:
        print("line3")
        3+"5"
        print("line4")
    except ZeroDivisionError:
        print("Except1")
    finally:
        print("finally1")
    print("line5")
except TypeError:
    print("Except2")
finally:
    print("finally2")
