# Dokumentacja projektu TabliceRejestracyjneOCR
 
## I. Charakterystyka oprogramowania
**a. Nazwa skrócona:** TabliceRejestracyjneOCR


**b. Nazwa pełna:** System Rozpoznawania Numerów Tablic Rejestracyjnych Ze Zdjęć i Filmów Z Wykorzystaniem Pythona, OpenCV i OCR
 
**c. Krótki opis ze wskazaniem celów:**
System służy do automatycznego rozpoznawania tekstu w obrazach i filmach przy użyciu technologii OCR (Optical Character Recognition) zaimplementowanej w Pythonie z wykorzystaniem biblioteki OpenCV. Jego głównym celem jest konwersja tekstu z obrazów i filmów na edytowalny format, co pozwala na automatyzację procesów, poprawę dostępności treści oraz analizę tekstu w różnych zastosowaniach.
 
## II. Prawa autorskie 
**a. Autorzy:** Marta Kosmowska, Dominik Malczyński, Adrian Chmielewski


**b. Warunki licencyjne:**
Oprogramowanie jest objęte licencją GNU General Public License v3.0, co pozwala na jego swobodne używanie, modyfikowanie oraz dystrybucję, pod warunkiem, że wszelkie zmiany i pochodne prace również będą objęte tą samą licencją. Licencja ta zapewnia również, że kod źródłowy będzie dostępny dla użytkowników końcowych, umożliwiając im swobodę w badaniu, poprawianiu i dzieleniu się modyfikacjami.
 
## III. Specyfikacja wymagań
 
| Identyfikator | Nazwa                      | Opis                                                                                                     | Priorytet | Kategoria       |
|---------------|----------------------------|----------------------------------------------------------------------------------------------------------|-----------|-----------------|
| 1             | Wczytywanie obrazu         | Użytkownik powinien mieć możliwość wczytania obrazu oraz pliku wideo w następujących formatach: JPEG, PNG, MP4.| 1         | Funkcjonalne    |
| 2             | Przetwarzanie obrazu       | System powinien automatycznie skalować obraz, aby ułatwić odczyt tekstu z tablicy rejestracyjnej i przyspieszyć działanie programu. | 1         | Funkcjonalne    |
| 3             | Wykrywanie tablic rejestracyjnych | System powinien automatycznie wykrywać obecność unikalnych tablic rejestracyjnych na obrazie lub pliku wideo, aby użytkownik nie musiał ręcznie zaznaczać tablic. | 1         | Funkcjonalne    |
| 4             | Segmentacja tablic         | System powinien automatycznie wyodrębniać tablice rejestracyjne z tła obrazu, aby tekst był bardziej czytelny. | 1         | Funkcjonalne    |
| 5             | Odczyt tekstu z tablic     | System powinien umożliwiać odczyt tekstu z wykrytej tablicy rejestracyjnej, aby użytkownik mógł uzyskać tekst w formie cyfrowej oraz wizualnej. | 1         | Funkcjonalne    |
| 6            | Wytrenowanie systemu, Testowanie i Ocena         | System powinien zostać nauczony maszynowo rozpoznawania tablic rejestracyjnych oraz przetestowany, aby użytkownik miał pewność co do jakości wyników. | 1         | Funkcjonalne |
| 7            | Dokumentacja               | Powinna istnieć szczegółowa dokumentacja techniczna zawierająca spis potrzebnych bibliotek oraz przetrenowany model. | 1         | Niefunkcjonalne |
| 8            | Przykładowe obrazy         | Powinny być udostępnione przykładowe obrazy i film do testowania oraz wyniki, aby użytkownik mógł przetestować system przed jego użyciem. | 2         | Niefunkcjonalne |
 
## IV. Architektura systemu/oprogramowania
 
## 1. Architektura rozwoju - stos technologiczny
1.1 Język programowania: Python 3.7
1.2 Środowisko: Pycharm Community - zintegrowane środowisko programistyczne dla języka programowania Python firmy JetBrains.
1.3 Biblioteki/algorytymy:
  - OpenCV (Open Source Computer Vision) - biblioteka do przetwarzania obrazów i wideo, oferująca narzędzia do analizy obrazów, detekcji obiektów i maszynowego uczenia.
  - EasyOCR - biblioteka  do optycznego rozpoznawania znaków (Optical Character Recognition).
  - NumPy -  biblioteka do obliczeń numerycznych. Zapewnia efektywne struktury danych do pracy z wielowymiarowymi tablicami i macierzami oraz funkcje do wykonywania operacji na tych danych.
  - Matplotlib - biblioteka do tworzenia wykresów i wizualizacji danych.
  - Pandas - biblioteka, zaprojektowana do manipulacji i analizy danych, umożliwiająca łatwą pracę z danymi w formie tabelarycznej.
  - SciPy - biblioteka  do zaawansowanych obliczeń numerycznych i analizy danych.
  - Filterpy - biblioteka w języku awierająca implementacje różnych filtrów Bayesowskich oraz algorytmów śledzenia obiektów.
  - Ultralytics.YOLO - biblioteka, korzystająca z algorytmu detekcji obiektów YOLO (You Only Look Once), umożliwiająca szybkie tworzenie systemów, które potrafią identyfikować i klasyfikować obiekty na obrazach i wideo, wykorzystując techniki uczenia maszynowego.
  - Sort - algorytm śledzenia wielu obiektów w czasie rzeczywistym w sekwencjach wideo.
1.4 Platforma wspomagająca: Github - platforma internetowa, która umożliwia programistom przechowywanie, zarządzanie i udostępnianie kodu źródłowego projektów oraz współpracę nad nimi przy użyciu systemu kontroli wersji Git.

## 2. Architektura uruchomieniowa - stos technologiczny
  2.1 PyCharm Community - zintegrowane środowisko programistyczne (IDE) opracowane przez firmę JetBrains, zaprojektowane specjalnie dla programistów pracujących w języku Python. Jest to bezpłatna wersja narzędzia, która oferuje pełen zakres funkcji, w tym edycję kodu, debugowanie, refaktoryzację, zarządzanie projektem, integrację z systemami kontroli wersji oraz obsługę bibliotek Pythona.

 
## V. Testy
 
### Scenariusze testów:
- Test obsługi formatów: Weryfikacja, czy system obsługuje wszystkie wymagane formaty obrazów (JPEG, PNG) oraz filmów (MP4).
- Test wykrywania tablic: Sprawdzenie skuteczności wykrywania tablic rejestracyjnych na obrazach lub filmach.
- Test segmentacji: Weryfikacja poprawności segmentacji tablic rejestracyjnych z tła obrazu.
- Test odczytu tekstu: Ocena dokładności odczytu tekstu z wykrytych tablic rejestracyjnych.
 
### Sprawozdanie z wykonania scenariuszy testów:
Wszystkie testy zostały przeprowadzone pomyślnie. System poprawnie obsługuje wymagane formaty, skutecznie wykrywa tablice rejestracyjne, prawidłowo segmentuje je z tła oraz dokładnie odczytuje tekst.
