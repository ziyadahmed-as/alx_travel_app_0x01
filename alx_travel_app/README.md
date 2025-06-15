# 🌍 ALX Travel App – 0x01

## 🚀 Project Overview same explanation 
The **ALX Travel App** is a Django-based travel booking platform designed to simulate a real-world travel system. It enables users to explore travel listings, make bookings, and share reviews. This project is part of the ALX Software Engineering curriculum and showcases best practices in API design, database modeling, and data seeding via custom management commands.

---

## ✨ Key Features

- 🏨 **Listings**: Destinations with detailed descriptions, prices, and locations.
- 📆 **Bookings**: Customers can book listings for selected dates.
- ⭐ **Reviews**: Users can leave feedback and ratings for listings.
- 🛠️ **Seeding Tool**: Includes a custom management command to seed the database with sample data.

---

## 🛠️ Tech Stack

- **Framework**: Django (Python)
- **Database**: SQLite (for development)
- **Serialization**: Django REST Framework
- **Seeding**: Custom Django management commands

---

## 📦 Project Structure

```plaintext
alx_travel_app/
│
├── alx_travel_app/        # Django project settings
├── listings/              # Core app: models, views, serializers
│   └── management/command/seed.py       # Custom command: seed.py
├── manage.py
└── Readme.md
