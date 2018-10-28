class SuffixTrie(object):
    def __init__(self, text):
        '''construct suffix trie from text'''
        text += '$'
        self.root = {}
        for i in range(len(text), -1, -1):
            curr = self.root
            suffix = text[i:]
            for char in suffix:
                if char not in curr:
                    curr[char] = {}
                curr = curr[char]

    def traverse(self, s):
        '''
        traverse the trie by following characters of s
        :param s : query string
        :return : suffix trie node at end of path, or None due to premature exit
        '''
        curr = self.root
        for char in s:
            if char not in curr:
                return None
            curr = curr[char]
        return curr

    def has_substring(self, s):
        '''
        return true iff s appears as a substring of text
        :param s : query string
        :return bool: True if s is a substring else False
        '''
        return self.traverse(s) is not None

    def has_suffix(self, s):
        '''
        return true iff s is a suffix of text
        :param s : query string
        return true iff s is a suffix of text
        '''
        curr_node = self.traverse(s)
        return True if curr_node is not None and '$' in curr_node else False


s = SuffixTrie('ABCD')
print(s.has_substring('BC'))
print(s.has_substring('BX'))
print(s.has_suffix('BCD'))
print(s.has_substring('ABX'))
