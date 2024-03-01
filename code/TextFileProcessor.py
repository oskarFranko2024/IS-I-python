# Procesador de archivos de texto
from FileProcessor import FileProcessor

class TextFileProcessor(FileProcessor):
    def count_word_occurrences(self, file_path, word):
        count = 0
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                count += line.lower().count(word.lower())
        return count


