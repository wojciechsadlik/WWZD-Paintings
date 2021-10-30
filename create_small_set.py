import os
import shutil

def main():
    prepare_dirs()
    copy_files(50)
    print('done')
    return

def prepare_dirs():
    try:
        os.mkdir('dataset_small/')
    except OSError:
        shutil.rmtree('dataset_small')
        os.mkdir('dataset_small/')

    for entry in os.listdir('dataset_full/'):
        if os.path.isdir(os.path.join('dataset_full/', entry)):
            os.mkdir('dataset_small/' + entry)

def copy_files(files_number):
    for dirpath, dirnames, files in os.walk('dataset_full/'):
        i = 0
        for file_name in files:
            shutil.copy(os.path.join(dirpath, file_name), os.path.join('dataset_small/', os.path.basename(dirpath)))
            
            i += 1
            if (i >= files_number):
                break

if __name__ == '__main__':
    main()