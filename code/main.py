from FileScanner import FileScanner
from ProcessorFactory import ProcessorFactory

def main():
    # Crear una fábrica de procesadores y el escáner de archivos
    factory = ProcessorFactory()
    scanner = FileScanner(factory)
    
    # Solicitar al usuario la ruta de la carpeta y la palabra a buscar
    folder_path = input("Ingrese la ruta de la carpeta: ")
    word = input("Ingrese la palabra a buscar: ")
    
    # Recibir los resultados del conteo y manejarlos aquí
    results = scanner.scan_files(folder_path, word)
    for file, count in results.items():
        print(f"'{word}' encontrado {count} veces en {file}")


if __name__ == "__main__":
    main()


