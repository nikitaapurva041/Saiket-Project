import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

# ---------------- SCRAPERS ---------------- #

def scrape_bbc():
    url = "https://www.bbc.com/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    headlines = soup.find_all("h2")

    data = []
    for h in headlines[:10]:
        text = h.get_text(strip=True)
        if text:
            data.append({
                "source": "BBC",
                "headline": text,
                "time": datetime.now().strftime("%Y-%m-%d %H:%M")
            })

    return data


def scrape_reuters():
    url = "https://www.reuters.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    headlines = soup.find_all("h2")

    data = []
    for h in headlines[:10]:
        text = h.get_text(strip=True)
        if len(text) > 20:
            data.append({
                "source": "Reuters",
                "headline": text,
                "time": datetime.now().strftime("%Y-%m-%d %H:%M")
            })

    return data


# ---------------- GUI FUNCTIONS ---------------- #

current_data = []

def fetch_news():
    try:
        text_area.delete("1.0", tk.END)

        bbc_data = scrape_bbc()
        reuters_data = scrape_reuters()

        all_news = bbc_data + reuters_data

        if not all_news:
            text_area.insert(tk.END, "No news found.")
            return

        # Remove duplicates
        df = pd.DataFrame(all_news)
        df.drop_duplicates(subset="headline", inplace=True)

        # Sort
        df.sort_values(by="source", inplace=True)

        # Display
        for i, row in df.iterrows():
            line = f"{i+1}. [{row['source']}] {row['headline']} ({row['time']})\n\n"
            text_area.insert(tk.END, line)

        global current_data
        current_data = df.to_dict(orient="records")

    except Exception as e:
        messagebox.showerror("Error", str(e))


def save_data():
    try:
        if not current_data:
            messagebox.showwarning("Warning", "No data to save")
            return

        df = pd.DataFrame(current_data)
        df.to_csv("news_data.csv", index=False)

        messagebox.showinfo("Success", "Data saved as news_data.csv")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------------- GUI SETUP ---------------- #

root = tk.Tk()
root.title("News Aggregator App")
root.geometry("700x500")

tk.Label(root, text="📰 Multi-Site News Aggregator", font=("Arial", 16, "bold")).pack(pady=10)

text_area = tk.Text(root, wrap="word")
text_area.pack(expand=True, fill="both", padx=10, pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Button(frame, text="Fetch News", command=fetch_news, bg="#2196F3", fg="white", width=15).grid(row=0, column=0, padx=5)

tk.Button(frame, text="Save to CSV", command=save_data, bg="#4CAF50", fg="white", width=15).grid(row=0, column=1, padx=5)

tk.Button(frame, text="Exit", command=root.quit, bg="#f44336", fg="white", width=15).grid(row=0, column=2, padx=5)

root.mainloop()
