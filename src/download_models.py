import os
import gdown

# --- Configuration des modèles ---
models_to_download = [
    {
        "name": "fasttext_full_model",
        "local_path": "../models/embeddings/cc.fr.300.bin",
        "drive_id": "165QiIF_OKBG9wccs8tOrm0FJ_vma3azf"
    },
    {
        "name": "fasttext_words_model_vectors",
        "local_path": "../models/embeddings/fasttext_fr.kv.vectors.npy",
        "drive_id": "1gqZOPuEprMxolbl1jkhyWmm1Px6rMeFW"
    },
    {
        "name": "fasttext_words_model",
        "local_path": "../models/embeddings/fasttext_fr.kv",
        "drive_id": "11xslkCM8GXUW5cvSwGLxapFplnVmWwTE"
    },
    {
        "name": "word2vec_model_1",
        "local_path": "../models/embeddings/frWac_no_postag_no_phrase_500_skip_cut100.bin",
        "drive_id": "11t4Ld2HbMTNtNuhBzICs79G41Tb7L-1d"
    },
    {
        "name": "word2vec_model_2",
        "local_path": "../models/embeddings/frWac_postag_no_phrase_700_skip_cut50.bin",
        "drive_id": "1z9RA34Hp-kxTb62bmvHEOWTsveYZAGla"
    },
    {
        "name": "word2vec_model_3",
        "local_path": "../models/embeddings/frWac_postag_no_phrase_1000_skip_cut100.bin",
        "drive_id": "1mxo6zevEPzE212LvHeSmy2Vn8hs32F80"
    },
    {
        "name": "language_detection_model",
        "local_path": "../models/language_detection/lid.176.ftz",
        "drive_id": "1gUKkv-_zZQvvLqe6Bq9RUFDj9RnDCwjZ"
    }
]

# --- Fonction pour télécharger un fichier si nécessaire ---
def download_if_missing(local_path, drive_id):
    if not os.path.exists(local_path):
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        url = f"https://drive.google.com/uc?id={drive_id}"
        print(f"Téléchargement de {local_path} depuis Google Drive...")
        gdown.download(url, local_path, quiet=False)
    else:
        print(f"{local_path} déjà présent, pas de téléchargement nécessaire.")

# --- Télécharger les modèles manquants ---
for model in models_to_download:
    download_if_missing(model["local_path"], model["drive_id"])

print("Tous les modèles sont prêts !")
