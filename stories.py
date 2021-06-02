"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, title, words, text):
        """Create story with words and template text."""
        self.title = title
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story1 = Story("short",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story("long", 
    ["noun1", "noun2", "noun3", "noun4", "verb1", "adjective1", "adjective2", "adjective3", "noun5", "adjective4", "noun6", "noun7", "noun8", "noun9", "adjective5", "adjective6", "noun10", "noun11", "verb2"],
"""I will tell you why. So shall my {noun1} prevent your discovery, 
   and your {noun2} to the king and queen moult no {noun3}. I have of late—but wherefore 
   I know not—lost all my {noun4}, forgone all custom of {verb1}, and 
   indeed it goes so {adjective1} with my disposition that this {adjective2} frame, the earth, 
   seems to me a {adjective3} {noun5}; this most excellent canopy, the air—look you, 
   this brave o'erhanging firmament, this {adjective4} roof fretted with golden fire—why, 
   it appears no other {noun6} to me than a foul and pestilent congregation of {noun7}. 
   What a piece of {noun8} is a man! How noble in reason, how infinite in {noun9}! 
   In form and moving how {adjective5} and {adjective6}! In action how like an angel, 
   in {noun10} how like a god! The {noun11} of the world. The paragon of animals. 
   And yet, to me, what is this quintessence of dust? Man delights not me. 
   No, nor woman neither, though by your {verb2} you seem to say so.""")