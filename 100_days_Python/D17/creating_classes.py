class User:

    def __init__(self, user_id, username):
        print('Created a new user...')
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers +=1
        self.following +=1


user_1 = User("001", 'thriller')
user_2 = User('002', 'jackson')

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)