class Solution:

    def encode(self, strs: List[str]) -> str:
        # in this the return will be in the follwoing format :
        # len of string + delimiter + string 
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "#" + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            result.append(s[j+1:j+1+length])
            i = j+1+length
        return result