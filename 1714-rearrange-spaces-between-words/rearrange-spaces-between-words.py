class Solution:
    def reorderSpaces(self, text: str) -> str:
        space = 0

        # Count spaces
        for i in text:
            if i == " ":
                space += 1

        # Split words (ignores extra spaces)
        text_word = text.split()

        # Case 1: Only one word
        if len(text_word) == 1:
            return text_word[0] + " " * space  

        # Case 2: Multiple words
        len_words = len(text_word) - 1
        mid_space = space // len_words
        extra_space = space % len_words

        word_join = (" " * mid_space).join(text_word)
        return word_join + (" " * extra_space)
