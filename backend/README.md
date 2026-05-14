# LearnWithAcel — Backend API

FastAPI + PostgreSQL + Prisma backend for the LearnWithAcel learning platform.

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI 0.115 |
| Database | PostgreSQL 16 |
| ORM | Prisma (Python) |
| Auth | JWT via PyJWT |
| Password hashing | passlib + bcrypt |
| Validation | Pydantic v2 |
| Runtime | Python 3.12 |

## Project Structure

```
backend/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── auth.py        # POST /auth/register, /auth/login, GET /auth/me
│   │       ├── content.py     # GET /categories, /roadmap/{slug}, /lessons/{level}/{lesson}
│   │       ├── progress.py    # POST /progress/complete/{id}, GET /progress/stats
│   │       └── router.py      # Aggregates all v1 routers
│   ├── core/
│   │   ├── config.py          # Pydantic Settings (env vars)
│   │   ├── database.py        # Prisma client singleton
│   │   ├── deps.py            # FastAPI dependency injection
│   │   ├── exceptions.py      # Custom HTTP exceptions + handlers
│   │   └── security.py        # Password hashing + JWT
│   ├── schemas/
│   │   ├── auth.py            # Request/response models for auth
│   │   ├── content.py         # Request/response models for content
│   │   └── progress.py        # Request/response models for progress
│   ├── services/
│   │   ├── auth_service.py    # Auth business logic
│   │   ├── content_service.py # Content business logic
│   │   └── progress_service.py# Progress business logic
│   └── main.py                # App factory + lifespan
├── prisma/
│   └── schema.prisma          # Database schema
├── scripts/
│   └── seed.py                # Data migration from static JS files
├── .env.example
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```

## Quick Start

### 1. Prerequisites

- Python 3.12+
- PostgreSQL 16 (or use Docker)

### 2. Setup

```bash
# Clone and enter backend directory
cd backend

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Copy and configure environment
copy .env.example .env
# Edit .env with your DATABASE_URL and JWT_SECRET_KEY
```

### 3. Database

```bash
# Generate Prisma client
prisma generate

# Push schema to database (creates tables)
prisma db push

# Seed with initial data
python -m scripts.seed

# Promote a registered user to admin (required for /api/v1/admin/* endpoints)
python -m scripts.promote_admin you@example.com
```

### 4. Run

```bash
uvicorn app.main:app --reload
```

API is available at `http://localhost:8000`  
Swagger docs at `http://localhost:8000/docs`

---

### Docker (alternative)

```bash
# Copy env file
copy .env.example .env

# Start everything (PostgreSQL + API)
docker-compose up --build
```

---

## API Endpoints

### Authentication

| Method | Path | Auth | Description |
|---|---|---|---|
| POST | `/api/v1/auth/register` | ❌ | Register new user |
| POST | `/api/v1/auth/login` | ❌ | Login, get JWT token |
| GET | `/api/v1/auth/me` | ✅ | Get current user profile |

### Content (Public)

| Method | Path | Auth | Description |
|---|---|---|---|
| GET | `/api/v1/categories` | ❌ | List all learning paths |
| GET | `/api/v1/roadmap/{category_slug}` | ❌ | Full roadmap for a category |
| GET | `/api/v1/lessons/{level_slug}/{lesson_slug}` | ❌ | Full lesson content |

### Progress (User)

| Method | Path | Auth | Description |
|---|---|---|---|
| POST | `/api/v1/progress/complete/{lesson_id}` | ✅ | Mark lesson as completed |
| GET | `/api/v1/progress/stats` | ✅ | Get learning statistics |

### Content Management (Admin)

All admin endpoints require a valid JWT token from a user with `is_admin = true`.

| Method | Path | Auth | Description |
|---|---|---|---|
| POST | `/api/v1/admin/categories` | 🔐 Admin | Create a new category |
| PUT | `/api/v1/admin/categories/{id}` | 🔐 Admin | Update a category |
| DELETE | `/api/v1/admin/categories/{id}` | 🔐 Admin | Delete a category (cascades) |
| POST | `/api/v1/admin/levels` | 🔐 Admin | Create a new level |
| PUT | `/api/v1/admin/levels/{id}` | 🔐 Admin | Update a level |
| DELETE | `/api/v1/admin/levels/{id}` | 🔐 Admin | Delete a level (cascades) |
| POST | `/api/v1/admin/lessons` | 🔐 Admin | Create a new lesson (with Markdown content) |
| PUT | `/api/v1/admin/lessons/{id}` | 🔐 Admin | Update a lesson / edit content |
| DELETE | `/api/v1/admin/lessons/{id}` | 🔐 Admin | Delete a lesson |

---

## Environment Variables

| Variable | Required | Default | Description |
|---|---|---|---|
| `DATABASE_URL` | ✅ | — | PostgreSQL connection string |
| `JWT_SECRET_KEY` | ✅ | — | Secret for signing JWT tokens |
| `JWT_ALGORITHM` | ❌ | `HS256` | JWT signing algorithm |
| `JWT_ACCESS_TOKEN_EXPIRE_MINUTES` | ❌ | `1440` | Token TTL (24h) |
| `CORS_ORIGINS` | ❌ | `http://localhost:3000` | Comma-separated allowed origins |
| `DEBUG` | ❌ | `false` | Enable debug mode |

## Security Notes

- Passwords are hashed with bcrypt (cost factor 12)
- JWT tokens expire after 24 hours by default
- Timing-safe password comparison prevents user enumeration
- CORS is restricted to configured origins only
- All inputs are validated via Pydantic before reaching business logic
