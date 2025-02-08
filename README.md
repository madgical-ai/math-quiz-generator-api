# FastAPI Math Question Generator with Google Sheets Integration

This guide will help you set up and run the FastAPI server for generating math questions and integrate it with Google Sheets for automatic execution.

---

## 📌 Prerequisites

### **1. Install Python and Virtual Environment**

Ensure you have Python installed. Then, create and activate a virtual environment:

```bash
python -m venv myenv
source myenv/bin/activate  # On macOS/Linux
myenv\Scripts\activate    # On Windows
```

### **2. Install Dependencies**

Run the following command to install all required packages:

```bash
pip install -r requirements.txt
```

---

## 🔑 **Setting Up API Keys**

To use Langsmith and Gemini, create a `.env` file in the root of your project and add the following lines:

```
LANGSMITH=<your_langsmith_api_key>
GEMINI=<your_gemini_api_key>
```

### **Steps to Get API Keys**

#### **1. Get Langsmith API Key**

1. Go to [Langsmith](https://smith.langchain.com/) and log in.
2. Navigate to **API Keys** in your account settings.
3. Generate a new API key and copy it.
4. Paste it into the `.env` file under `LANGSMITH=`.

#### **2. Get Gemini API Key**

1. Visit [Google AI Studio](https://aistudio.google.com/) and sign in.
2. Go to **API Keys** under your account settings.
3. Generate a Gemini API key and copy it.
4. Paste it into the `.env` file under `GEMINI=`.

After adding the keys, restart your FastAPI server to apply the changes.

---

## 🚀 **Setting Up FastAPI**

### **1. Running the FastAPI Server**

If you have cloned the repository, navigate to the project folder and start the FastAPI server:

```bash
uvicorn app:app --reload
```

By default, FastAPI will run at `http://127.0.0.1:8000`.

### **2. Exposing FastAPI with Ngrok**

Since Google Sheets cannot access `localhost`, use **ngrok** to expose your API publicly:

1. Install ngrok if not already installed:

   ```bash
   pip install pyngrok
   ```

2. Start ngrok on port 8000:

   ```bash
   ngrok http 8000
   ```

3. Copy the `https://your-ngrok-url.ngrok.io` URL and update **Settings!B1** in Google Sheets with:

   ```
   https://your-ngrok-url.ngrok.io/ask
   ```

---

## 📊 **Google Sheets Integration**

[Open Google Sheet](https://docs.google.com/spreadsheets/d/1YkjLOhFM05cFQ-hdapT5a7LDkckddi2BTPqGLPsSGLA/edit?gid=0#gid=0)

### **1. Add API URL to the "Settings" Sheet**

- Open your **Google Sheets**.
- Create a new sheet named **Settings**.
- In **cell B1**, paste your **ngrok API URL**:
  ```
  https://your-ngrok-url.ngrok.io/ask
  ```

### **2. Running the Script**

1. Save and refresh your Google Sheet.
2. Go to **Extensions > 🚀 Fetch Data > Run FetchMathQuestions**.
3. The sheet will start fetching data and updating each row with API-generated math questions.

---

## 🎯 **Final Notes**

- Ensure FastAPI is running before executing the script.
- Always use the **ngrok URL** instead of `localhost` in Google Sheets.
- If the API is deployed online, replace the **ngrok URL** with the **live API URL** in **Settings!B1**.

🚀 Enjoy automating math question generation with FastAPI & Google Sheets!

