class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        all_words = []
        for word in strs:
            count_of_chars = [0] * 26
            for char in word:
                count_of_chars[ord(char) - ord('a')] += 1

            key = tuple(count_of_chars)
            if key not in hash_map:
                hash_map[key] = [word]
            else:
                hash_map[key].append(word)

        for key in hash_map:
            all_words.append(hash_map[key])

        return all_words