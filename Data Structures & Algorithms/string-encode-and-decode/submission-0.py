class Solution:

    def encode(self, strs: List[str]) -> str:
        #Makin an empty string to add the list of strings
        encoded_strs = ""
        for i in strs:
            encoded_strs += str(len(i)) + "#" + i
        return encoded_strs

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0

        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])

            word_starting = j +1
            word_ending = j + 1 + length

            word = s[word_starting:word_ending]
            decoded_strs.append(word)

            i = word_ending
        return decoded_strs

