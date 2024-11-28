**Language Translator Tool**
============================

A Python-based tool for translating text between languages using the `googletrans` library. This project simplifies language translation by leveraging Google Translate's API and supports a wide range of languages.

* * * * *

### **Features**

-   **Multi-Language Translation**: Translate text dynamically between various supported languages.
-   **User-Friendly Input**: Enter text and specify source and destination language codes for seamless translation.
-   **Built-In Error Handling**: Provides informative messages in case of translation failures.
-   **Lightweight and Simple**: Easy to set up and extend for additional features.

* * * * *

### **Requirements**

-   Python 3.8+
-   `googletrans` library

* * * * *

### **Usage**

1.  Clone the repository:

    ```bash
    git clone https://github.com/FurqanTheGreat/CodeAlpha_Language_Translation_Tool.git
    cd CodeAlpha_Language_Translation_Tool
    ```

2.  Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3.  Run the script:

    ```bash
    python translator.py
    ```

* * * * *

### **How It Works**

1.  Enter the text you want to translate.
2.  Specify the source language (e.g., English) or leave it blank for auto-detection.
3.  Specify the target language code (e.g., Spanish).
4.  View the translated text instantly!

* * * * *

### **Example**

#### Input:

```plaintext
Simple Language Translation Tool

        Supported languages: English, Spanish, French, German, etc.

        Enter text to translate: Hello, how are you
        Enter source language (leave blank for auto-detection): English
        Enter destination language: Spanish
```

#### Output:

```plaintext
        Source Language: English
        Translated Text (english -> spanish):
        Hola, ¿cómo estás?
```
