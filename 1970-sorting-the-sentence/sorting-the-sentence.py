class Solution:
    def sortSentence(self, s: str) -> str:
        sen=s.split()
        final=[""]*len(sen)
        for words in sen:
            position=int(words[-1])
            word=words[:-1]
            final[position-1]=word
        return " ".join(final)


            
            
