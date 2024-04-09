import sys
from fileMover import FileMover

def main():
    if len(sys.argv) < 3:
        print("Please declare both file path and the destination directory")
        return
    
    file_path = sys.argv[1]
    output_dir_path = sys.argv[2]

    dest_path = FileMover().move_file(file_path, output_dir_path)
    print(dest_path)

if __name__ == "__main__":
    main()
