import pathlib
import os


def main():
    output_dir = 'tests_dir/'

    with open("input_files-02.txt", "r") as f:
        for file_name in f.readlines():
            file_name = file_name.replace('./', '')
            file_name = file_name.replace('\n', '')
            if file_name == "." or file_name.endswith("DS_Store"):
                continue

            # Assuming that if it doesn't end with pdf it's a dir
            if not file_name.lower().endswith(".pdf"):
                pathlib.Path(
                    output_dir + file_name).mkdir(parents=True, exist_ok=True)
                continue

            if not pathlib.Path(output_dir + file_name).parents[0].is_dir():
                pathlib.Path(
                    output_dir + file_name).mkdir(parents=True, exist_ok=True)

            pathlib.Path(output_dir + file_name).touch()

    with open("files_created.txt", "w") as w:

        for root, sub_dirs, files in os.walk(output_dir):
            if len(files) == 0:
                continue

            for file in files:
                w.write(root.replace(output_dir, '') + '/' + file + '\n')


if __name__ == "__main__":
    main()
