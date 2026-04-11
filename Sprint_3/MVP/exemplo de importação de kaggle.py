import kagglehub
import pandas as pd
import os
from kagglehub import KaggleDatasetAdapter

def carregar_dataset_doacao_sangue():
    """
    Função para carregar o dataset de doação de sangue com diagnóstico automático
    """
    print("="*60)
    print("CARREGADOR DE DATASET - BLOOD DONOR REGISTRY")
    print("="*60)
    
    # Baixar o dataset para ver os arquivos
    try:
        path = kagglehub.dataset_download("tarekmasryo/blood-donor-registry-dataset")
        print(f"\n📂 Dataset baixado em: {path}")
        
        # Listar arquivos disponíveis
        arquivos = os.listdir(path)
        print(f"\n📋 Arquivos disponíveis ({len(arquivos)}):")
        for arquivo in arquivos:
            print(f"   - {arquivo}")
        
        # Tentar carregar cada arquivo CSV encontrado
        arquivos_csv = [f for f in arquivos if f.endswith('.csv')]
        
        if not arquivos_csv:
            print("\n❌ Nenhum arquivo CSV encontrado no dataset!")
            return None
        
        print(f"\n🔄 Tentando carregar arquivos CSV...")
        
        for arquivo in arquivos_csv:
            try:
                print(f"\n   Tentando: {arquivo}")
                df = kagglehub.dataset_load(
                    KaggleDatasetAdapter.PANDAS,
                    "tarekmasryo/blood-donor-registry-dataset",
                    arquivo
                )
                
                print(f"   ✅ Sucesso! Arquivo '{arquivo}' carregado.")
                print(f"   📊 Shape: {df.shape[0]} linhas x {df.shape[1]} colunas")
                print(f"\n   📋 Primeiras 5 linhas:")
                print(df.head())
                
                # Informações adicionais
                print(f"\n   📊 Informações do dataset:")
                print(f"   Colunas: {list(df.columns)}")
                print(f"   Tipos de dados:\n{df.dtypes}")
                
                return df
                
            except Exception as e:
                print(f"   ❌ Erro ao carregar '{arquivo}': {str(e)[:100]}...")
        
        print("\n❌ Não foi possível carregar nenhum arquivo CSV.")
        return None
        
    except Exception as e:
        print(f"\n❌ Erro ao baixar dataset: {e}")
        return None

# Executar a função
df = carregar_dataset_doacao_sangue()

# Se quiser acessar diretamente o caminho dos arquivos
if df is not None:
    print("\n" + "="*60)
    print("✅ DATASET CARREGADO COM SUCESSO!")
    print("="*60)