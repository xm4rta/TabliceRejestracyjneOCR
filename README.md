# Dokumentacja Projektu: Rozpoznawanie Tekstu w Obrazach z Wykorzystaniem Pythona i OpenCV
 
## I. Charakterystyka oprogramowania
**Nazwa skrócona:** OCR Python OpenCV  
**Nazwa pełna:** System Rozpoznawania Tekstu w Obrazach z Wykorzystaniem Pythona i OpenCV  
 
**Krótki opis ze wskazaniem celów:**
System służy do automatycznego rozpoznawania tekstu w obrazach przy użyciu technologii OCR (Optical Character Recognition) zaimplementowanej w Pythonie z wykorzystaniem biblioteki OpenCV. Jego głównym celem jest konwersja tekstu z obrazów na edytowalny format, co pozwala na automatyzację procesów, poprawę dostępności treści oraz analizę tekstu w różnych zastosowaniach, takich jak przetwarzanie dokumentów, analiza obrazów medycznych i rozpoznawanie znaków na zdjęciach.
 
## II. Prawa autorskie
**Autorzy:** [Twoje Imię i Nazwisko oraz inne osoby zaangażowane w projekt]  
**Warunki licencyjne:**
Oprogramowanie jest objęte licencją MIT, co pozwala na jego swobodne używanie, modyfikowanie oraz dystrybucję z zachowaniem informacji o autorach.
 
## III. Specyfikacja wymagań
 
| Identyfikator | Nazwa                      | Opis                                                                                                     | Priorytet | Kategoria       |
|---------------|----------------------------|----------------------------------------------------------------------------------------------------------|-----------|-----------------|
| 1             | Wczytywanie obrazu         | System powinien umożliwiać wczytanie obrazu z różnych źródeł takich jak pliki obrazowe, strumienie wideo lub kamery. | 1         | Funkcjonalne    |
| 2             | Obsługa formatów obrazów   | System powinien obsługiwać różne formaty obrazów takie jak JPEG, PNG itp.                                 | 1         | Funkcjonalne    |
| 3             | Przetwarzanie obrazu       | Implementacja algorytmów przetwarzania obrazu za pomocą biblioteki OpenCV w celu poprawy jakości obrazu i ułatwienia odczytu tablicy rejestracyjnej. | 1         | Funkcjonalne    |
| 4             | Wykrywanie tablic rejestracyjnych | System powinien automatycznie wykrywać obecność tablic rejestracyjnych na obrazie.                           | 1         | Funkcjonalne    |
| 5             | Wykrywanie różnych tablic  | System powinien wykrywać tablice rejestracyjne różnych kształtów i rozmiarów.                             | 1         | Funkcjonalne    |
| 6             | Segmentacja tablic         | Implementacja algorytmów segmentacji w celu wyciągnięcia tablicy rejestracyjnej z tła obrazu.              | 1         | Funkcjonalne    |
| 7             | Odczyt tekstu z tablic     | System powinien umożliwiać odczyt tekstu z zidentyfikowanej tablicy rejestracyjnej.                        | 1         | Funkcjonalne    |
| 8             | Rozpoznawanie znaków       | Zastosowanie bibliotek do rozpoznawania znaków (OCR) takich jak Tesseract w celu odczytu tekstu.           | 1         | Funkcjonalne    |
| 10            | Testowanie i ocena         | Przeprowadzenie testów w celu oceny skuteczności odczytywania tablic rejestracyjnych.                      | 1         | Niefunkcjonalne |
| 11            | Dostosowanie parametrów    | Możliwość dostosowywania parametrów algorytmów w celu poprawy wyników.                                     | 2         | Niefunkcjonalne |
| 12            | Dokumentacja               | Stworzenie szczegółowej dokumentacji technicznej zawierającej instrukcje instalacji, konfiguracji oraz użytkowania systemu. | 1         | Niefunkcjonalne |
| 13            | Przykładowe obrazy         | Udostępnienie przykładowych obrazów do testowania oraz wyników.                                           | 2         | Niefunkcjonalne |
 
## IV. Architektura systemu/oprogramowania
 
### Architektura rozwoju:
- **Stos technologiczny:** Python, OpenCV, EasyOCR, YOLO (You Only Look Once)
- **Narzędzia wspomagające:** Git (do wersjonowania kodu), PyCharm (do edycji kodu)
 
### Architektura uruchomieniowa:
- **Stos technologiczny:** Python, OpenCV, EasyOCR, YOLO
- **Środowisko uruchomieniowe:** System operacyjny z zainstalowanym Pythonem i wymaganymi bibliotekami (OpenCV, EasyOCR, etc.)
 
## V. Testy
 
### Scenariusze testów:
- Test wczytywania obrazów: Sprawdzenie, czy system prawidłowo wczytuje obrazy z różnych źródeł (pliki, kamery, strumienie wideo).
- Test obsługi formatów: Weryfikacja, czy system obsługuje wszystkie wymagane formaty obrazów (JPEG, PNG).
- Test przetwarzania obrazu: Ocena jakości przetwarzania obrazu przy użyciu algorytmów OpenCV.
- Test wykrywania tablic: Sprawdzenie skuteczności wykrywania tablic rejestracyjnych na obrazach.
- Test segmentacji: Weryfikacja poprawności segmentacji tablic rejestracyjnych z tła obrazu.
- Test odczytu tekstu: Ocena dokładności odczytu tekstu z wykrytych tablic rejestracyjnych.
 
### Sprawozdanie z wykonania scenariuszy testów:
Testy zostały przeprowadzone na zestawie próbek obrazów zawierających tablice rejestracyjne z różnych krajów. Wyniki testów wykazały, że system prawidłowo wczytuje obrazy, obsługuje różne formaty, skutecznie przetwarza obrazy, wykrywa i segmentuje tablice rejestracyjne oraz odczytuje tekst z wysoką dokładnością. Szczegółowe wyniki testów są dostępne w załączonym sprawozdaniu.
 
