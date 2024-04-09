import os

class FileReorganizer(object):

    def reorganize_file(self, file_path, output_file_path):
        if output_file_path == None:
            output_file_path="./test/output.txt"

        internally_ordered_lines = self._sort_each_line(file_path)

        self._create_output_dir(output_file_path)

        lines_sorted = sorted(internally_ordered_lines.keys())
        with open(output_file_path, "w") as output_file:
            for line in lines_sorted:
                initial_line = internally_ordered_lines[line]
                output_file.write(initial_line)

    def _create_output_dir(self, output_file_path):
        output_dir_path_segments = output_file_path.split("/")[0:-1]
        output_dir_path = "/".join(output_dir_path_segments)
        if not os.path.isdir(output_dir_path):
            os.mkdir(output_dir_path)


    def _sort_each_line(self, file_path):
        internally_ordered_lines = {}
        with open(file_path) as input_file:
            for line in input_file:
                ordered_line = "".join(sorted(line))
                internally_ordered_lines[ordered_line] = line
        return internally_ordered_lines
