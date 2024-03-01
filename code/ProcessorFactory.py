
from JsonFileProcessor import JsonFileProcessor
from TextFileProcessor import TextFileProcessor


class ProcessorFactory:
    def get_processor(self, type):
        if type == 'text':
            return TextFileProcessor()
        elif type == 'json':
            return JsonFileProcessor()
        # Agregar más tipos según sea necesario

