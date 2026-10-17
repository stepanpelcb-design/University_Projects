# University Projects

Python projects from my BSc (Honours) Artificial Intelligence and Data Science degree at Middlesex University Dubai.

## Projects

### 1. Multi-Domain Intelligence Platform
**Folder:** [`multi_domain_platform-main`](multi_domain_platform-main)
**Tech:** Python, Streamlit, SQLite, OpenAI API, bcrypt, pandas

A multi-page web app for managing three domains: cyber security incidents, dataset metadata and IT support tickets.

- Full CRUD functionality and interactive charts for each domain
- AI assistant in every domain (GPT-4o-mini) for chatting about and analyzing the stored records
- Secure registration and login with bcrypt password hashing, input validation and password strength checks
- Role-based access, with admin users able to manage other accounts
- Object-oriented structure with separate models and services

**Run:** `streamlit run multi_domain_platform-main/Home.py` (full setup instructions in the project's README)

### 2. Dijkstra's Shortest Path Algorithm
**Folder:** [`Dijkstra's algorithm`](Dijkstra%E2%80%99s%20algorithm)
**Tech:** Python

An object-oriented implementation of Dijkstra's algorithm for weighted graphs.

- Loads graphs from JSON files and validates them (duplicate edges, wrong formats, missing vertices)
- Finds the shortest path and total distance between two vertices
- Tested on six graphs, including edge cases, with a written report on the results

**Run:** `python3 Main.py` from inside the project folder

### 3. London Crime Data Analysis
**Folder:** [`dataset_handling`](dataset_handling)
**Tech:** Python, Jupyter, pandas, NumPy, lets-plot

A data analysis of Metropolitan Police street crime data from August 2023 to July 2025 (over 2 million records).

- Loading, merging and cleaning 24 monthly datasets
- Finding crime hotspots by borough and crime type
- Visualizing crime trends over time
- Calculating proportions and 95% confidence intervals
- Also includes a simple knowledge base with a query function and a perceptron implemented from scratch

**Run:** open `Assessment 1 - Stepan Pelc.ipynb` in Jupyter

## Author
Stepan Pelc
