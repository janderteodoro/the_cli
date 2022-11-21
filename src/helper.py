import os
from config_env import config_env

path_project = config_env()['PATH_PROJECT']

class Helper:

    def create_folder(folder):
        path_folder = f'{path_project}/{folder}'
        if not os.path.exists(path_folder):
            os.mkdir(path_folder)

    def create_many_folders(folders):
        folders_list = []
        for folder in folders:
                os.makedirs(folder)
                folders_list.append(folder)
        return folders_list


    def dynamic_menu(itens, text):
        print('=' * 60)
        print(text.center(60))
        print('=' * 60)

        c = 1 

        for i in itens:
            print(f'[{c}] - {i}')
            c += 1
        
        print()


    def read_int(txt, itensAmount):
        while True:
            try:
                n = int(input(txt))
            except(TypeError, ValueError):
                print('Insira números por favor')
                continue
            else:
                if ( n < 1 ) or ( n > itensAmount ):
                    print('Opção Inválida. Tente Novamente')
                    continue
                else:
                    return n



    def read_str(txt, size):
        while True:
            try:
                word = str(input(txt).strip())
            except(TypeError, ValueError):
                print('Insira números por favor')
                continue
            else:
                if len(word) < size:
                    print(f'Necessário pelo menos {size} letras')
                    continue
                else:
                    return word


    def create_file(file, mode, content):
        f = open(file, mode)
        f.write(content)
        f.close

Helper.create_folder('testezim')