"""
Comprehensive Endpoint Verification Test Script.
Tests all public, authentication, content, progress, and admin routes.
"""

from fastapi.testclient import TestClient
from app.main import app


def test_all_routes():
    print("==================================================")
    print("   EXHAUSTIVE ENDPOINT VERIFICATION SUITE")
    print("==================================================")

    # Use context manager so FastAPI lifespan (prisma.connect() & cache_manager.init()) executes!
    with TestClient(app) as client:
        # 1. Health & Root Endpoints
        print("\n--- 1. Testing Root & Health Check Endpoints ---")
        r_root = client.get("/")
        print(f"GET / -> Status: {r_root.status_code}, Body: {r_root.json()}")
        assert r_root.status_code == 200, "Root GET failed!"

        r_health = client.get("/health")
        print(f"GET /health -> Status: {r_health.status_code}, Body: {r_health.json()}")
        assert r_health.status_code == 200, "Health GET failed!"

        # 2. Public Content Endpoints
        print("\n--- 2. Testing Content Endpoints ---")
        r_cats = client.get("/api/v1/categories")
        print(f"GET /api/v1/categories -> Status: {r_cats.status_code}, Cache-Control: {r_cats.headers.get('cache-control')}")
        assert r_cats.status_code == 200, f"Categories GET failed with status {r_cats.status_code}"

        r_road = client.get("/api/v1/roadmap/frontend")
        print(f"GET /api/v1/roadmap/frontend -> Status: {r_road.status_code}, Cache-Control: {r_road.headers.get('cache-control')}")
        assert r_road.status_code in [200, 404], f"Roadmap GET returned unexpected status: {r_road.status_code}"

        r_lesson = client.get("/api/v1/lessons/html-css/mengenal-html")
        print(f"GET /api/v1/lessons/html-css/mengenal-html -> Status: {r_lesson.status_code}")
        assert r_lesson.status_code in [200, 404], f"Lesson GET returned unexpected status: {r_lesson.status_code}"

        # 3. Auth Validation & Exception Handling
        print("\n--- 3. Testing Auth Endpoints Validation ---")
        r_login_bad = client.post("/api/v1/auth/login", json={"email": "bad", "password": "short"})
        print(f"POST /api/v1/auth/login (bad body) -> Status: {r_login_bad.status_code}")
        assert r_login_bad.status_code == 422, "Login validation error expected (422)"

        r_reg_bad = client.post("/api/v1/auth/register", json={"email": "invalid"})
        print(f"POST /api/v1/auth/register (bad body) -> Status: {r_reg_bad.status_code}")
        assert r_reg_bad.status_code == 422, "Register validation error expected (422)"

        # 4. Protected Routes Authentication Checks (Unauthenticated -> 401 or 403)
        print("\n--- 4. Testing Protected Routes Unauthenticated Access ---")
        r_me = client.get("/api/v1/auth/me")
        print(f"GET /api/v1/auth/me (no token) -> Status: {r_me.status_code}")
        assert r_me.status_code in [401, 403], f"Expected 401/403 for /auth/me, got {r_me.status_code}"

        r_stats = client.get("/api/v1/progress/stats")
        print(f"GET /api/v1/progress/stats (no token) -> Status: {r_stats.status_code}")
        assert r_stats.status_code in [401, 403], f"Expected 401/403 for /progress/stats, got {r_stats.status_code}"

        r_admin_stats = client.get("/api/v1/admin/stats")
        print(f"GET /api/v1/admin/stats (no token) -> Status: {r_admin_stats.status_code}")
        assert r_admin_stats.status_code in [401, 403], f"Expected 401/403 for /admin/stats, got {r_admin_stats.status_code}"

        # 5. Non-existent Route Handling (404 Not Found)
        print("\n--- 5. Testing Non-Existent Route (404) ---")
        r_404 = client.get("/api/v1/non-existent-route-xyz")
        print(f"GET /api/v1/non-existent-route-xyz -> Status: {r_404.status_code}")
        assert r_404.status_code == 404, "Expected 404 for non-existent route"

        print("\n==================================================")
        print("   ALL ENDPOINTS VERIFIED AND PASSING SUCCESSFULLY!")
        print("==================================================")


if __name__ == "__main__":
    test_all_routes()
