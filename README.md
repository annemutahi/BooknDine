# 🍽️ BooknDine — Restaurant Booking & Management System

**BooknDine** is a Django-based restaurant booking and staff management system with two integrated apps:  
- **Book** – for guest bookings and table management.  
- **Staff** – for staff authentication, reservation control, and API access.

The platform provides both a **web interface** and **REST API endpoints** to support frontend clients or third-party integrations.

---

## ⚙️ Core Features

✅ **Guest Reservations** — Guests can make bookings online.  
✅ **Table Management** — Reservations are tied to specific tables and positions.  
✅ **Staff Dashboard** — Staff can view, confirm, or cancel bookings.  
✅ **Role-Based Access** — Separate permissions for staff, admin, and guests.  
✅ **RESTful API** — All major features are accessible via REST endpoints.  
✅ **CRUD Operations** — Full create, read, update, and delete functionality.

---

## 🧠 Tech Stack

| Component | Technology |
|------------|-------------|
| **Framework** | Django 5.2.5 |
| **API Framework** | Django REST Framework (DRF) |
| **Language** | Python 3.13 |
| **Frontend** | HTML, CSS, Bootstrap |
| **Database** | MySQL |
| **Server** | Django Development Server |
| **Authentication** | Django built-in & token-based (API) |

---

## 🗂️ App Overview

### 🧾 **Book App**
Handles guest reservations, table management, and confirmation views.

**Key Models:** `Guests`, `Table`, `Bookings`  
**Primary Views:** Guest registration, booking creation, and confirmation.

---

### 👨‍🍳 **Staff App**
Handles staff authentication, dashboard management, and booking updates.

**Key Models:** `StaffProfile`  
**Primary Views:** Staff login, dashboard, and status updates.

---

## 🌐 Web Interfaces

| Interface | URL | Description |
|------------|------|-------------|
| **Guest Portal** | [`/book/`](http://127.0.0.1:8000/book/) | For guests to make and view bookings |
| **Staff Portal** | [`/staff/dashboard/`](http://127.0.0.1:8000/staff/dashboard/) | Staff dashboard and management view |
| **Admin Panel** | [`/admin/`](http://127.0.0.1:8000/admin/) | Django admin site for superusers |

---

## 🔗 URL ROUTES

### 📘 **Book App**

#### Web Routes
| URL | View | Description |
|------|------|-------------|
| `/book/guest/add/` | `GuestCreateView` | Add a new guest |
| `/book/guest/<int:pk>/` | `GuestDetailView` | View guest details |
| `/book/bookings/add/` | `BookingCreateView` | Create a new booking |
| `/book/bookings/<int:pk>/` | `BookingDetailView` | View booking details |
| `/book/bookings/confirmation/<int:booking_id>/` | `booking_confirmation` | Booking confirmation page |

#### API Endpoints
| Endpoint | Method | Description |
|-----------|---------|-------------|
| `/book/api/guests/` | **GET / POST** | List or create guests |
| `/book/api/guests/<int:pk>/` | **GET / PUT / DELETE** | Retrieve, update, or delete a guest |
| `/book/api/tables/` | **GET** | List all tables |
| `/book/api/tables/<int:pk>/` | **GET** | Retrieve a table |
| `/book/api/bookings/` | **GET / POST** | List or create bookings |
| `/book/api/bookings/<int:pk>/` | **GET / PUT / DELETE** | Retrieve, update, or delete a booking |

---

### 👨‍💼 **Staff App**

#### Web Routes
| URL | View | Description |
|------|------|-------------|
| `/staff/login/` | `staff_login` | Staff login |
| `/staff/logout/` | `staff_logout` | Staff logout |
| `/staff/dashboard/` | `DashboardView` | Staff dashboard showing all bookings |
| `/staff/update/<int:booking_id>/` | `BookingStatusUpdateView` | Update booking status |

#### API Endpoints
| Endpoint | Method | Description |
|-----------|---------|-------------|
| `/staff/api/staff/` | **GET / POST** | List or create staff profiles |
| `/staff/api/staff/<int:pk>/` | **GET / PUT / DELETE** | Retrieve or modify a staff profile |
| `/staff/api/auth/login/` | **POST** | Login via API |
| `/staff/api/auth/logout/` | **POST** | Logout via API |

---
Project Strucure

BooknDine/
├── BooknDine/
├── book/
├── staff/
├──.gitignore
├── manage.py
└── README.md

API tests
POST- http://127.0.0.1:8000/book/api/guests/
{
    "name": "name",
    "email": "name@gmail.com",
    "phone_number": "00000010"

}

POST- http://127.0.0.1:8000/book/api/bookings/
add booking
{
    "guest": given guest id,
    "table": 2,
    "num_people": 4,
    "start_time": "19:00:00",
    "end_time": "21:00:00",
    "status": "PENDING"
}

POST- http://127.0.0.1:8000/staff/api/token/
login
{
   "username": "name",
   "password": "password"
}

GET- http://127.0.0.1:8000/staff/api/bookings/- view bookings

PATCH- http://127.0.0.1:8000/staff/api/bookings/booking-id/update-status/
update status
{
  "status": "confirmed/cancelled/pending"
}




🚀 Future Enhancements

📧 Email and SMS booking confirmations

📊 Analytics dashboard for reservations and occupancy

💳 Payment and deposit integration

🔐 JWT authentication for API access

📱 Mobile client app integration


👩‍💻 Author

Anne Mutahi
Role: Tech
📍 Nairobi, Kenya
