"""In-class activity on practicing writing classes."""

class Profile:

    username: str
    private: bool

    def __init__(self, username_input: str):
        """Create new profile."""
        self.username = username_input
        self.private = True
        # return self
    
    def tweet(self, msg: str) -> None:
        """If Profile is not private, print msg."""
        if self.private is False:
            print(msg)


user1: Profile = Profile("110_rulez")
user1.private = False
user1.tweet("OOP is cool!")
