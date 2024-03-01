# IS-I-python
```mermaid
classDiagram
    class FileProcessor {
      +count_word_occurrences(file_path: String, word: String): int
    }

    class TextFileProcessor {
      +count_word_occurrences(file_path: String, word: String): int
    }

    class JsonFileProcessor {
      +count_word_occurrences(file_path: String, word: String): int
    }

    class FileScanner {
      -processor_factory: ProcessorFactory
      +scan_files(folder_path: String, word: String): Map~String, Integer~
    }

    class ProcessorFactory {
      +get_processor(type: String): FileProcessor
    }

    FileProcessor <|-- TextFileProcessor : implements
    FileProcessor <|-- JsonFileProcessor : implements
    FileScanner --> ProcessorFactory : depends on
    ProcessorFactory ..> FileProcessor : creates
