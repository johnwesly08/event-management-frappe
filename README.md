````markdown
# Event Management Web Application (Frappe)

This project is a simple Event Management web application built using the **Frappe Framework**.
It allows event planners to manage events, attendees, and ticket sales efficiently.

This application was developed as part of a full-stack evaluation task.

---

## Features Implemented

### Event Management
- Create, update, and delete events
- Fields included:
  - Event Title
  - Description
  - Event Date
  - Location
  - Capacity
- Search and filter events using Frappe list views

### Attendee Management
- Register attendees for events
- Update attendee details
- View attendees mapped to each event
- Server-side validation to prevent exceeding event capacity

### Ticket Sales
- Create ticket sales linked to events and attendees
- Prevent duplicate ticket sales for the same attendee
- Track remaining ticket availability automatically
- Calculate ticket availability based on capacity and sales

### Reports
- **Ticket Sales Summary Report**
  - Total tickets sold per event
  - Revenue per event (fixed ticket price assumption)

### CSV Import
- Event records can be imported from CSV files
- Implemented using server-side Python logic as allowed in the requirements

---

## Tech Stack

- **Framework**: Frappe Framework
- **Backend**: Python (Frappe ORM, Server Scripts)
- **Database**: MariaDB
- **Frontend**: Frappe Desk UI
- **Others**: Redis

---

## Project Setup

```bash
bench get-app event_management
bench --site mysite.local install-app event_management
bench start
````

Access the application at:

```
http://127.0.0.1:8000/desk
```

---

## CSV Import Format

```csv
Event Title,Description,Event Date,Location,Capacity
Event A,Test event A,2026-02-01,Chennai,50
Event B,Test event B,2026-02-10,Bangalore,100
```

---

## Screenshots



* Event creation
* Attendee list
* Ticket tracking
* CSV import result

---

## Notes

* User roles and permissions were kept minimal as specified
* All critical validations are handled server-side
* No additional frontend frameworks were used



# 2️⃣ SCREENSHOTS


### 📸 Required screenshots:

1. **Event creation**
<img width="1919" height="1077" alt="image" src="https://github.com/user-attachments/assets/84bb92ab-413d-40d8-b6d6-4e51d571e71e" />
<img width="1916" height="1018" alt="image" src="https://github.com/user-attachments/assets/6f21b29f-8589-48a5-8b7b-5c1591bb64e7" />
   * Event form with title, date, location, capacity
  
2. **Attendee list**
<img width="1917" height="1079" alt="image" src="https://github.com/user-attachments/assets/27e1e7a3-4a4f-4c1a-9cdb-09621cdbf5b1" />
<img width="1917" height="1079" alt="image" src="https://github.com/user-attachments/assets/5a30c558-c9fb-4a33-b346-a88bf6f29050" />
   * Attendees linked to an event
     
3. **Ticket tracking**
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/8ac3e887-ae89-4e99-9564-b7e9efb2cf97" />
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/b558f2b2-7cbd-4f3f-8095-9311ff752649" />
   * Ticket Sale entry + updated availability
    
4. **CSV import**
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/44197172-1e5f-41ba-8319-62a554403d39" />
   * Imported events visible in list view

