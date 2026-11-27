
# without inherting 
'''
class whatsappv1:
    def messages(self):
        print("You can send the messages")

class whatsappv2:
    def audiocalls(self):
        print("You can call to the people")

print("------------user-1-------------")
user1 = whatsappv1()
user1.messages()

print("------------user-2-------------")
user1 = whatsappv2()
user1.audiocalls()
'''
# this is single inherritence

'''
class whatsappv1:
    def messages(self):
        print("You can send the messages")

class whatsappv2(whatsappv1):
    def audiocalls(self):
        print("You can call to the people")

print("------------user-1-------------")
user1 = whatsappv1()
user1.messages()

print("------------user-2-------------")
user2 = whatsappv2()
user2.audiocalls()
user2.messages()

'''

#this multi level inhertience
'''
class whatsappv1:
    def messages(self):
        print("You can send the messages")

class whatsappv2(whatsappv1):
    def audiocalls(self):
        print("You can call to the people")

class whatsappv3(whatsappv2):
    def videocalls(self):
        print("You can video call to people")


print("------------user-1-------------")
user1 = whatsappv1()
user1.messages()

print("------------user-2-------------")
user2 = whatsappv2()
user2.audiocalls()
user2.messages()

print("-------------user-3------------")
user3 = whatsappv3()
user3.messages()
user3.audiocalls()
user3.videocalls()
'''

'''
class whatsappv1:
    def messages(self):
        print("You can send the messages")

class whatsappv2:
    def audiocalls(self):
        print("You can call to the people")
class whatsappv3(whatsappv1,whatsappv2):
    def videocalls(self):
        print("You can video call to people")

print("------------user-1-------------")
user1 = whatsappv1()
user1.messages()

print("------------user-2-------------")
user2 = whatsappv2
user2.audiocalls()

print("----------user-3--------")
user3 = whatsappv3
user3.videocalls()
user3.audiocalls()
user3.messages()
'''
#this is higher archi 
'''
class whatsappv1:
    def messages(self):
        print("You can send the messages")

class whatsappv2(whatsappv1):
    def audiocalls(self):
        print("You can call to the people")
class whatsappv3(whatsappv1):
    def videocalls(self):
        print("You can video call to people")

print("------------user-1-------------")
user1 = whatsappv1()
user1.messages()

print("------------user-2-------------")
user2 = whatsappv2()
user2.audiocalls()
user2.messages()

print("-------------user-3----------")
user3 = whatsappv3()
user3.videocalls()
user3.messages()
'''

# this is hibrid inhertitence
'''
class whatsappv1:
    def messages(self):
        print("You can send the messages")

class whatsappv2(whatsappv1):
    def audiocalls(self):
        print("You can call to the people")
class whatsappv3(whatsappv2):
    def videocalls(self):
        print("You can video call to people")
class whatsappt1:
    def groups(self):
        print("You can create groups")
class whatsappt2:
    def comunities(self):
        print("You can create communities")
class whatsappv4(whatsappt1,whatsappt2,whatsappv3):
    def status(self):
        print("You can upload a status for 24 hours")

print("------------user-1-------------")
user1 = whatsappv1()
user1.messages()

print("------------user-2-------------")
user2 = whatsappv2()
user2.audiocalls()
user2.messages()

print("-------------user-3----------")
user3 = whatsappv3()
user3.videocalls()
user3.messages()
user3.audiocalls()

print("------------user-4----------")
user4 =whatsappv4()
user4.videocalls()
user4.messages()
user4.audiocalls()
user4.groups()
user4.comunities()
user4.status()
'''

# super method
'''
class whatsappv1:
    def status(self):
        print("You can upload your image and videos as status for 24 hours")

class whatsappv2(whatsappv1):
    def status(self):
        super().status()
        print("You can react/reply to the status")

class whatsappv3(whatsappv2):
    def status(self):
        super().status()
        print("You can like the status and add a song to it")

print("-------------user-1-----------")
user1 = whatsappv1()
user1.status()

print("-----------user-2-----------")
user2 = whatsappv2()
user2.status()

print("-----------user-3-----------")
user3 = whatsappv3()
user3.status()
'''


# class method
'''
class whatsappv1:
    def status(self):
        print("You can upload your image or video to the status for 24 hours")

class whatsappv2:
    def status(self):
        print("You can react/reply to the status")

class whatsappv3(whatsappv1,whatsappv2):
    def status(self):
        whatsappv1.status(self)
        whatsappv2.status(self)
        print("You can like the status and add a song to it")


print("---------------user-1-------------")
user1 = whatsappv1()
user1.status()

print("---------------user-2-------------")
user2 = whatsappv2()
user2.status()

print("---------------user-3-------------")
user3 = whatsappv3()
user3.status()

'''

