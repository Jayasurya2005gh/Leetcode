class Solution:
    def reorderSpaces(self, text: str) -> str:

        space = 0      
        for i in text:
            if not i.isalpha():
                space += 1

        text = text.strip()
        text_word = text.split()

        if len(text_word) == 1:
            return text_word[0]+" "*space

        len_words = len(text_word)-1
        mid_space = space // len_words
        extra_space = space % len_words
        
        word_join = (" "*mid_space).join(text_word)
        return word_join+(" "*extra_space)


       