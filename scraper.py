import bs4, requests

cookies = {
    'cid': 'CigRn2W38LKCRgAbdOK3Ag==',
    '_pxvid': 'a16f41a1-bed5-11ee-828d-374afc9db3eb',
    'featureFlagOverride': '%7B%7D',
    'featureFlagOverrideCrossSite': '%7B%7D',
    'cb_analytics_consent': 'denied',
    'OptanonAlertBoxClosed': '2024-01-29T18:38:56.111Z',
    'xsrf_token': 'gck8BA/Mty7MH0z5G5yjbfuWdqnKnKteP8VD6Ln6OS4',
    '__cflb': '0H28vxzrpPtLNGTtMM6UPrK8jvxkeai9b7dZ5VJBgG4',
    'pxcts': 'd14c3286-c278-11ee-b434-a097f7f2f542',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Sat+Feb+03+2024+11%3A39%3A01+GMT%2B0100+(Ora+standard+dell%E2%80%99Europa+centrale)&version=202304.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=bb88da48-49e1-429f-a17d-7ebf6d5f0d98&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0&geolocation=IT%3B62&AwaitingReconsent=false',
    '_pxhd': 'ODRxouXg3jis/rg13KF7ilrNwpIRKIW6J0p42zcqXKc0yWrhRkeBP7eczq9VA/cGqyoArXftPfe0szfVhz/oOg',
    'authcookie': 'eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiI4MDI2MGU3My04N2U3LTQxNzItYmE2OS0zNTk2MGYzZTA5YTEiLCJpc3MiOiJ1c2Vyc2VydmljZV82OTYwMTUxN183MTciLCJzdWIiOiIwNmZmMmRhNy00ODU3LTRjOGMtOTBjOS1hY2FkNWNlNDM1Y2UiLCJleHAiOjE3MDY5NTcwOTgsImlhdCI6MTcwNjk1Njc5OCwicHJpdmF0ZSI6IlhBbVRTc2V5enVsWjVuRE5BTnlJOTBoQUxkVVRpSUJwSzBlTUFkTWNrdlhsZFVIN29GWDZPY3dDRi8rR0cvVTVoTVlHQ09uT0d2RzI1dlhZYXViMmExVmFXb3ExVW1oS0J0OHFrYWdUckcvc0VkOE8wSzB1bWN0aGE1bU1aeUtxeXJmcEk0bXpPYTE2bm9IUkEzRHdtNUJPRVZ1TU1pcWxWMGt0TEh1NzBzVXBvdTNhMlRCMXZWcytTbFJmUExmV1BXdW5pQndteHVLdGpGTUxva3EwRnZCbDd4eTZNZEYwcit4NThQVkFFaTNNa0ptbjkzQ3JuTzY0SHhDcWlPeWhycERqVmRyNm5UbCt2dVpEYVduZVh2ZmdHVVkwMnZBUkhGam5JZVpxM3d6bmF4TzhOQUllRFZKejhLQS9YQVZHVzM4R2FhaWlIVU5oYUc1TzFmWWh6T3BwZ1J5WTZ5YTkzMjloMG1GNXBHQjZyNkJOWU9GY1VEZ1YrRmRsMGdUMTF5dHpWeHhPcCtCRGdTUjlpQXpyQW95RExDem9kNVRjNGFvM2kxU2tDNXE1VE5UR09abVBmUS9BWXVnVExaQVZIV0crRDNNUnhHR2pmTFdwOFgwYTdDMTNUNmZZODJRTlJFNUozS2k4ZG9pN3RzMlJham5ldUFUZTJjWmNBWG9mOU9DUUZUV0lBcE4xRUpSeVhPSjNsdnV6a1ZaY3Y3a1Y3Ukl1OE9nRWl5Vk1KQlJRLzJuUHlOUm9iaHR0WHJ5YjNvbktsS0lTNmQwUFcyWHpHbnkyUjQvbXpNY2tnY3g0RVlhTkE4LzhiZkpFVmhDV005TmtTbitaanhQK2xOZ3dsU3VWY1NaT2o1RmcvZEFoVGlHa3FMNWVnNExiYUhLLzBlNGNjNGxNZ0dDeUhHMndoTG1YZCt3YUJ5aTVNV0poWW9YOW1vcHpMbVBnbjFva012bmdva1QwNkxlTXh5NjQxMjBxSk1GaW9DYUM3VTdxNWpRWi84SlEvOTlaYzdoNlhCUjdDWGZCeC9zUFhLT2pMOTNEbkNvTnlwZUkzcFliN0s3a0lwaGJ4aGVnVXlKU29tM25zSGRmVGhRcFJlVk5hMkFJd1BIRndnenZsSVVGcXAzN3FoM1htcEVsYW42NDROdGgrTitjRUxRU3pPU1lJZUlldGpLWHNjRFJaaGtrLzdyeitFRnhzNWQ4eldKWmhvZ0tzL01BU3VMOVUxejIwVUE0aE1pMHBNcGdyMUFXSXk5VHo4OHlxZFpXc1NnYlFncHRmZjdCTEVJUVZmUlpUVjY5ZTBJVE1SWjI1aUxqT0FNOXIxMWl2NXV4akxGYzRQOVJUbVY5S1hDZ0szc3FIZTdha05ndFdwRkNpcTRzdXhMVDdJSlI3Um9DdGI5UUkwVlZzb0tCT2VVcVppVDdPZjNSY3dYb3RoTTIzYmd3amt2eG92clhLd2hQMmFMNENsTHk0VGg3VEhNNGlObE43V3ZvMDBZTzU2Q2NpTFN6VU02TW1PSWZ3bWhPQTdZMmtWdzZ5b01FNHpWT1dPQjZtaDlZRVNSNVFRSExaRHVLTUtrUlpQeXI4MW5yUzlFMXo3MmtydVlVMVp5SDM2V0dNTUhLUDJjb0VIb3l3L0wvVVREUEpsT0NHcXB1WVQ2blRsRzViNFN2ZThVPSIsInB1YmxpYyI6eyJzZXNzaW9uX2hhc2giOiItMTc2NTU1MDA2In19.DzGfqBVaJrKLfWl2ph8F0nLP67-5YlVfB4GJ0bOtqv5aVpDs-oXGbTefNW9GU8rtYGMbLu0YgxocQBisBd3wfw',
    '_px3': '1a62c8f6260242780b2b5ba242011f51643acedcf2fe4b8d4d66fde9af99f907:hWmNPvHK9LUfD6rneqLdbwE2NxyIOK1OdUirqB1Sog0SwzuVBh8Jj9244a5WTQMgR2JtHQnfXSaYK+cEslNRRA==:1000:I3F3wwGD7lfcWQXygaHDcdI0n1V+ZH7doYhTp4bddtYFieWxVGF/wKFNJQRarAwAUDbwfGSI55pMvZUrIpj+V5XXJMgKO0id1w58h7bkJM7QYXUwsaGW6TJqcfL7j4DC3dEXjQKK8raFC6cd6PSek/w4nAz05ZW97MzSNV9KSAX0xBc4iQrz52IErQoi+8LoSFIjHGnD9zhL+6LXUsgMLMpmxJoz75RDkcrCBN1rTTw=',
}

headers = {
    'authority': 'www.crunchbase.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7,ru-RU;q=0.6,ru;q=0.5,el-GR;q=0.4,el;q=0.3',
    'cache-control': 'max-age=0',
    # 'cookie': 'cid=CigRn2W38LKCRgAbdOK3Ag==; _pxvid=a16f41a1-bed5-11ee-828d-374afc9db3eb; featureFlagOverride=%7B%7D; featureFlagOverrideCrossSite=%7B%7D; cb_analytics_consent=denied; OptanonAlertBoxClosed=2024-01-29T18:38:56.111Z; xsrf_token=gck8BA/Mty7MH0z5G5yjbfuWdqnKnKteP8VD6Ln6OS4; __cflb=0H28vxzrpPtLNGTtMM6UPrK8jvxkeai9b7dZ5VJBgG4; pxcts=d14c3286-c278-11ee-b434-a097f7f2f542; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Feb+03+2024+11%3A39%3A01+GMT%2B0100+(Ora+standard+dell%E2%80%99Europa+centrale)&version=202304.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=bb88da48-49e1-429f-a17d-7ebf6d5f0d98&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0&geolocation=IT%3B62&AwaitingReconsent=false; _pxhd=ODRxouXg3jis/rg13KF7ilrNwpIRKIW6J0p42zcqXKc0yWrhRkeBP7eczq9VA/cGqyoArXftPfe0szfVhz/oOg; authcookie=eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiI4MDI2MGU3My04N2U3LTQxNzItYmE2OS0zNTk2MGYzZTA5YTEiLCJpc3MiOiJ1c2Vyc2VydmljZV82OTYwMTUxN183MTciLCJzdWIiOiIwNmZmMmRhNy00ODU3LTRjOGMtOTBjOS1hY2FkNWNlNDM1Y2UiLCJleHAiOjE3MDY5NTcwOTgsImlhdCI6MTcwNjk1Njc5OCwicHJpdmF0ZSI6IlhBbVRTc2V5enVsWjVuRE5BTnlJOTBoQUxkVVRpSUJwSzBlTUFkTWNrdlhsZFVIN29GWDZPY3dDRi8rR0cvVTVoTVlHQ09uT0d2RzI1dlhZYXViMmExVmFXb3ExVW1oS0J0OHFrYWdUckcvc0VkOE8wSzB1bWN0aGE1bU1aeUtxeXJmcEk0bXpPYTE2bm9IUkEzRHdtNUJPRVZ1TU1pcWxWMGt0TEh1NzBzVXBvdTNhMlRCMXZWcytTbFJmUExmV1BXdW5pQndteHVLdGpGTUxva3EwRnZCbDd4eTZNZEYwcit4NThQVkFFaTNNa0ptbjkzQ3JuTzY0SHhDcWlPeWhycERqVmRyNm5UbCt2dVpEYVduZVh2ZmdHVVkwMnZBUkhGam5JZVpxM3d6bmF4TzhOQUllRFZKejhLQS9YQVZHVzM4R2FhaWlIVU5oYUc1TzFmWWh6T3BwZ1J5WTZ5YTkzMjloMG1GNXBHQjZyNkJOWU9GY1VEZ1YrRmRsMGdUMTF5dHpWeHhPcCtCRGdTUjlpQXpyQW95RExDem9kNVRjNGFvM2kxU2tDNXE1VE5UR09abVBmUS9BWXVnVExaQVZIV0crRDNNUnhHR2pmTFdwOFgwYTdDMTNUNmZZODJRTlJFNUozS2k4ZG9pN3RzMlJham5ldUFUZTJjWmNBWG9mOU9DUUZUV0lBcE4xRUpSeVhPSjNsdnV6a1ZaY3Y3a1Y3Ukl1OE9nRWl5Vk1KQlJRLzJuUHlOUm9iaHR0WHJ5YjNvbktsS0lTNmQwUFcyWHpHbnkyUjQvbXpNY2tnY3g0RVlhTkE4LzhiZkpFVmhDV005TmtTbitaanhQK2xOZ3dsU3VWY1NaT2o1RmcvZEFoVGlHa3FMNWVnNExiYUhLLzBlNGNjNGxNZ0dDeUhHMndoTG1YZCt3YUJ5aTVNV0poWW9YOW1vcHpMbVBnbjFva012bmdva1QwNkxlTXh5NjQxMjBxSk1GaW9DYUM3VTdxNWpRWi84SlEvOTlaYzdoNlhCUjdDWGZCeC9zUFhLT2pMOTNEbkNvTnlwZUkzcFliN0s3a0lwaGJ4aGVnVXlKU29tM25zSGRmVGhRcFJlVk5hMkFJd1BIRndnenZsSVVGcXAzN3FoM1htcEVsYW42NDROdGgrTitjRUxRU3pPU1lJZUlldGpLWHNjRFJaaGtrLzdyeitFRnhzNWQ4eldKWmhvZ0tzL01BU3VMOVUxejIwVUE0aE1pMHBNcGdyMUFXSXk5VHo4OHlxZFpXc1NnYlFncHRmZjdCTEVJUVZmUlpUVjY5ZTBJVE1SWjI1aUxqT0FNOXIxMWl2NXV4akxGYzRQOVJUbVY5S1hDZ0szc3FIZTdha05ndFdwRkNpcTRzdXhMVDdJSlI3Um9DdGI5UUkwVlZzb0tCT2VVcVppVDdPZjNSY3dYb3RoTTIzYmd3amt2eG92clhLd2hQMmFMNENsTHk0VGg3VEhNNGlObE43V3ZvMDBZTzU2Q2NpTFN6VU02TW1PSWZ3bWhPQTdZMmtWdzZ5b01FNHpWT1dPQjZtaDlZRVNSNVFRSExaRHVLTUtrUlpQeXI4MW5yUzlFMXo3MmtydVlVMVp5SDM2V0dNTUhLUDJjb0VIb3l3L0wvVVREUEpsT0NHcXB1WVQ2blRsRzViNFN2ZThVPSIsInB1YmxpYyI6eyJzZXNzaW9uX2hhc2giOiItMTc2NTU1MDA2In19.DzGfqBVaJrKLfWl2ph8F0nLP67-5YlVfB4GJ0bOtqv5aVpDs-oXGbTefNW9GU8rtYGMbLu0YgxocQBisBd3wfw; _px3=1a62c8f6260242780b2b5ba242011f51643acedcf2fe4b8d4d66fde9af99f907:hWmNPvHK9LUfD6rneqLdbwE2NxyIOK1OdUirqB1Sog0SwzuVBh8Jj9244a5WTQMgR2JtHQnfXSaYK+cEslNRRA==:1000:I3F3wwGD7lfcWQXygaHDcdI0n1V+ZH7doYhTp4bddtYFieWxVGF/wKFNJQRarAwAUDbwfGSI55pMvZUrIpj+V5XXJMgKO0id1w58h7bkJM7QYXUwsaGW6TJqcfL7j4DC3dEXjQKK8raFC6cd6PSek/w4nAz05ZW97MzSNV9KSAX0xBc4iQrz52IErQoi+8LoSFIjHGnD9zhL+6LXUsgMLMpmxJoz75RDkcrCBN1rTTw=',
    'dnt': '1',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

response = requests.get(
    'https://www.crunchbase.com/discover/organization.companies/2b963fc2eb57534259ed26145d83fe94',
    cookies=cookies,
    headers=headers,
)
response.raise_for_status()

soup = bs4.BeautifulSoup(response.text, "html.parser")

div_grid = soup.find("div", class_="grid-id-organization-companies")

rows = div_grid.find_all("grid-row", class_="ng-star-inserted")

headers = [i.text for i in div_grid.find_all("grid-column-header")]

df_rows=[]
for row in rows:
    cells = row.find_all("grid-cell")
    cells = [i.text for i in cells]
    df_rows.append(cells)

import pandas as pd
df = pd.DataFrame(df_rows, columns=headers)

with open("crunch_scrape3.tsv", "w") as f:
    df.to_csv(f, sep="\t", index=False)

print(df)

        