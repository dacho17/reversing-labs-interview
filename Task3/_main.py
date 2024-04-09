import sys
from fileReorganizer import FileReorganizer

def main():
    if len(sys.argv) < 2:
        print("Please declare input file path")
        return

    file_path = sys.argv[1]
    output_file_path = sys.argv[2] if len(sys.argv) >= 3 else None
        
    FileReorganizer().reorganize_file(file_path, output_file_path)

if __name__ == "__main__":
    main()
