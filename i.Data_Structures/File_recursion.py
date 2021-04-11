import os
def find_files(suffix, path):
    if os.path.exists(path):
        filepath_list = []
    else:
        return []
    for each in os.listdir(path):
        new_path=os.path.join(path,each)
        if os.path.isfile(new_path) and new_path.endswith(suffix):
            filepath_list.append(new_path)
        if os.path.isdir(new_path):
            filepath_list+=find_files(suffix,new_path)
    return filepath_list


# test
print(find_files('.c', 'testdir'))
print(find_files('.h', 'testdir'))
print(find_files('.c', ''))
print(find_files('.c', 'testdir/subdir5'))