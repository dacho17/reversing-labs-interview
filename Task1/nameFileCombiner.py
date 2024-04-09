# 1. sort output entries by id number
# 2. TODO: input data is too big to fit into main memory

class NameFileCombiner(object):
    def combine_name_files(self, output_file_path, first_name_path, last_name_path):
        first_names = self._read_name_file(first_name_path)
        last_names = self._read_name_file(last_name_path)
        
        name_ids = sorted(first_names.keys())
        
        self._write_name_file(output_file_path, name_ids, first_names, last_names)

    def _read_name_file(self, file_path):
        sol = {}
        with open(file_path) as file:
            for line in file:
                name, id_number = line[0:-1].split(" ") # remove new line char
                sol[id_number] = name
        return sol

    def _write_name_file(self, output_file_path, name_ids, first_names, last_names):
        with open(output_file_path, 'w') as output_file:
            for name_id in name_ids:
                first_name = first_names[name_id]
                last_name = last_names[name_id]
                output_line = "{} {} {}\n".format(first_name, last_name, name_id)
                output_file.write(output_line)
