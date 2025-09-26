

---

# ✨ Fast Auth: Secure Google OAuth Template (FastAPI + Next.js)

**Fast Auth** is a minimalist, modular, and secure full-stack template for implementing Google OAuth 2.0. It's designed for developers who need a production-grade authentication starter kit without the bloat.

It solves a common problem: most auth tutorials are either too basic (insecure) or over-engineered. This template hits the sweet spot, using best practices like **HttpOnly cookies**, **CSRF protection**, and a **decoupled service-oriented architecture**.

### ✨ Demo

Watch the 60-second walkthrough to see the seamless user flow from the landing page to the authenticated dashboard.

[![Fast Auth Demo](https://img.youtube.com/vi/6Ok3jafXzFE/maxresdefault.jpg)](https://www.youtube.com/watch?v=6Ok3jafXzFE)

### 📖 In-Depth Article

For a complete, layer-by-layer breakdown of the architecture, security decisions, and code, read the full article on Medium:

**[Fast Auth: A Secure, Minimalist Google OAuth Template with FastAPI & Next.js](https://medium.com/@amirabdallahpfe/fast-auth-a-secure-minimalist-google-oauth-template-with-fastapi-next-js-3a87d375ff68)**

---

## ✅ Features

-   **Secure Authentication Flow**: Implements the complete OAuth 2.0 Authorization Code Flow.
-   **HttpOnly Cookies for Sessions**: Stores JWTs securely, preventing access from client-side JavaScript (XSS protection).
-   **CSRF Protection**: Uses the `state` parameter in a short-lived cookie to mitigate Cross-Site Request Forgery.
-   **Decoupled Architecture**: Clear separation between the FastAPI backend and Next.js frontend.
-   **Database Integration**: Uses SQLAlchemy with Neon (PostgreSQL) to persist user data.
-   **Database Migrations**: Alembic is configured for safe and version-controlled schema changes.
-   **Environment-Based Configuration**: Easily manage secrets and settings for different environments.
-   **Containerized**: One-command setup using Docker and Docker Compose.

## 🛠️ Tech Stack

| Area      | Technology                                                      |
| :-------- | :-------------------------------------------------------------- |
| **Backend** | 🐍 FastAPI, 🐘 PostgreSQL (Neon), 🗃️ SQLAlchemy, 📜 Alembic       |
| **Frontend**| ⚛️ Next.js, 🔷 TypeScript, 🎨 Tailwind CSS, 🧩 ShadCN/ui          |
| **Infra**   | 🐳 Docker, 🐋 Docker Compose                                       |
| **Auth**    | 🔐 JWT, 🇬 Google OAuth 2.0                                      |

---

## 🏁 Getting Started

Follow these steps to get the project running locally.

### Prerequisites

-   [Git](https://git-scm.com/)
-   [Docker](https://www.docker.com/products/docker-desktop/)
-   [Docker Compose](https://docs.docker.com/compose/)
-   **Google OAuth Credentials** (Client ID & Client Secret). You can get these from the [Google Cloud Console](https://console.cloud.google.com/).

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Fast-Auth.git
cd Fast-Auth
```

### 2. Configure Backend Environment

Navigate to the `backend` directory and create your `.env` file.

```bash
cd backend
cp .env.example .env
```

Now, open the `.env` file and fill in your credentials:

```env
# backend/.env

# Database URL (Neon DB or local Postgres)
DB_URL="postgresql://user:password@host:port/dbname"

# Google OAuth Credentials
GOOGLE_CLIENT_ID="YOUR_GOOGLE_CLIENT_ID"
GOOGLE_CLIENT_SECRET="YOUR_GOOGLE_CLIENT_SECRET"

# JWT Settings (Generate a new secret)
# Run `openssl rand -hex 32` in your terminal to create one
SECRET_KEY="YOUR_32_BYTE_HEX_SECRET_KEY"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Application URLs
FRONTEND_URL="http://localhost:3000"
BACKEND_URL="http://localhost:8000"
```

### 3. Configure Frontend Environment

Navigate to the `frontend` directory and create your `.env.local` file.

```bash
cd ../frontend
cp .env.example .env.local
```

The file should contain the backend API URL:

```env
# frontend/.env.local
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
```

### 4. Build and Run with Docker Compose

Return to the root directory of the project and start the application.

```bash
cd ..
docker-compose up --build -d
```

-   The `-d` flag runs the containers in detached mode.

### 5. Run Database Migrations

With the containers running, execute the Alembic migrations to create the `users` table in your database.

```bash
docker-compose exec backend alembic upgrade head
```

You should see output indicating that the migration script has run successfully.

### 6. Access the Application

🎉 **You're all set!**

-   Frontend is running at: **[http://localhost:3000](http://localhost:3000)**
-   Backend API is available at: **[http://localhost:8000](http://localhost:8000)**
-   API docs (Swagger UI) at: **[http://localhost:8000/docs](http://localhost:8000/docs)**

---

## 📂 Project Structure

The project is organized into distinct `backend` and `frontend` directories, each with a modular, scalable structure.

```
/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── db/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── security/
│   │   └── services/
│   ├── alembic/
│   └── Dockerfile
├── frontend/
└── docker-compose.yml
```

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.