import xarray as xr
import pandas as pd
import os

# Caminho para a pasta contendo os arquivos .nc
data_path = "D:/dados_nc"  # Altere para o caminho correto da sua pasta

# Listar os arquivos .nc na pasta
file_paths = [os.path.join(data_path, file) for file in os.listdir(data_path) if file.endswith(".nc")]

# Verificar se há arquivos .nc
if not file_paths:
    raise ValueError("Nenhum arquivo .nc encontrado na pasta.")

# Carregar cada arquivo individualmente e garantir que os índices de tempo sejam monotônicos
datasets = []
for file_path in file_paths:
    try:
        ds = xr.open_dataset(file_path, decode_times=False)
        
        # Garantir que a dimensão 'time' esteja monotônica
        if "time" in ds.variables:
            ds = ds.sortby("time")  # Ordenar por 'time'
        
        datasets.append(ds)
    except Exception as e:
        print(f"Falha ao carregar o arquivo {file_path}: {e}")

# Concatenar os datasets manualmente
try:
    combined_data = xr.concat(datasets, dim="time")  # Usar 'time' como dimensão de concatenação
    print("Arquivos combinados com sucesso!")
except Exception as e:
    raise ValueError(f"Falha ao combinar arquivos: {e}")

# Decodificar manualmente a variável 'time' usando cftime
if "time" in combined_data.variables:
    time_units = combined_data["time"].attrs.get("units", "")
    raw_time_values = combined_data["time"].values  # Valores brutos (números)

    # Identificar o tipo de unidade de tempo
    if "days since" in time_units:
        reference_date = pd.Timestamp(time_units.split("days since ")[1])  # Extrair a data de referência
        decoded_dates = [reference_date + pd.Timedelta(days=int(t)) for t in raw_time_values]
    elif "months since" in time_units:
        reference_date = pd.Timestamp(time_units.split("months since ")[1])  # Extrair a data de referência
        decoded_dates = [reference_date + pd.DateOffset(months=int(t)) for t in raw_time_values]
    else:
        raise ValueError(f"Unidades de tempo não suportadas: {time_units}")

    # Atualizar a variável 'time' no dataset
    combined_data["time"] = xr.Variable(
        dims=combined_data["time"].dims,
        data=decoded_dates,
        attrs=combined_data["time"].attrs
    )

# Converter para DataFrame
df = combined_data.to_dataframe()

# Salvar como CSV
output_path = os.path.join(data_path, "dados_combinados.csv")
df.to_csv(output_path)

print(f"Arquivos combinados e salvos como CSV em: {output_path}")