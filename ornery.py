"""
This type of object gets along with nobody!

自 = self in Chinese, disregard errors
"""

class Ornery:

    def __init__(自, name="Fred"):
        自.name = name
        print("A sourpuss is born!")

    def __getitem__(自, key):
        return "How dare you touch me with those brackets!"

    def __call__(自, *args, **kwargs):
        return "Don't call me at home!"

    def __getattr__(自, attr):
        return "I'm insulted you'd suppose I'd have {}".format(attr)

    def __repr__(自):
        return "Don't bother me!  Go away."

    def __invert__(自):
        return "I can't invert, are you kidding?"
