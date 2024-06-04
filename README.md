# Dokumentacja projektu TabliceRejestracyjneOCR
 
## I. Charakterystyka oprogramowania
**Nazwa skrócona:** TabliceRejestracyjneOCR


**Nazwa pełna:** System Rozpoznawania Numerów Tablic Rejestracyjnych Ze Zdjęć i Filmów Z Wykorzystaniem Pythona, OpenCV i OCR
 
**Krótki opis ze wskazaniem celów:**
System służy do automatycznego rozpoznawania tekstu w obrazach i filmach przy użyciu technologii OCR (Optical Character Recognition) zaimplementowanej w Pythonie z wykorzystaniem biblioteki OpenCV. Jego głównym celem jest konwersja tekstu z obrazów i filmów na edytowalny format, co pozwala na automatyzację procesów, poprawę dostępności treści oraz analizę tekstu w różnych zastosowaniach.
 
## II. Prawa autorskie 
**Autorzy:** Marta Kosmowska, Dominik Malczyński, Adrian Chmielewski


**Warunki licencyjne:**
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
 
### IV. Architektura systemu/oprogramowania
 
#### a. Architektura rozwoju - stos technologiczny
- Język programowania: Python 3.7
- Biblioteki:
  - OpenCV (Open Source Computer Vision)
  - EasyOCR
  - YOLO (You Only Look Once)
  - OS (Biblioteka do interakcji z systemem operacyjnym. Umożliwia wykonywanie operacji na plikach, katalogach itp.)
  - NumPy (Popularna biblioteka do obliczeń numerycznych w języku Python. Zapewnia efektywne struktury danych do pracy z wielowymiarowymi tablicami i macierzami oraz funkcje do wykonywania operacji na tych danych.)
  - CSV (Biblioteka do manipulacji plikami CSV (Comma Separated Values). Umożliwia czytanie i zapisywanie danych w formacie CSV.)
  - Ultralytics.YOLO (Implementacja algorytmu YOLO (You Only Look Once) do detekcji obiektów w obrazach. YOLO jest popularnym algorytmem do detekcji obiektów w czasie rzeczywistym.)
  - Sort.Sort (Implementacja algorytmu SORT (Simple Online and Realtime Tracking) do śledzenia obiektów w sekwencji obrazów.)
  - Matplotlib.pyplot (Biblioteka do tworzenia wykresów i wizualizacji danych. Umożliwia generowanie różnych rodzajów wykresów, histogramów itp.)
  - AST (Biblioteka do analizy i manipulacji kodem źródłowym Pythona. Może być używana do analizy składniowej i semantycznej kodu Pythona.)
  - Pandas (Biblioteka do manipulacji danymi, szczególnie w przypadku danych tabelarycznych. Umożliwia łatwe wczytywanie, przetwarzanie i analizę danych.)
  - SciPy.interpolate.interp1d (Biblioteka SciPy jest zbiorem narzędzi i algorytmów do obliczeń naukowych w Pythonie. Ta konkretna funkcja służy do interpolacji danych.)
  - Filterpy (Biblioteka Pythona służąca do implementacji różnych filtrów Bayesowskich, takich jak filtr Kalmana, filtr cząsteczkowy i inne, wykorzystywanych do estymacji stanu w systemach dynamicznych.)
- Narzędzia wspomagające:
  - Git (do wersjonowania kodu)
  - PyCharm Community (do edycji kodu)
 
## V. Testy
 
### Scenariusze testów:
- Test obsługi formatów: Weryfikacja, czy system obsługuje wszystkie wymagane formaty obrazów (JPEG, PNG) oraz filmów (MP4).
- Test wykrywania tablic: Sprawdzenie skuteczności wykrywania tablic rejestracyjnych na obrazach lub filmach.
- Test segmentacji: Weryfikacja poprawności segmentacji tablic rejestracyjnych z tła obrazu.
- Test odczytu tekstu: Ocena dokładności odczytu tekstu z wykrytych tablic rejestracyjnych.
 
### Sprawozdanie z wykonania scenariuszy testów:
Wszystkie testy zostały przeprowadzone pomyślnie. System poprawnie obsługuje wymagane formaty, skutecznie wykrywa tablice rejestracyjne, prawidłowo segmentuje je z tła oraz dokładnie odczytuje tekst.
