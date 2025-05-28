# 🦸‍♂️ Superhero Universe Network – Take-Home Assignment

Welcome! This project is part of a take-home coding challenge where you will design and analyze a superhero network using two CSV files.

---

<img width="426" alt="Screenshot 2025-05-26 at 21 17 15" src="https://media.npr.org/assets/img/2016/06/09/john-p-fleenor-courtesy-of-hbo_wide-f730538a10afad26c9de9a42561772522e4e87e6.jpg?s=1400&c=100&f=jpeg">

---

## 📘 Project Story

In this superhero universe:

- Each **superhero is a node**
- Each **friendship is a connection (edge)** between superheroes

Given:
- `superheroes.csv`: Contains superhero ID, name, and created date
- `links.csv`: Contains pairs of superhero IDs who are friends

Your task: Read the data and generate key insights about the superhero network.

---

## ✅ Features & Insights

The Python program provides:

- ✅ Total number of superheroes
- ✅ Total number of connections (edges)
- ✅ Superheroes added in the last **3 days**
- ✅ Top 3 most connected superheroes
- ✅ Information about a special superhero named `dataiskole`
  - When was `dataiskole` added?
  - Who are their friends?

---

## 🎨 Bonus Features

- 📊 **Visual graph** of the superhero network using `networkx` and `matplotlib`
- 💻 Optional Streamlit app interface for interactive viewing

---

🧪 Sample Output
markdown
Copy
Edit
🔢 Total superheroes: 11
🔗 Total connections: 40
🆕 Superheroes added in last 3 days:
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

✅ Network graph saved to graph.png



