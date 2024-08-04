import sys
import os
from cx_Freeze import setup, Executable

arquivos = ['db_utils.py', 'python.ico']

config = Executable(
    script='app.py',
    icon='python.ico'
)

setup(
    name='Gerenciador de tarefas',
    version='1.0',
    description='Este programa gerencia tarefas salvas em um banco de dados feito em SQLite3.',
    author='Carlos Rodrigues',
    options={'build_exe': {'include_files': arquivos}},
    executables=[config]
)
