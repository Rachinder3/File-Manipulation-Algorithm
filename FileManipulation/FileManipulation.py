from logger.logger import Logger
import os
import shutil


class FileManipulation:
    __log_obj = Logger("Logs\\log.log")  # creating the log object

    def __init__(self, file_paths):
        self.__file_system = {}

        if os.path.exists("staging\\"):
            shutil.rmtree("staging\\")
        # create staging folder
        os.mkdir("staging")

        # copy files into staging folder

        for file in file_paths:
            file_name = file.split("\\")[-1]

            shutil.copyfile(file, "staging//" + file_name)

        # populate the file system

        files = os.listdir("staging\\")

        for file in files:
            file_name, extension = os.path.splitext(file)
            if extension in self.__file_system:
                self.__file_system[extension].append(file_name)
            else:
                self.__file_system[extension] = [file_name]

        FileManipulation.__log_obj.add_log("File Manipulation initialized")

    def create_folders(self):
        try:
            """ function that creates folder for each type of file extension"""
            # check if folders folder exits, delete if it does
            if os.path.exists("folders\\"):
                shutil.rmtree("folders\\")  # deleting the folder
            os.mkdir("folders")  # creating the folder which contains separate folder for separate file extension
            FileManipulation.__log_obj.add_log("FOLDERS folder created")

            # creating folders for each file

            for extension in self.__file_system:
                os.mkdir("folders\\" + extension)

                # copying files in the folder
                for individual_file in self.__file_system[extension]:
                    shutil.copyfile(src="staging\\" + individual_file + extension,
                                    dst="folders\\" + extension + "\\" + individual_file + extension)

            FileManipulation.__log_obj.add_log("folder created for each extension in folders folder")


        except Exception as e:
            FileManipulation.__log_obj.add_log("Error in create folder function")
            FileManipulation.__log_obj.add_log(str(e))

    def merge_files_same_extension(self, extension_to_be_merged, final_file_name):
        try:
            """ function that merges all the files with a given extension"""

            final_file = bytearray()  # object storing the bytes of merged file

            for file in self.__file_system[extension_to_be_merged]:
                # iterate over all the files whose extension is "extension to be merged"

                path = "staging\\" + file + extension_to_be_merged

                with open(path, "rb") as file_obj:
                    individual_byte_file = bytearray(file_obj.read())  # read bytes of single file

                    for index, byte in enumerate(individual_byte_file):
                        final_file.append(byte)  # append bytes into final_file

                # writing into final file
                final_path = "Merged_Files\\" + final_file_name + extension_to_be_merged

                with open(final_path, "wb") as file_obj:
                    file_obj.write(final_file)

            FileManipulation.__log_obj.add_log("merged file function successful")


        except Exception as e:
            FileManipulation.__log_obj.add_log("problem in merged file function")
            FileManipulation.__log_obj.add_log(str(e))

    def sort_on_names(self):
        try:
            """function that sorts all the files on the basis of names"""
            sorted_files = []

            for extension in self.__file_system:
                for file in self.__file_system[extension]:
                    sorted_files.append(file)

            FileManipulation.__log_obj.add_log("sort_on_names function successful")
            return sorted(sorted_files)

        except Exception as e:
            FileManipulation.__log_obj.add_log("Problem in sort_on_names function")
            FileManipulation.__log_obj.add_log(str(e))

    def sort_on_size(self):
        try:
            """function that sorts all the files on the basis of size of files"""
            sorted_files_dict = {}
            for extension in self.__file_system:
                for file in self.__file_system[extension]:
                    sorted_files_dict[file] = os.stat("staging\\" + file + extension).st_size

            sorted_files_dict = {k: v for k, v in sorted(sorted_files_dict.items(), key=lambda item: item[1])}

            FileManipulation.__log_obj.add_log("sort_on_size function successful")

            return list(sorted_files_dict.keys())


        except Exception as e:
            FileManipulation.__log_obj.add_log("problem in sort_on_size function")
            FileManipulation.__log_obj.add_log(str(e))

    @staticmethod
    def __patsearching(file_name, pattern):
        try:
            """function that searches for a given pattern in a given file"""
            """implements the naive pattern searching algorithm"""
            """helper function for searching function"""

            m = len(pattern)
            n = len(file_name)

            for i in range(0, n - m + 1):

                j = 0
                while j < m:
                    if pattern[j] != file_name[i + j]:
                        break
                    j += 1
                if j == m:
                    return file_name  # Pattern found in this file
            return -1  # Pattern not found in this file


        except Exception as e:
            FileManipulation.__log_obj.add_log("problem in patsearching file")
            FileManipulation.__log_obj.add_log(str(e))

    def searching(self, pattern):
        try:
            """generator function that searches for the files which satisfy a given pattern"""
            for extension in self.__file_system:
                for file in self.__file_system[extension]:
                    x = FileManipulation.__patsearching(file, pattern)

                    if x != -1:
                        yield x
        except Exception as e:
            FileManipulation.__log_obj.add_log("problem in searching algorithm")
            FileManipulation.__log_obj.add_log(str(e))

