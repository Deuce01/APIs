<h1 align="center">🚀 Python API Roadmap 🚀</h1>

<p align="center">
  A comprehensive journey to mastering APIs with Python! This repository documents our progress as we build various API projects, from simple to complex. Each API comes with well-structured code, project setup instructions, and examples for testing.
</p>

---

## 📖 Table of Contents

- [Introduction](#introduction)
- [Current APIs](#current-apis)
- [Installation & Setup](#installation--setup)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)

---

## 🌟 Introduction

This repository serves as a roadmap for learning and building Python APIs. We will create a variety of APIs to demonstrate best practices and practical use cases, starting with beginner-friendly projects and progressing toward more advanced topics like authentication, databases, and deployment.

## 📚 Current APIs

| API Name              | Description                             | Status        |
|-----------------------|-----------------------------------------|---------------|
| **To-Do List API**     | A basic API for managing tasks          | ✅ Completed  |
| **Weather API**        | A simple API for fetching weather data  | ✅ Completed  |

Feel free to follow along and contribute!

---

## 🛠 Installation & Setup

### Requirements

- Python 3.x
- Flask
- [OpenWeatherMap API Key](https://openweathermap.org/api) (for the Weather API)

### Steps

1. **Clone the repository**:
  

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install Flask requests
   ```

4. **Run the desired API**:
   Navigate to the folder of the API you want to run and start it.
   ```bash
   python <api_name>.py
   ```

---

## 📖 API Documentation

### **To-Do List API** (Completed ✅)

- **Description**: A basic API to manage to-do tasks (CRUD functionality).
  
#### Endpoints:

| Method | Endpoint        | Description              |
|--------|-----------------|--------------------------|
| GET    | `/tasks`        | Get all tasks            |
| POST   | `/tasks`        | Add a new task           |
| DELETE | `/tasks/<id>`   | Delete task by ID        |

---

### **Weather API** (Completed ✅)

- **Description**: A simple API that fetches the current weather data for a specified city using the OpenWeatherMap API.
  
#### Endpoints:

| Method | Endpoint                  | Description                    |
|--------|----------------------------|---------------------------------|
| GET    | `/weather?city=<city_name>` | Fetch weather data for a city   |

#### Example Usage:
- Fetch weather for Nairobi:
  ```bash
  curl "http://127.0.0.1:5000/weather?city=Nairobi"
  ```

---

## 🤝 Contributing

Contributions are welcome! If you have any suggestions, feel free to create an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -m 'Add new API feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Open a pull request.

---


---

<p align="center">
  Made with ❤️ by Victor Chege.
</p>

