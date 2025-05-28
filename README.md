# 🦸‍♂️ Superhero Universe Network – Take-Home Assignment

Welcome! This project is a take-home coding assignment for the **Dataiskole Internship Qualification**.  
Your challenge is to analyze a superhero network using two CSV files and extract key insights.

---

<img width="426" alt="Superhero Network" src="https://media.npr.org/assets/img/2016/06/09/john-p-fleenor-courtesy-of-hbo_wide-f730538a10afad26c9de9a42561772522e4e87e6.jpg?s=1400&c=100&f=jpeg" />

---

## 📘 Project Overview

In this superhero universe:

- Each **superhero is a node**
- Each **friendship is a connection (edge)** between superheroes

You are provided with:

- `superheroes.csv`: Contains superhero ID, name, and created date
- `links.csv`: Contains pairs of superhero IDs who are friends

Your task is to read the data and generate useful insights and a visual graph.

---

## ✅ Features & Insights

This project:

- 🔢 Calculates the total number of superheroes
- 🔗 Computes total number of connections
- 🆕 Identifies superheroes added in the last **3 days**
- 🏆 Finds the **Top 3 most connected superheroes**
- 👤 Shows details of a special superhero named `dataiskole`:
  - When they were added
  - Who their friends are

---

## 🎨 Bonus Features

- 📈 Visual graph of the superhero network using `NetworkX` and `Matplotlib`
- 🌐 Streamlit-based interactive web app for viewing the data and results

---

## 🧰 Tech Stack

- Python 3.8+
- Pandas
- NetworkX
- Matplotlib
- Streamlit

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Sandeep992299/Superhero-Network-Challenge.git
cd Superhero-Network-Challenge
### 2. (Optional) Create a Virtual Environment
bash
Copy
Edit
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
### 3. Install Required Packages
bash
Copy
Edit
pip install -r requirements.txt
If requirements.txt is missing, install manually:

bash
Copy
Edit
pip install pandas networkx matplotlib streamlit
🚀 Running the Streamlit App
Run the Streamlit app with:

bash
Copy
Edit
streamlit run data/app.py
Make sure app.py is inside the data/ folder.

### 🧪 Sample Output
markdown
Copy
Edit
🔢 Total superheroes: 11
🔗 Total connections: 40

🆕 Superheroes added in the last 3 days:
  - Doctor Strange (2025-05-23)
  - Black Panther (2025-05-23)
  - Scarlet Witch (2025-05-24)
  - Ant-Man (2025-05-24)
  - dataiskole (2025-05-26)

🏆 Top 3 most connected superheroes:
  - Spider-Man (9 friends)
  - Iron Man (8 friends)
  - Thor (7 friends)

👤 Info on 'dataiskole':
  - Added on: 2025-05-26
  - Friends: Spider-Man, Captain America, Scarlet Witch

✅ Network graph saved as: `graph.png`
