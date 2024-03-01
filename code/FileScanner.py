import os

class FileScanner:
    def __init__(self, processor_factory):
        self.processor_factory = processor_factory

    def scan_files(self, folder_path, word):
        results = {}  # Diccionario para almacenar los resultados del conteo
        for file_path in os.listdir(folder_path):
            full_path = os.path.join(folder_path, file_path)
            if file_path.endswith('.txt'):
                processor = self.processor_factory.get_processor('text')
            elif file_path.endswith('.json'):
                processor = self.processor_factory.get_processor('json')
            else:
                print(f"Tipo de archivo no soportado: {file_path}")
                continue
            # Contar ocurrencias y almacenar en el diccionario
            count = processor.count_word_occurrences(full_path, word)
            results[file_path] = count
        
        return results



