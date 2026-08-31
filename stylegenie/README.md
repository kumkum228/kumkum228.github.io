# ✨ StyleGenie – AI Fashion Shopping Assistant

An original, Myntra-inspired fashion e-commerce web application with a
**Google Gemini–powered AI shopping assistant**. Users browse fashion
products and chat with **StyleGenie AI** to discover items, build outfits,
and get recommendations — where every recommended product actually exists in
the database.

> **Portfolio project.** No real brand assets are copied. All products,
> images, and branding are original or placeholder/royalty-free.

---

## 🚧 Build progress

This project is built in **15 phases**. Each phase is completed and reviewed
before moving on.

| Phase | Description | Status |
|------|-------------|--------|
| 1 | Project architecture & setup | ✅ Done |
| 2 | React frontend structure & routing | ⏳ Next |
| 3 | UI components & homepage | — |
| 4 | Product listing & product details | — |
| 5 | MySQL database & sample products | — |
| 6 | FastAPI backend | — |
| 7 | Authentication (JWT) | — |
| 8 | Cart & wishlist | — |
| 9 | Orders | — |
| 10 | Gemini API integration | — |
| 11 | AI Shopping Assistant | — |
| 12 | AI recommendation engine | — |
| 13 | Responsive design | — |
| 14 | Testing & debugging | — |
| 15 | Final README & deployment prep | — |

---

## 🧱 Technology stack

| Layer | Technology | Why |
|-------|-----------|-----|
| Frontend | React + Vite, React Router, Axios | Fast, component-based UI |
| Backend | Python + FastAPI | Simple, modern, auto-documented REST API |
| Database | MySQL (via SQLAlchemy) | Reliable relational storage |
| AI | Google Gemini API | Natural-language shopping assistant |
| Auth | JWT + bcrypt | Secure login without storing plain passwords |

---

## 🏛️ Architecture — how the pieces talk

```
  Browser (React app on :5173)
        |  HTTP (JSON) via Axios
        v
  FastAPI backend (:8000)
        |                     \
        | SQLAlchemy           \  Gemini client (backend only)
        v                       v
  MySQL (stylegenie_db)     Google Gemini API
```

**Key rule:** the browser never talks to MySQL or Gemini directly. It only
talks to the FastAPI backend. The **Gemini API key lives only on the backend**
(in `backend/.env`) so it is never exposed to users.

The AI recommendation flow (built in Phases 10–12):

```
User message → FastAPI → understand intent → search MySQL for real products
→ send those products to Gemini → Gemini writes a friendly reply
→ backend returns { message, products, filters } → React renders product cards
```

---

## 📁 Folder structure

```
stylegenie/
├── frontend/                 # React app (Vite)
│   ├── src/
│   │   ├── components/       # Reusable UI (Header, ProductCard, Chatbot…)
│   │   ├── pages/            # Full pages (Home, Product, Cart…)
│   │   ├── services/         # api.js – talks to the backend
│   │   ├── context/          # Global state (auth, cart, wishlist)
│   │   ├── assets/           # Images, icons
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── index.html
│   ├── package.json
│   └── .env.example
│
├── backend/                  # FastAPI app
│   ├── app/
│   │   ├── main.py           # API entry point
│   │   ├── config.py         # Reads .env into settings
│   │   ├── database.py       # MySQL connection
│   │   ├── models/           # SQLAlchemy table models
│   │   ├── schemas/          # Pydantic request/response shapes
│   │   ├── routes/           # API endpoints
│   │   ├── services/         # Business logic
│   │   └── ai/               # Gemini integration
│   ├── requirements.txt
│   └── .env.example
│
├── database/
│   └── schema.sql            # Creates DB + tables + sample data
│
├── README.md
└── .gitignore
```

---

## ✅ Prerequisites (install these once)

- **Node.js** 18+ — https://nodejs.org  (`node -v` to check)
- **Python** 3.10+ — https://python.org  (`python --version`)
- **MySQL** — easiest via **XAMPP** (https://apachefriends.org), which bundles
  MySQL + phpMyAdmin. Start MySQL from the XAMPP control panel.
- **VS Code** — recommended editor.
- A **Google Gemini API key** — free from https://aistudio.google.com/app/apikey
  (needed from Phase 10 onward, not required yet).

---

## 🚀 Setup & run (Phase 1)

### 1. Backend (FastAPI)

```bash
cd stylegenie/backend

# create an isolated Python environment
python -m venv venv

# activate it
# macOS/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# install dependencies
pip install -r requirements.txt

# create your env file and fill it in
cp .env.example .env

# run the API
uvicorn app.main:app --reload
```

Now visit:
- http://localhost:8000/api/health → `{"status":"ok"}`
- http://localhost:8000/docs → interactive API docs

### 2. Database (MySQL)

Start MySQL (XAMPP → Start MySQL), then:

```bash
cd stylegenie/database
mysql -u root -p < schema.sql
```

Or in phpMyAdmin: **Import → choose `schema.sql` → Go**.
(Phase 1 only creates the empty `stylegenie_db`; tables arrive in Phase 5.)

### 3. Frontend (React)

Open a **second terminal**:

```bash
cd stylegenie/frontend

# install dependencies
npm install

# create your env file
cp .env.example .env

# run the dev server
npm run dev
```

Open http://localhost:5173 — you should see the StyleGenie welcome page
showing **Backend status: ok** (proving frontend ↔ backend communication).

---

## 🔐 Environment variables

**backend/.env** (secrets — never committed):

| Variable | Purpose |
|----------|---------|
| `DATABASE_URL` | MySQL connection string |
| `JWT_SECRET` | Signs login tokens |
| `GEMINI_API_KEY` | Google Gemini key (backend only) |
| `FRONTEND_ORIGINS` | Which frontend URLs may call the API (CORS) |

**frontend/.env** (safe, public):

| Variable | Purpose |
|----------|---------|
| `VITE_API_BASE_URL` | Where the React app finds the backend |

> ⚠️ The Gemini API key goes **only** in `backend/.env`. Never place it in the
> frontend — anything in the frontend is visible to every visitor.

---

## 🔮 Coming next

**Phase 2** builds the React frontend structure: routing, the shared Header
(Men / Women / Kids / Beauty / Home + search + AI Assistant + Cart), a Footer,
and empty page components wired to routes.
