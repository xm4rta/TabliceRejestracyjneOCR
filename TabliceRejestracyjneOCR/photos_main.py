import os
import cv2
import numpy as np
import easyocr
import csv
import util

# Definiowanie ścieżek do plików modelu
model_cfg_path = os.path.join('.', 'models', 'cfg', 'darknet-yolov3.cfg')
model_weights_path = os.path.join('.', 'models', 'weights', 'model.weights')
class_names_path = os.path.join('.', 'models', 'class.names')

# Definiowanie ścieżek do katalogu wejściowego i wyjściowego oraz pliku CSV
input_dir = './photos/input_images'
output_csv = './photos/csv/results.csv'
output_dir = './photos/output_images'


# Otwarcie pliku CSV w trybie zapisu
with open(output_csv, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    # Zapisanie nagłówka
    writer.writerow(['Nazwa obrazu', 'Tekst tablicy rejestracyjnej', 'Ocena tablicy rejestracyjnej'])

    # Iteracja po wszystkich obrazach w katalogu wejściowym
    for img_name in os.listdir(input_dir):
        img_path = os.path.join(input_dir, img_name)

        # Wczytanie nazw klas z pliku
        with open(class_names_path, 'r') as f:
            class_names = [j.strip() for j in f.readlines() if len(j.strip()) > 0]

        # Wczytanie modelu YOLO
        net = cv2.dnn.readNetFromDarknet(model_cfg_path, model_weights_path)

        # Wczytanie obrazu
        img = cv2.imread(img_path)
        H, W, _ = img.shape

        # Konwersja obrazu na format wymagany przez model YOLO
        blob = cv2.dnn.blobFromImage(img, 1 / 255, (416, 416), (0, 0, 0), True)

        # Uzyskanie wykryć obiektów ( tablic rejestracyjnych )
        net.setInput(blob)
        detections = util.get_outputs(net)

        # Listy do przechowywania ramek, identyfikatorów klas i pewności
        bboxes = []
        class_ids = []
        scores = []

        # Przetwarzanie wykryć
        for detection in detections:
            bbox = detection[:4]

            xc, yc, w, h = bbox
            bbox = [int(xc * W), int(yc * H), int(w * W), int(h * H)]

            bbox_confidence = detection[4]

            class_id = np.argmax(detection[5:])
            score = np.amax(detection[5:])

            bboxes.append(bbox)
            class_ids.append(class_id)
            scores.append(score)

        # Zastosowanie NMS (usuwanie nakładających się ramek, aby zachować tylko te z najwyższą pewnością wykrycia)
        bboxes, class_ids, scores = util.NMS(bboxes, class_ids, scores)

        # Inicjalizacja czytnika EasyOCR
        reader = easyocr.Reader(['en'])
        for bbox_, bbox in enumerate(bboxes):
            xc, yc, w, h = bbox

            # Wycięcie tablicy rejestracyjnej z obrazu
            license_plate = img[int(yc - (h / 2)):int(yc + (h / 2)), int(xc - (w / 2)):int(xc + (w / 2)), :].copy()

            # Konwersja na skale szarości
            license_plate_gray = cv2.cvtColor(license_plate, cv2.COLOR_BGR2GRAY)

            _, license_plate_thresh = cv2.threshold(license_plate_gray, 64, 255, cv2.THRESH_BINARY_INV)

            # Rozpoznawanie tekstu za pomocą EasyOCR
            output = reader.readtext(license_plate_thresh)

            for out in output:
                text_bbox, text, text_score = out
                if text_score > 0.4:
                    # Zapis do CSV
                    writer.writerow([img_name, text, text_score])

                    # Rysowanie ramki wokół tablicy rejestracyjnej
                    cv2.rectangle(img, (int(xc - w / 2), int(yc - h / 2)), (int(xc + w / 2), int(yc + h / 2)),
                                  (0, 255, 0), 3)

                    # Rysowanie tekstu
                    cv2.putText(img, text, (int(xc - w / 2), int(yc - h / 2) - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.2,
                                (0, 0, 0), 7)


                    cv2.putText(img, text, (int(xc - w / 2), int(yc - h / 2) - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.2,
                                (0, 0, 255), 3)

        # Zapis obrazu z ramkami i tekstem
        output_img_path = os.path.join(output_dir, img_name)
        cv2.imwrite(output_img_path, img)

# Wyświetlenie wyników z pliku CSV
with open(output_csv, mode='r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)
