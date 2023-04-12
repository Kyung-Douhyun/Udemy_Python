class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0  # 속성의 기본값 지정, 기본값은 매개변수 설정 불필요
        self.following = 0

    def follow(self, user):
        user.folllwers += 1
        self.following += 1


user_1 = User("123", "ABC")

print(user_1.id)
print(user_1.username)
print(user_1.followers)
