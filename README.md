🍽️ BooknDine — Restaurant Booking System

BooknDine is a Django-based restaurant booking system that allows guests to make reservations online and enables staff to manage them efficiently.
Guests can submit their booking details including name, table position, and number of people.
Staff members can view all reservations, update their status, or cancel them through an intuitive admin or management interface.

⚙️ Core Features
✅ Guest Booking — Guests can make table reservations by filling in their details.
✅ Table Management — Each reservation is linked to a specific table position.
✅ Capacity Tracking — Number of people per reservation is stored for planning.
✅ Staff Controls — Staff can approve, update, or cancel reservations.
✅ CRUD Operations — Create, view, edit, and delete reservations.

🧠 Tech Stack
Component	Technology
Framework	Django 5.2.5
Language	Python 3.13
Frontend	HTML, CSS, Bootstrap
Database	MySQL
Server	Django Development Server

Access the app
🌐 Guest interface → http://127.0.0.1:8000/guests/
🔐 Admin interface → http://127.0.0.1:8000/admin/

🧩 URL Patterns
URL	View	Purpose
/guests/	GuestListView	List all reservations
/guests/add/	GuestCreateView	Make a new reservation
/guests/<int:pk>/	GuestDetailView	View reservation details
/guests/<int:pk>/edit/	GuestUpdateView	Edit reservation status/details
/guests/<int:pk>/delete/	GuestDeleteView	Cancel or remove a reservation
🧱 Project Structure
BooknDine/
│
├── Book/                      # Main app
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   ├── guest_list.html
│   │   ├── guest_detail.html
│   │   ├── guest_form.html
│   │   └── guest_confirm_delete.html
│   ├── models.py              # Reservation & guest models
│   ├── views.py               # Class-based views
│   ├── urls.py                # App-level routes
│   └── admin.py               # Staff admin management
│
├── BooknDine/                 # Project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py

🧰 Future Enhancements

📧 Add email or SMS booking confirmations

📊 Integrate analytics dashboard for restaurant occupancy

💳 Enable payment or deposit options for reservations


👩‍💻 Author

Anne Mutahi
Role: Tech
📍 Nairobi, Kenya