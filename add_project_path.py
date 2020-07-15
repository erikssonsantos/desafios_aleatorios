class AddProjectPath:

    def add_project_path(self):

        from os.path import realpath
        from sys import path
        from ntpath import sep

        caminho_alvo = realpath('__file__').replace(f'__main__.py', '')
        sep_para_substituir = caminho_alvo[-1]

        if sep_para_substituir != sep:
            caminho = caminho_alvo.replace(sep_para_substituir, sep)
            path.insert(0, caminho)
        else:
            caminho = caminho_alvo
            path.insert(0, caminho)
