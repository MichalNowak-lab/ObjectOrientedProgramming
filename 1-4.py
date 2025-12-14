class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")
    def display_timeline(self):
        print(f'name: {self.username}, posts: {self.posts}, number of posts {len(self.posts)}')

def main():
    acc1=SocialMediaProfile('johndoe')
    acc1.add_post('hello, world!')
    acc1.add_post('Had a great day at the park!')
    acc1.add_post("What's up, Natalie? How are you?")
    acc1.display_timeline()
if __name__ == '__main__':
    main()