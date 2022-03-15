from FileManipulation.FileManipulation import FileManipulation

if __name__ == '__main__':
    file_paths = ["Input_files\\csv_1.csv",
                  "Input_files\\csv_2.csv",
                  "Input_files\\excel_1.xlsx",
                  "Input_files\\excel_2.xlsx",
                  "Input_files\\pdf_1.pdf",
                  "Input_files\\pdf_2.pdf",
                  "Input_files\\txt_1.txt",
                  "Input_files\\txt_2.txt",
                  "Input_files\\word_1.docx",
                  "Input_files\\word_2.docx",
                  ]

    file_system = FileManipulation(file_paths)

    # create folder for each file
    file_system.create_folders()

    print("-----------------------------------------------------------------------------")

    # merge files function

    file_system.merge_files_same_extension(".csv", "merged")

    print("-----------------------------------------------------------------------------")

    # sort on names
    files = file_system.sort_on_names()
    print("sorting on names")
    print(files)

    print("-----------------------------------------------------------------------------")

    # sort on size
    files = file_system.sort_on_size()
    print("sorting on size")
    print(files)

    print("-----------------------------------------------------------------------------")

    # pattern searching
    pattern = "pd"
    for file in file_system.searching(pattern):
        print(file)

    print("-----------------------------------------------------------------------------")