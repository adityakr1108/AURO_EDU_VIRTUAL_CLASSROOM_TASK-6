
# 🎓 Virtual Classroom Platform

A web-based virtual classroom built with **Django**, **WebRTC**, and **Django Channels**. This platform allows teachers and students to interact in real-time with:

- 📹 Video Conferencing
- 💬 Live Chat
- 🧑‍🏫 Role-based Dashboards (Teacher & Student)
- ✅ Attendance & Classroom Management
- 📝 Collaborative Features (Whiteboard, File Sharing — coming soon)

---

## 🚀 Features

### 👩‍🏫 Teacher
- Create classrooms
- Start video calls
- Manage students

### 👨‍🎓 Student
- Join classrooms
- Participate in video sessions
- Interact via real-time chat

---

## 🛠️ Tech Stack

- **Backend**: Django, Django Channels, Redis
- **Frontend**: HTML5, CSS3, JavaScript
- **WebRTC**: For peer-to-peer video communication
- **WebSockets**: For real-time communication

---

## ⚙️ Installation

### 1. Clone the repo
```bash
git clone https://github.com/your-username/virtual-classroom.git
cd virtual-classroom
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Start Redis (required for Django Channels)
Make sure Redis is installed and run:
```bash
redis-server
```

### 5. Apply migrations
```bash
python manage.py migrate
```

### 6. Run the server
```bash
python manage.py runserver
```

---

## 📂 Project Structure

```
virtual_classroom/
│
├── accounts/         # User management (signup, login, dashboard)
├── chat/             # WebSocket consumers and chat logic
├── video/            # Video chat (WebRTC)
├── templates/        # HTML templates
├── static/           # CSS/JS files (optional)
├── db.sqlite3        # Default DB
└── manage.py         # Django management script
```

---

## ✍️ Author

- **Your Name** – [@yourhandle](https://github.com/your-username)

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
