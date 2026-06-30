class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        list_list_strings = []
        for i, word in enumerate(strs):
            sorted_word = ''.join(sorted(list(word)))

            if sorted_word not in hash_map:
                hash_map[sorted_word] = [word]
            else:
                hash_map[sorted_word].append(word)

        for key in hash_map:
            list_list_strings.append(hash_map.get(key))

        return list_list_strings