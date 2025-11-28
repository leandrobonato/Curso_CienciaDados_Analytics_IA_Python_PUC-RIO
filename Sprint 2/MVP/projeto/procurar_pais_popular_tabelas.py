import requests
import pandas as pd

# Função para buscar dados de países usando a API REST Countries
def fetch_country_data():
    try:
        # URL da API REST Countries com o parâmetro 'fields'
        url = "https://restcountries.com/v3.1/all?fields=name,cca2,cca3,population,region,subregion"
        
        # Fazer a requisição HTTP
        response = requests.get(url)
        response.raise_for_status()  # Verifica se houve erro na requisição
        
        # Extrair os dados JSON
        data = response.json()
        
        # Lista para armazenar os dados dos países
        countries = []
        
        # Iterar sobre os dados e extrair informações relevantes
        for country in data:
            name = country.get("name", {}).get("common", "N/A")  # Nome comum do país
            official_name = country.get("name", {}).get("official", "N/A")  # Nome oficial do país
            alpha2_code = country.get("cca2", "N/A")  # Código ISO Alpha-2
            alpha3_code = country.get("cca3", "N/A")  # Código ISO Alpha-3
            population = country.get("population", "N/A")  # População
            region = country.get("region", "N/A")  # Região
            subregion = country.get("subregion", "N/A")  # Sub-região
            
            # Adicionar os dados à lista
            countries.append({
                "Nome Comum": name,
                "Nome Oficial": official_name,
                "Código ISO Alpha-2": alpha2_code,
                "Código ISO Alpha-3": alpha3_code,
                "População": population,
                "Região": region,
                "Sub-Região": subregion
            })
        
        # Criar um DataFrame com os dados
        df = pd.DataFrame(countries)
        
        # Salvar os dados em um arquivo CSV
        df.to_csv("dados_paises.csv", index=False, encoding="utf-8")
        
        print("Dados salvos com sucesso no arquivo 'dados_paises.csv'")
    
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

# Executar a função
fetch_country_data()