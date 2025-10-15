class Member:
    not_allawed_names=["hima","figo"]
    users_num=0


    @classmethod 
    def show_user_count(cls):
        return f"number of users {cls.users_num}"
    @staticmethod
    def say_good():
        return 'good mornning'


    def __init__(self,firstName,lastName):
        self.fname=firstName
        self.lname=lastName
        Member.users_num +=1
    def say_hello(self):
        return f"Hello {self.fname}"
    def delete_user(self):
        Member.users_num -=1
        print(f"user {self.fname} is deleted")


uOne=Member("Hassan","zizo")
uTwo=Member("ahmed","hassan")
uthree=Member("hima","figo")


print(Member.users_num)

print(uOne.say_hello())      
print(uTwo.say_hello())      
print(uthree.say_hello())    

print(Member.users_num)
print(Member.show_user_count())
print(Member.say_good())
