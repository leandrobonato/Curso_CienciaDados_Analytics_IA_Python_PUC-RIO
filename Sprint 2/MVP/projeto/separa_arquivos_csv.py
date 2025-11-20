import pandas as pd
import os

def split_csv_by_size(input_file, output_dir, max_size_mb=50):
    """
    Separa um arquivo CSV grande em arquivos menores com base no tamanho máximo.

    :param input_file: Caminho para o arquivo CSV de entrada.
    :param output_dir: Diretório onde os arquivos divididos serão salvos.
    :param max_size_mb: Tamanho máximo de cada arquivo dividido (em MB).
    """
    # Converte o tamanho máximo para bytes
    max_size_bytes = max_size_mb * 1024 * 1024

    # Cria o diretório de saída, se ele não existir
    os.makedirs(output_dir, exist_ok=True)

    # Lê o cabeçalho do arquivo CSV
    with open(input_file, 'r') as f:
        header = f.readline()

    # Inicializa variáveis
    chunk_size = 10000  # Número inicial de linhas por chunk (ajustável)
    file_index = 1
    current_chunk = []
    current_size = len(header.encode('utf-8'))  # Começa com o tamanho do cabeçalho

    # Lê o arquivo CSV em chunks
    for chunk in pd.read_csv(input_file, chunksize=chunk_size):
        for _, row in chunk.iterrows():
            # Converte a linha para string e calcula seu tamanho em bytes
            row_str = ','.join(map(str, row.values)) + '\n'
            row_size = len(row_str.encode('utf-8'))

            # Verifica se a linha cabe no arquivo atual
            if current_size + row_size > max_size_bytes:
                # Salva o chunk atual como um novo arquivo
                output_file = os.path.join(output_dir, f'part_{file_index}.csv')
                with open(output_file, 'w') as f:
                    f.write(header)
                    f.writelines(current_chunk)
                
                # Reinicia variáveis para o próximo arquivo
                file_index += 1
                current_chunk = [row_str]
                current_size = len(header.encode('utf-8')) + row_size
            else:
                # Adiciona a linha ao chunk atual
                current_chunk.append(row_str)
                current_size += row_size

    # Salva o último chunk, se houver
    if current_chunk:
        output_file = os.path.join(output_dir, f'part_{file_index}.csv')
        with open(output_file, 'w') as f:
            f.write(header)
            f.writelines(current_chunk)

    print(f"Arquivo dividido em {file_index} partes.")

# Exemplo de uso
input_csv = "D:/dados_nc/.csv"
output_directory = "caminho/para/diretorio_saida"
split_csv_by_size(input_csv, output_directory, max_size_mb=50)