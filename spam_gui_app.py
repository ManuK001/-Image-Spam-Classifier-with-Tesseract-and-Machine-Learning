import re
import pytesseract
from PIL import Image, ImageTk
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import tkinter as tk
from tkinter import filedialog, messagebox

# === Setup Tesseract Path (Update this if different) ===
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# === Step 1: Load and Train Model ===
df = pd.read_csv("spam.csv", encoding="latin-1")[["v1", "v2"]]
df.columns = ['label', 'message']
df['message'] = df['message'].apply(lambda x: re.sub(r'\W+', ' ', str(x).lower()))
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['message'])
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = MultinomialNB()
model.fit(X_train, y_train)

# === Step 2: Helper Functions ===
def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    cleaned = re.sub(r'\W+', ' ', text.lower())
    return cleaned

def classify_image_text(image_path):
    text = extract_text_from_image(image_path)
    vector = vectorizer.transform([text])
    prediction = model.predict(vector)
    return 'Spam' if prediction[0] == 1 else 'Ham', text

# === Step 3: GUI Setup ===
def browse_image():
    file_path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")]
    )
    if not file_path:
        return

    try:
        prediction, extracted = classify_image_text(file_path)
        img = Image.open(file_path).resize((300, 300))
        img_tk = ImageTk.PhotoImage(img)
        image_label.config(image=img_tk)
        image_label.image = img_tk
        result_label.config(text=f"Prediction: {prediction}")
        text_label.config(text=f"Extracted Text:\n{extracted}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# === Tkinter GUI Layout ===
root = tk.Tk()
root.title("Spam or Ham Classifier")
root.geometry("450x600")

btn = tk.Button(root, text="Select Image", command=browse_image, font=("Arial", 14), bg="lightblue")
btn.pack(pady=20)

image_label = tk.Label(root)
image_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 16, "bold"))
result_label.pack(pady=10)

text_label = tk.Label(root, text="", font=("Arial", 10), wraplength=400, justify="left")
text_label.pack(pady=10)

root.mainloop()
