my_file=None
my_tries=5
while my_tries >0:
    try:
        print(f"you have {my_tries} tries left")
        files=(input("enter your path file => :").strip())
        my_file=open(files,"r")
        print(my_file.read())
        break
    except FileNotFoundError:
        print("file not found ")
        my_tries -=1
    except:
        print("error happens")
    finally:
        my_file.close()
        print("file closed")
else:
    print("end tries")
