Image-Spam-Classifier-with-Tesseract-and-Machine-Learning
A Python project that uses Tesseract OCR to extract text from images and classifies the text as Spam or Ham using a Naive Bayes model trained on SMS data. Includes a simple Tkinter GUI for image upload, text preview, and real-time prediction.

🔍 Features
🧠 Spam Classification using Multinomial Naive Bayes

🖼️ Text Extraction from Images with Tesseract OCR

🖥️ Graphical User Interface using Tkinter

📄 Displays extracted text and prediction result instantly

🛠️ Tech Stack
Python

Tesseract OCR

Scikit-learn

Pandas

Tkinter

Regular Expressions

📁 Dataset
The model is trained using the SMS Spam Collection Dataset from kaggle.
(https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset?resource=download)

🚀 How It Works
Load and preprocess SMS spam data

Train a Naive Bayes classifier using CountVectorizer

Use Tesseract to extract text from a selected image

Predict whether the extracted text is Spam or Ham

Display the image, extracted text, and prediction result in the GUI

✅ Conclusion
This project demonstrates the effective integration of OCR technology with machine learning to classify image-based text as spam or ham. By combining Tesseract OCR, Naive Bayes classification, and a simple Tkinter GUI, it offers a practical tool for spam detection from images. It highlights how traditional text-based models can be extended to handle real-world image inputs, making it useful for scenarios like screenshot analysis, document scanning, or automated moderation tools.

![Screenshot 2025-05-11 172611](https://github.com/user-attachments/assets/207467c8-44f4-4ec8-8390-6f3668b392a3)
