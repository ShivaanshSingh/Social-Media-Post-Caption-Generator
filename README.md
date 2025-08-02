# Social Media Post & Caption Generator

This project is a **Streamlit web application** that generates **catchy captions, hashtags, and emojis** for social media posts using **Google Gemini (Generative AI)**.  

Users can provide **keywords or themes**, select a **platform** (Instagram, Twitter, LinkedIn), and instantly generate a ready-to-post social media caption with relevant hashtags and emojis.  

---

## Features

- Generate **catchy social media captions** based on your keywords.
- Suggest **5-7 relevant hashtags** automatically.
- Include **3-5 engaging emojis** to boost post visibility.
- Supports **Instagram, Twitter, and LinkedIn**.
- **Download generated captions** as a `.txt` file.
- Handles **JSON output from Gemini** and cleans it for display.

---

## Tech Stack

- **Python 3.8+**
- **Streamlit** for the web interface
- **Google Generative AI (Gemini 1.5 Flash)** for text generation
- **JSON** for structured AI response handling

---

## Installation

1. **Clone the Repository**  
```bash
git clone https://github.com/yourusername/social-media-caption-generator.git
cd social-media-caption-generator
```

2. **Create Virtual Environment (Optional but Recommended)**  
```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```

3. **Install Dependencies**  
```bash
pip install -r requirements.txt
```

4. **Set Your Gemini API Key**  
- Open the Python file (`app.py`)  
- Replace the line:  
```python
genai.configure(api_key="YOUR_GEMINI_API_KEY")
```  
with your actual **Gemini API key**.

---

## Usage

Run the Streamlit application:

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal (usually `http://localhost:8501`) to use the web app.

---

## Example Workflow

1. Enter keywords or theme, e.g.,  
   ```
   Fitness, Morning Workout, Motivation
   ```
2. Select a platform, e.g., **Instagram**  
3. Click **Generate Post**  
4. View the generated:  
   - Caption  
   - Hashtags  
   - Emojis  
5. Download the caption as a `.txt` file if needed

---

## Project Structure

```
social-media-caption-generator/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .gitignore              # Optional: Ignore virtual env & system files
```

---

## Requirements

- Python 3.8+
- Streamlit
- Google Generative AI (`google-generativeai`)

Install using:

```bash
pip install streamlit google-generativeai
```

---

## Future Enhancements

- Generate **multiple caption variations** in a single click
- Add **Twitter character limit validation**
- Optional **AI-generated images** for Instagram posts
- Save post history in a **local database**

---

## License

This project is released under the **MIT License**. You are free to modify and distribute it with attribution.
