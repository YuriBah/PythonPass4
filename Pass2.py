from requests import get, utils

response = utils.get_unicode_from_response(get("http://www.cbr.ru/scripts/XML_daily.asp"))


def currency_rates(code):
    cont = response.split("<Valute ID=")
    for i in cont:
        if code.upper() in i:
            return float(i.replace("/", "").split("<Value>")[-2].replace(',', '.'))

if __name__ == "__main__":
    print(currency_rates("USD"))
    print(currency_rates("EUR"))

