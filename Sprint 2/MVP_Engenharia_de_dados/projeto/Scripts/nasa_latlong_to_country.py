import pandas as pd
import re
import time
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
from typing import Optional, Tuple

# Configuração do geocodificador (respeite os termos de uso do Nominatim)
geolocator = Nominatim(user_agent="co2_etl_mvp_leandro@bonato16.com")

def get_country_from_latlon(lat: float, lon: float, max_retries: int = 3) -> Tuple[Optional[str], Optional[str]]:
    """
    Retorna (country_name, iso_alpha_3) com base em lat/lon.
    Usa cache simples em memória (em produção, usar Redis ou lookup pré-calculado).
    """
    for attempt in range(max_retries):
        try:
            location = geolocator.reverse((lat, lon), language="en", timeout=10)
            if location and location.raw.get("address"):
                address = location.raw["address"]
                country = address.get("country")
                # ISO código via "country_code" (alpha-2) → mapear para alpha-3 via tabela
                cc = address.get("country_code", "").upper()
                iso3 = ISO2_TO_ISO3.get(cc, None)
                return country, iso3
        except (GeocoderTimedOut, GeocoderServiceError):
            time.sleep(1 * (2 ** attempt))  # backoff exponencial
        except Exception as e:
            print(f"Erro inesperado ({lat}, {lon}): {e}")
            break
    return None, None

# Mapeamento ISO Alpha-2 → Alpha-3 (extraído do `catalogo_paises` do seu XLSX)
ISO2_TO_ISO3 = {
    "AF": "AFG", "AX": "ALA", "AL": "ALB", "DZ": "DZA", "AS": "ASM", "AD": "AND", "AO": "AGO",
    "AI": "AIA", "AQ": "ATA", "AG": "ATG", "AR": "ARG", "AM": "ARM", "AW": "ABW", "AU": "AUS",
    "AT": "AUT", "AZ": "AZE", "BS": "BHS", "BH": "BHR", "BD": "BGD", "BB": "BRB", "BY": "BLR",
    "BE": "BEL", "BZ": "BLZ", "BJ": "BEN", "BM": "BMU", "BT": "BTN", "BO": "BOL", "BQ": "BES",
    "BA": "BIH", "BW": "BWA", "BV": "BVT", "BR": "BRA", "IO": "IOT", "BN": "BRN", "BG": "BGR",
    "BF": "BFA", "BI": "BDI", "CV": "CPV", "KH": "KHM", "CM": "CMR", "CA": "CAN", "KY": "CYM",
    "CF": "CAF", "TD": "TCD", "CL": "CHL", "CN": "CHN", "CX": "CXR", "CC": "CCK", "CO": "COL",
    "KM": "COM", "CG": "COG", "CD": "COD", "CK": "COK", "CR": "CRI", "CI": "CIV", "HR": "HRV",
    "CU": "CUB", "CW": "CUW", "CY": "CYP", "CZ": "CZE", "DK": "DNK", "DJ": "DJI", "DM": "DMA",
    "DO": "DOM", "EC": "ECU", "EG": "EGY", "SV": "SLV", "GQ": "GNQ", "ER": "ERI", "EE": "EST",
    "SZ": "SWZ", "ET": "ETH", "FK": "FLK", "FO": "FRO", "FJ": "FJI", "FI": "FIN", "FR": "FRA",
    "GF": "GUF", "PF": "PYF", "TF": "ATF", "GA": "GAB", "GM": "GMB", "GE": "GEO", "DE": "DEU",
    "GH": "GHA", "GI": "GIB", "GR": "GRC", "GL": "GRL", "GD": "GRD", "GP": "GLP", "GU": "GUM",
    "GT": "GTM", "GG": "GGY", "GN": "GIN", "GW": "GNB", "GY": "GUY", "HT": "HTI", "HM": "HMD",
    "VA": "VAT", "HN": "HND", "HK": "HKG", "HU": "HUN", "IS": "ISL", "IN": "IND", "ID": "IDN",
    "IR": "IRN", "IQ": "IRQ", "IE": "IRL", "IM": "IMN", "IL": "ISR", "IT": "ITA", "JM": "JAM",
    "JP": "JPN", "JE": "JEY", "JO": "JOR", "KZ": "KAZ", "KE": "KEN", "KI": "KIR", "KP": "PRK",
    "KR": "KOR", "KW": "KWT", "KG": "KGZ", "LA": "LAO", "LV": "LVA", "LB": "LBN", "LS": "LSO",
    "LR": "LBR", "LY": "LBY", "LI": "LIE", "LT": "LTU", "LU": "LUX", "MO": "MAC", "MG": "MDG",
    "MW": "MWI", "MY": "MYS", "MV": "MDV", "ML": "MLI", "MT": "MLT", "MH": "MHL", "MQ": "MTQ",
    "MR": "MRT", "MU": "MUS", "YT": "MYT", "MX": "MEX", "FM": "FSM", "MD": "MDA", "MC": "MCO",
    "MN": "MNG", "ME": "MNE", "MS": "MSR", "MA": "MAR", "MZ": "MOZ", "MM": "MMR", "NA": "NAM",
    "NR": "NRU", "NP": "NPL", "NL": "NLD", "NC": "NCL", "NZ": "NZL", "NI": "NIC", "NE": "NER",
    "NG": "NGA", "NU": "NIU", "NF": "NFK", "MK": "MKD", "MP": "MNP", "NO": "NOR", "OM": "OMN",
    "PK": "PAK", "PW": "PLW", "PS": "PSE", "PA": "PAN", "PG": "PNG", "PY": "PRY", "PE": "PER",
    "PH": "PHL", "PN": "PCN", "PL": "POL", "PT": "PRT", "PR": "PRI", "QA": "QAT", "RE": "REU",
    "RO": "ROU", "RU": "RUS", "RW": "RWA", "BL": "BLM", "SH": "SHN", "KN": "KNA", "LC": "LCA",
    "MF": "MAF", "PM": "SPM", "VC": "VCT", "WS": "WSM", "SM": "SMR", "ST": "STP", "SA": "SAU",
    "SN": "SEN", "RS": "SRB", "SC": "SYC", "SL": "SLE", "SG": "SGP", "SX": "SXM", "SK": "SVK",
    "SI": "SVN", "SB": "SLB", "SO": "SOM", "ZA": "ZAF", "GS": "SGS", "SS": "SSD", "ES": "ESP",
    "LK": "LKA", "SD": "SDN", "SR": "SUR", "SJ": "SJM", "SE": "SWE", "CH": "CHE", "SY": "SYR",
    "TW": "TWN", "TJ": "TJK", "TZ": "TZA", "TH": "THA", "TL": "TLS", "TG": "TGO", "TK": "TKL",
    "TO": "TON", "TT": "TTO", "TN": "TUN", "TR": "TUR", "TM": "TKM", "TC": "TCA", "TV": "TUV",
    "UG": "UGA", "UA": "UKR", "AE": "ARE", "GB": "GBR", "UM": "UMI", "US": "USA", "UY": "URY",
    "UZ": "UZB", "VU": "VUT", "VE": "VEN", "VN": "VNM", "VG": "VGB", "VI": "VIR", "WF": "WLF",
    "EH": "ESH", "YE": "YEM", "ZM": "ZMB", "ZW": "ZWE", "XK": "XKX"
}

def parse_latlon(latlon_str: str) -> Tuple[Optional[float], Optional[float]]:
    """Extrai lat/lon de string 'lat,lon'"""
    if not isinstance(latlon_str, str):
        return None, None
    match = re.match(r"^([+-]?\d+\.?\d*),\s*([+-]?\d+\.?\d*)$", latlon_str.strip())
    if match:
        try:
            lat, lon = float(match.group(1)), float(match.group(2))
            # Validação básica
            if -90 <= lat <= 90 and -180 <= lon <= 180:
                return lat, lon
        except ValueError:
            pass
    return None, None

# --- Exemplo de uso (em Databricks, substitua por spark.read.csv() etc.) ---
if __name__ == "__main__":
    # 🔁 Substitua esta linha pela leitura real do seu CSV/Parquet/NCF convertido
    # Ex: df = spark.table("workspace.pucrio.nasa_cms_flux_total_bronze").toPandas()
    df = pd.DataFrame({
        "ANO": [2020, 2021, 2022],
        "LATITUDE_LONGITUDE": [
            "-23.5505,-46.6333",  # São Paulo
            "51.5074,-0.1278",    # Londres
            "40.7128,-74.0060",   # Nova York
            "0,0",                # Atlântico
            "999,999"             # Inválido
        ],
        "VALOR": [1.2, 0.9, 1.5, 0.3, 0.0],
        "qtd_area_m2": [1e6, 2e6, 1.5e6, 5e5, 1e4]
    })

    print("🚀 Iniciando geocodificação reversa...")

    results = []
    for idx, row in df.iterrows():
        lat, lon = parse_latlon(row["LATITUDE_LONGITUDE"])
        if lat is None or lon is None:
            # Dados inválidos → atribui 'Unknown' ou ignora
            country, iso3 = "Unknown", None
        else:
            country, iso3 = get_country_from_latlon(lat, lon)
            if country is None:
                country = "Ocean" if (-90 < lat < 90 and -180 < lon < 180) else "Unknown"
        
        # Normaliza nome do país usando seu catálogo (opcional: faça join depois)
        # Ex: "United States" → "United States of America" (para casar com catalogo_paises)

        results.append({
            "PAIS": country,
            "SIGLA_PAIS": iso3,
            "ANO": int(row["ANO"]),
            "VALOR": float(row["VALOR"]),
            "AREA_M2": float(row.get("qtd_area_m2", 0)),
            "LATITUDE": lat,
            "LONGITUDE": lon
        })

    result_df = pd.DataFrame(results)

    # 🔧 Agregação por país/ano (exemplo: média de fluxo)
    # IMPORTANTE: VALOR é g/m²/dia → para total por país: somar(VALOR * AREA_M2 * 365) / 1e6 → MtCO₂
    aggregated = result_df.groupby(["SIGLA_PAIS", "ANO", "PAIS"], dropna=False).agg(
        MEDIA_FLUXO=("VALOR", "mean"),
        TOTAL_AREA_M2=("AREA_M2", "sum"),
        CONTAGEM=("VALOR", "count")
    ).reset_index()

    print("\n✅ Resultado (exemplo):")
    print(aggregated.head(10))

    # 💾 Exportar para CSV ou subir para Delta (ex: spark.createDataFrame(aggregated).write...)
    # aggregated.to_csv("nasa_flux_by_country_year.csv", index=False)