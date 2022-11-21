from helper import Helper
from create_express import create_express

if __name__ == '__main__':
    Helper.dynamic_menu(['Criar projeto express',
    'Criar projeto flask'], 'MENU PRINCIPAL')
    choice_project = Helper.read_int('Digite sua escolha: ', 2)
    if(choice_project == 1):
        name_project = Helper.read_str('Digite o nome do seu projeto Express (Node.js): ', 3)
        create_express(name_project)