# Dokumentacja Projektu: Rozpoznawanie Tekstu w Obrazach z Wykorzystaniem Pythona i OpenCV
 
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
| 1             | Wczytywanie obrazu         | Użytkownik powinien mieć możliwość wczytania obrazu z różnych źródeł takich jak pliki obrazowe, strumienie wideo lub kamery. | 1         | Funkcjonalne    |
| 2             | Obsługa formatów obrazów   | System powinien obsługiwać różne popularne formaty obrazów takie jak JPEG, PNG itp., aby użytkownik mógł korzystać z różnych źródeł obrazów. | 1         | Funkcjonalne    |
| 3             | Przetwarzanie obrazu       | System powinien automatycznie poprawiać jakość obrazu, aby ułatwić odczyt tekstu z tablicy rejestracyjnej. | 1         | Funkcjonalne    |
| 4             | Wykrywanie tablic rejestracyjnych | System powinien automatycznie wykrywać obecność tablic rejestracyjnych na obrazie, aby użytkownik nie musiał ręcznie zaznaczać tablic. | 1         | Funkcjonalne    |
| 5             | Wykrywanie różnych tablic  | System powinien wykrywać tablice rejestracyjne różnych kształtów i rozmiarów, aby użytkownik mógł rozpoznać tablice z różnych krajów. | 1         | Funkcjonalne    |
| 6             | Segmentacja tablic         | System powinien automatycznie wyodrębniać tablice rejestracyjne z tła obrazu, aby tekst był bardziej czytelny. | 1         | Funkcjonalne    |
| 7             | Odczyt tekstu z tablic     | System powinien umożliwiać odczyt tekstu z wykrytej tablicy rejestracyjnej, aby użytkownik mógł uzyskać tekst w formie cyfrowej. | 1         | Funkcjonalne    |
| 8             | Rozpoznawanie znaków       | System powinien wykorzystywać technologie OCR do rozpoznawania znaków na tablicy rejestracyjnej, aby użytkownik otrzymał dokładne wyniki. | 1         | Funkcjonalne    |
| 10            | Testowanie i ocena         | System powinien być przetestowany pod kątem skuteczności rozpoznawania tablic rejestracyjnych, aby użytkownik miał pewność co do jakości wyników. | 1         | Niefunkcjonalne |
| 11            | Dostosowanie parametrów    | System powinien umożliwiać dostosowanie parametrów algorytmów, aby użytkownik mógł poprawić wyniki w specyficznych warunkach. | 2         | Niefunkcjonalne |
| 12            | Dokumentacja               | Powinna istnieć szczegółowa dokumentacja techniczna zawierająca instrukcje instalacji, konfiguracji oraz użytkowania systemu, aby użytkownik mógł łatwo korzystać z systemu. | 1         | Niefunkcjonalne |
| 13            | Przykładowe obrazy         | Powinny być udostępnione przykładowe obrazy do testowania oraz wyniki, aby użytkownik mógł przetestować system przed jego użyciem. | 2         | Niefunkcjonalne |
 
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
 
