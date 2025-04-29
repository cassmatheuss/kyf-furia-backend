import base64
import numpy as np
import face_recognition as fr
import cv2

def clean_base64(b64_string):
    if ',' in b64_string:
        b64_string = b64_string.split(',', 1)[1]
    b64_string += '=' * ((4 - len(b64_string) % 4) % 4)
    return b64_string

def compare_faces_base64(document_b64, user_image_b64, tolerance=0.6):
    def b64_to_image(b64_string):
        b64_string = clean_base64(b64_string)
        try:
            img_data = base64.b64decode(b64_string)
        except Exception as e:
            raise Exception(f"Erro ao decodificar base64: {e}")
        np_arr = np.frombuffer(img_data, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        if img is None:
            raise Exception("Não foi possível decodificar a imagem (cv2.imdecode retornou None).")
        return img

    doc_img = b64_to_image(document_b64)
    user_img = b64_to_image(user_image_b64)

    doc_encodings = fr.face_encodings(cv2.cvtColor(doc_img, cv2.COLOR_BGR2RGB))
    user_encodings = fr.face_encodings(cv2.cvtColor(user_img, cv2.COLOR_BGR2RGB))

    if not doc_encodings or not user_encodings:
        return False

    result = fr.compare_faces([doc_encodings[0]], user_encodings[0], tolerance=tolerance)
    return result[0]
