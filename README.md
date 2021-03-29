# CeneoScrapper

## Etap 1 Ekstrakcja pojedynczej opinii o produkcie, którego kod będzie wpisany w kodzie programu
### 1. analiza struktury opinii w serwisie  [Ceneo.pl](https://www.ceneo.pl)
|Składowa|Selektor CSS|Nazwa zmiennej|Typ danych|
|--------|------------|--------------|----------|   
|Opinia|div.js_product_review|opinion|obiekt bs4.element.Tag|
|ID opinii|["data-entry-id"]|opinion_id|str|
|Autor|span.user-post__author-name|author|str|
|Rekomendacja|span.user-post__author-recomendation > em|recommendation|bool|
|Liczba gwiazdek|span.user-post__score-count|stars_count|float|
|Tresć opinii|div.user-post__text|content|str|
|Lista zalet|div.review-feature__col:has(> div[class*="positives"]) > div.review-feature__item|pros|list|
|Lista wad|div.review-feature__col:has(> div[class*="negatives"]) > div.review-feature__item|cons|list|
|Czy potwierdzona zakupem|div.review-pz|purchased|bool|
|Data wystawienia opinii|span.user-post__published > time:nth-child(1)["datetime"]|submit_date|str|
|Data zakupu produktu|span.user-post__published > time:nth-child(2)["datetime"]|purchase_date|str|
|Dla ilu osób przydatna|span[id^="votes-yes"]|useful|int|
|Dla ilu osób nieprzydatna|span[id^="votes-no"]|useless|int|   

### 2.pobranie składowych pojednyczej opinii
-pobranie kodu strony pojeynczej z opiniami
-wyodrebnienie z kodu strony pojedzynczej opinii
-pobieranie pojednyczych zmiennych na podstawie selektorów
-obsługa błędów
-dobranie typów danych do wartości zmiennych

## Etap 2 Ekstrakcja wszystkich opinii o produkcie z pojedynczej strony
