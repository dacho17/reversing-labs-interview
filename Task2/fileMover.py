import os
import shutil

class FileMover(object):

    def move_file(self, file_path, output_dir_path):
        dest_file_path = self._build_dest_file_path(file_path, output_dir_path)

        if not os.path.isdir(output_dir_path):
            os.mkdir(output_dir_path)

        try:
            shutil.move(file_path, dest_file_path)
            return dest_file_path
        except:
            print("An exception occurred while attempting to move the file")
            return None

    def _build_dest_file_path(self, file_path, output_dir_path):
        file_name = file_path.split("/")[-1]
        final_file_path = output_dir_path + "/" + file_name        
        
        return final_file_path
