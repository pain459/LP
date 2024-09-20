import requests
import pandas as pd

# Function to fetch exchange rates
def get_exchange_rates(api_key):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/INR"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        rates = data['conversion_rates']
        return rates
    else:
        print("Failed to retrieve data.")
        return None

# Mapping of currency codes to country names
currency_country_mapping = {
    "AED": "United Arab Emirates",
    "AFN": "Afghanistan",
    "ALL": "Albania",
    "AMD": "Armenia",
    "ANG": "Netherlands Antillean Guilder",
    "AOA": "Angola",
    "ARS": "Argentina",
    "AUD": "Australia",
    "AWG": "Aruba",
    "AZN": "Azerbaijan",
    "BAM": "Bosnia-Herzegovina",
    "BBD": "Barbados",
    "BDT": "Bangladesh",
    "BGN": "Bulgaria",
    "BHD": "Bahrain",
    "BIF": "Burundi",
    "BMD": "Bermuda",
    "BND": "Brunei",
    "BOB": "Bolivia",
    "BRL": "Brazil",
    "BSD": "Bahamas",
    "BTN": "Bhutan",
    "BWP": "Botswana",
    "BYN": "Belarus",
    "BZD": "Belize",
    "CAD": "Canada",
    "CDF": "Democratic Republic of Congo",
    "CHF": "Switzerland",
    "CLP": "Chile",
    "CNY": "China",
    "COP": "Colombia",
    "CRC": "Costa Rica",
    "CUP": "Cuba",
    "CVE": "Cape Verde",
    "CZK": "Czech Republic",
    "DJF": "Djibouti",
    "DKK": "Denmark",
    "DOP": "Dominican Republic",
    "DZD": "Algeria",
    "EGP": "Egypt",
    "ERN": "Eritrea",
    "ETB": "Ethiopia",
    "EUR": "European Union",
    "FJD": "Fiji",
    "FKP": "Falkland Islands",
    "FOK": "Faroe Islands",
    "GBP": "United Kingdom",
    "GEL": "Georgia",
    "GHS": "Ghana",
    "GIP": "Gibraltar",
    "GMD": "Gambia",
    "GNF": "Guinea",
    "GTQ": "Guatemala",
    "GYD": "Guyana",
    "HKD": "Hong Kong",
    "HNL": "Honduras",
    "HRK": "Croatia",
    "HTG": "Haiti",
    "HUF": "Hungary",
    "IDR": "Indonesia",
    "ILS": "Israel",
    "INR": "India",
    "IQD": "Iraq",
    "IRR": "Iran",
    "ISK": "Iceland",
    "JMD": "Jamaica",
    "JOD": "Jordan",
    "JPY": "Japan",
    "KES": "Kenya",
    "KGS": "Kyrgyzstan",
    "KHR": "Cambodia",
    "KMF": "Comoros",
    "KPW": "North Korea",
    "KRW": "South Korea",
    "KWD": "Kuwait",
    "KYD": "Cayman Islands",
    "KZT": "Kazakhstan",
    "LAK": "Laos",
    "LBP": "Lebanon",
    "LKR": "Sri Lanka",
    "LRD": "Liberia",
    "LSL": "Lesotho",
    "LYD": "Libya",
    "MAD": "Morocco",
    "MDL": "Moldova",
    "MGA": "Madagascar",
    "MKD": "North Macedonia",
    "MMK": "Myanmar",
    "MNT": "Mongolia",
    "MOP": "Macau",
    "MRU": "Mauritania",
    "MUR": "Mauritius",
    "MVR": "Maldives",
    "MWK": "Malawi",
    "MXN": "Mexico",
    "MYR": "Malaysia",
    "MZN": "Mozambique",
    "NAD": "Namibia",
    "NGN": "Nigeria",
    "NIO": "Nicaragua",
    "NOK": "Norway",
    "NPR": "Nepal",
    "NZD": "New Zealand",
    "OMR": "Oman",
    "PAB": "Panama",
    "PEN": "Peru",
    "PGK": "Papua New Guinea",
    "PHP": "Philippines",
    "PKR": "Pakistan",
    "PLN": "Poland",
    "PYG": "Paraguay",
    "QAR": "Qatar",
    "RON": "Romania",
    "RSD": "Serbia",
    "RUB": "Russia",
    "RWF": "Rwanda",
    "SAR": "Saudi Arabia",
    "SCR": "Seychelles",
    "SDG": "Sudan",
    "SEK": "Sweden",
    "SGD": "Singapore",
    "SHP": "Saint Helena",
    "SLL": "Sierra Leone",
    "SOS": "Somalia",
    "SRD": "Suriname",
    "SSP": "South Sudan",
    "STN": "Sao Tome and Principe",
    "SYP": "Syria",
    "SZL": "Eswatini",
    "THB": "Thailand",
    "TJS": "Tajikistan",
    "TMT": "Turkmenistan",
    "TND": "Tunisia",
    "TOP": "Tonga",
    "TRY": "Turkey",
    "TTD": "Trinidad and Tobago",
    "TVD": "Tuvalu",
    "TZS": "Tanzania",
    "UAH": "Ukraine",
    "UGX": "Uganda",
    "USD": "United States",
    "UYU": "Uruguay",
    "UZS": "Uzbekistan",
    "VES": "Venezuela",
    "VND": "Vietnam",
    "VUV": "Vanuatu",
    "WST": "Samoa",
    "XAF": "Central African CFA Franc",
    "XCD": "East Caribbean Dollar",
    "XOF": "West African CFA Franc",
    "XPF": "CFP Franc",
    "YER": "Yemen",
    "ZAR": "South Africa",
    "ZMW": "Zambia",
    "ZWL": "Zimbabwe"
}

# Function to organize and display exchange rates
def display_exchange_rates(rates):
    country_currency_data = {
        "Country": [], 
        "Currency": [], 
        "Exchange Rate (INR)": []
    }
    
    for currency, rate in rates.items():
        country = currency_country_mapping.get(currency, "Unknown")
        country_currency_data["Country"].append(country)
        country_currency_data["Currency"].append(currency)
        country_currency_data["Exchange Rate (INR)"].append(rate)
    
    # Convert to DataFrame for easy viewing
    df = pd.DataFrame(country_currency_data)
    return df


# Function to save the exchange rates to a text file
def save_to_text_file(df, filename="exchange_rates.txt"):
    with open(filename, 'w') as f:
        f.write(df.to_string(index=False))
    print(f"Data saved to {filename}")


# Main execution
if __name__ == "__main__":
    api_key = "<your-key-here>"  # Replace with your API key
    rates = get_exchange_rates(api_key)
    
    if rates:
        exchange_rate_df = display_exchange_rates(rates)
        print(exchange_rate_df)
        
        # Save the output to a text file
        save_to_text_file(exchange_rate_df)
