# CeneoScrapper

## Etap 1
### 1. analiza struktury opinii w serwisie  [Ceneo.pl](https://www.ceneo.pl)
|Składowa|Selektor CSS|Nazwa zmiennej|Typ danych|
|--------|------------|--------------|----------|   
|Opinia|div.js_product_review|opinion|typy danych tu|
|ID opinii|["data-entry-id"]|opinion_id||
|Autor|span.user-posts__author-name|author||
|Rekomendacja|span.user-post__author-name|recommendation||
|Liczba gwiazdek|span.user-post__score-count|stars_count||
|Tresć opinii|div.user-post__text|content||
|Lista wad|div.review-feature__col:has(> div[class*="negative"]) > div.review-feature__item|pros||
|Lista zalet|div.review-feature__col:has(> div[class*="positives"]) > div.review-feature__item|cons||
|Czy potwierdzona zakupem|div.review-pz|purchased||
|Data wystawienia opinii|span.user-post__published > time:nth-child(1)["datetime"]|submit_date||
|Data zakupu produktu|span.user-post__published > time:nth-child(2)["datetime"]|purchase_date||
|Dla ilu osób przydatna|span[id^="votes-yes"]|useful||
|Dla ilu osób nieprzydatna|span[id^="votes-no"]|useless||   

### 2.pobranie składowych pojednyczej opinii
-pobranie kodu strony pojeynczej z opiniami
-wyodrebnienie z kodu strony pojedzynczej opinii
-pobieranie pojednyczych zmiennych na podstawie selektorów