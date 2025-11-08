🧠 My Django REST Framework Learning Journey

Over the course of this practice project, I explored and implemented many important concepts of Django REST Framework (DRF) — from the fundamentals of REST APIs to advanced techniques like filtering, pagination, and nested serializers.

Below is a detailed outline of my learning path and key milestones.

📘 1. API Fundamentals

What is an API? — Understanding the concept of Application Programming Interfaces.

What is REST API? — Learning how RESTful principles use HTTP methods (GET, POST, PUT, DELETE) for communication.

⚙️ 2. Environment Setup

Installed Django and Django REST Framework (DRF).

Created Django apps and configured REST Framework settings.

Set up endpoints and verified API responses.

🌐 3. Building API Endpoints

Created and tested simple endpoints to serve JSON data.

Learned how web applications communicate through API URLs and routes.

Built function-based API endpoints to handle basic requests.

🧱 4. Models & Serialization

Created data models such as Student, Employee, and Blog.

Performed manual serialization (converting Python objects to JSON).

Used Serializers and ModelSerializers to simplify object transformations.

Implemented Nested Serializers for relationships (e.g., Blog ↔ Comments).

🧩 5. Views in DRF

Function-Based Views (FBV) — Handled GET, POST, PUT, DELETE manually.

Class-Based Views (CBV) — Introduced reusability and cleaner logic.

Used Mixins (ListModelMixin, CreateModelMixin, RetrieveModelMixin, etc.).

Practiced GenericAPIView and Generic Views like:

ListCreateAPIView

RetrieveUpdateDestroyAPIView

Implemented ViewSets and ModelViewSets for automatic CRUD routing.

⚡ 6. CRUD Operations

Created, retrieved, updated, and deleted model objects via REST APIs.

Performed primary key-based lookups for single object retrieval.

Implemented complete CRUD functionality for both Students and Employees.

🔍 7. Advanced Features

Pagination

Configured Global Pagination in settings.

Created Custom Pagination classes.

Filtering

Implemented basic filters.

Built Custom Filters (e.g., filter Employees by name, ID, or designation).

Learned Advanced Filtering, Search, and Ordering Filters.

🧠 8. Additional Learning

Understood the flow between Django views, serializers, and models.

Practiced API development following RESTful conventions.

Learned how to connect DRF with frontends (React) and ML projects (overview).

🧰 9. Tools & Technologies

Python 3.x

Django

Django REST Framework (DRF)

SQLite3 (default database)

Postman / Browser API testing

🚀 10. What’s Next

My next steps are to explore:

Authentication & Permissions (JWT, TokenAuth)

API documentation tools (drf-yasg, drf-spectacular)

DRF Testing with pytest and APITestCase

DRF + React integration
