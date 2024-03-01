from abc import ABC, abstractmethod

# Interfaz para procesadores de archivos
class FileProcessor(ABC):
    @abstractmethod
    def count_word_occurrences(self, file_path, word):
        pass


