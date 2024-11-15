### Charity Platform | پلتفرم خیریه

---

#### **Project Purpose | هدف پروژه**
This project aims to create an online platform to connect charity organizations with philanthropists. Its primary goal is to facilitate the process of connecting donors with people in need, especially for non-monetary requirements that demand specific skills or expertise.

هدف از این پروژه، ایجاد بستری اینترنتی برای برقراری ارتباط بین مراکز خیریه و نیکوکاران است. این سامانه با هدف تسهیل فرایند کمک‌رسانی، به ویژه در نیازمندی‌های غیر نقدی که به مهارت یا تخصص خاص نیاز دارند، طراحی شده است.

For example, tasks like caring for the elderly, volunteering as a teacher in underprivileged areas, or providing specialized skills are some of the non-monetary needs this platform addresses.

به عنوان مثال، نگهداری از سالمندان، تدریس داوطلبانه در مناطق محروم یا انجام فعالیت‌هایی که به تخصص خاص نیاز دارند، از جمله مواردی هستند که این سامانه به آن‌ها می‌پردازد.

---

#### **Features and Mechanism | ویژگی‌ها و مکانیزم کلی**

1. **Charity Projects Defined by Organizations | تعریف پروژه‌ها توسط موسسات خیریه:**
   - Organizations can define their needs as specific projects.
   - Projects include details about requirements, timelines, and conditions.

   موسسات خیریه می‌توانند نیازهای خود را به صورت پروژه تعریف کنند که شامل جزئیات، زمان‌بندی و شرایط است.

2. **Search and Apply by Philanthropists | جستجو و انتخاب توسط نیکوکاران:**
   - Philanthropists can search and apply for projects that align with their skills and time availability.
   - امکان جستجو و ارسال درخواست برای پروژه‌های متناسب با توانایی و زمان افراد وجود دارد.

3. **Request Review by Organizations | بررسی درخواست‌ها توسط موسسات:**
   - Organizations can accept or reject applications based on the philanthropist’s qualifications.
   - موسسات خیریه می‌توانند درخواست‌ها را بررسی و براساس شرایط نیکوکار، آن را رد یا قبول کنند.

4. **Project Management | مدیریت پروژه‌ها:**
   - Organizations can mark projects as completed when needs are fulfilled.
   - موسسات می‌توانند وضعیت پروژه را به حالت تمام‌شده تغییر دهند.

5. **User Features | امکانات کاربران:**
   - **Charity Organizations | موسسات خیریه**: Define and manage projects.
   - **Philanthropists | نیکوکاران**: Apply for volunteering opportunities.

---

#### **Educational Context | زمینه آموزشی**
This project is a practice assignment developed during the **Django course at Quera College**. The goal was to learn Django concepts and implement a real-world web application.

این پروژه به عنوان یک تمرین آموزشی در دوره **جنگو کالج کوئرا** انجام شده است. هدف این تمرین، یادگیری مفاهیم جنگو و پیاده‌سازی یک سامانه وب واقعی بوده است.

---

#### **Installation and Execution | نصب و اجرای پروژه**

##### **Requirements | پیش‌نیازها**
- **Frontend**:
  - Node.js
  - React
- **Backend**:
  - Python
  - Django
- **Database**: SQLite (Default) or any Django-compatible database.

---

##### **Steps | مراحل اجرا**

1. **Clone the repository | کلون کردن مخزن:**
   ```bash
   git clone https://github.com/fazeleardestani/charity.git
   cd charity
   ```

2. **Run Backend | اجرای بخش Backend:**
   - Navigate to the `backend` folder:
     ```bash
     cd backend
     ```
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Start Django server:
     ```bash
     python manage.py migrate
     python manage.py runserver
     ```

3. **Run Frontend | اجرای بخش Frontend:**
   - Navigate to the `frontend` folder:
     ```bash
     cd ../frontend
     ```
   - Install dependencies:
     ```bash
     npm install
     ```
   - Start the application:
     ```bash
     npm start
     ```

4. **Access Outputs | مشاهده خروجی:**
   - **Frontend**: [http://localhost:3000](http://localhost:3000)
   - **Backend**: [http://localhost:8000](http://localhost:8000)

---

#### **Project Structure | ساختار پوشه‌ها**
```
charity/
├── backend/        # Server-side code (Django) | کدهای سمت سرور
│   ├── manage.py
│   ├── charity_app/
│   └── ...
├── frontend/       # Client-side code (React) | کدهای سمت کلاینت
│   ├── src/
│   ├── package.json
│   └── ...
└── README.md       # راهنما
```

---

#### **Developer | توسعه‌دهنده**
- **Name | نام**: Fazele Ardestani | فاضله اردستانی
- **Email | ایمیل**: [Insert Your Email]

---

This project is a practical learning exercise, designed to systematize and facilitate the process of connecting charities with philanthropists.  
این پروژه به منظور تمرین و یادگیری مفاهیم جنگو طراحی شده و فرایند مدیریت نیازمندی‌های خیریه را تسهیل می‌کند.