import json
from FileProcessor import FileProcessor

class JsonFileProcessor(FileProcessor):
    def count_word_occurrences(self, file_path, word):
        count = 0
        with open(file_path, 'r', encoding='latin1') as file:
            data = json.load(file)
            count = self._count_in_dict(data, word)
        return count

    def _count_in_dict(self, data, word):
        if isinstance(data, dict):
            return sum(self._count_in_dict(v, word) for v in data.values())
        elif isinstance(data, list):
            return sum(self._count_in_dict(item, word) for item in data)
        elif isinstance(data, str):
            return data.lower().count(word.lower())
        else:
            return 0

