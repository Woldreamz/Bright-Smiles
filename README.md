# Dental Management Platform

This project is a Dental Management Platform built for **Bright Smile Dental Systems**. The platform allows administrative employees to manage clinics, doctors, and patients across multiple locations in the United States. Users can manage key aspects such as scheduling appointments, tracking visits, and editing details for clinics, doctors, and patients.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
  - [Clinics Management](#clinics-management)
  - [Doctors Management](#doctors-management)
  - [Patients Management](#patients-management)
- [Technology Stack](#technology-stack)
- [REST API Endpoints](#rest-api-endpoints)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Testing](#testing)
- [Project Deliverables](#project-deliverables)
- [Assumptions](#assumptions)

## Project Overview
The Dental Management Platform provides an intuitive interface for managing:
- Clinics
- Doctors
- Patients

The platform is built with Django for the backend and frontend, utilizing PostgreSQL for database management.

## Features
### Clinics Management
- **Clinics List**: Displays clinic details including name, phone, location, and counts of affiliated doctors and patients.
- **Clinic Detail Page**: 
  - Edit clinic information (name, address, phone, email).
  - List and manage affiliated doctors, including office address and schedule.

### Doctors Management
- **Doctors List**: Displays doctor details such as NPI, name, specialties, and affiliations with clinics and patients.
- **Doctor Detail Page**:
  - Edit doctor information (NPI, name, email, phone, specialties).
  - View affiliations with clinics and patients.

### Patients Management
- **Patients List**: Displays patient details including name, date of birth, visit history, and upcoming appointments.
- **Patient Detail Page**:
  - Edit patient information (name, address, phone, date of birth, SSN, gender).
  - List visit history and schedule new visits.
  - Manage upcoming appointments, including selection of procedure, clinic, doctor, and time slot.

### Predefined Procedures
- Supported procedures: Cleaning, Filling, Root Canal, Crown, Teeth Whitening.

## Technology Stack
- **Backend**: Django
- **Frontend**: HTML, Bootstrap, JavaScript
- **Database**: PostgreSQL

## REST API Endpoints
The platform includes REST APIs for:
- Adding a patient, doctor, or clinic.
- Retrieving clinic information (excluding affiliations).

## Setup Instructions
1. **Clone the repository**:
   ```bash
   git clone <repository-link>
   cd <repository-directory>
   ```

2. **Set up virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Database setup**:
   - Configure PostgreSQL and set the credentials in `settings.py`.
   - Run migrations:
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     python manage.py collectstatic
     ```

5. **Run the server**:
   ```bash
   python manage.py runserver
   ```
## BaseUrl
- localhost

## Usage
- **Login**: Users log in with an email and password (using Django’s admin features).
- **Navigation**: Access tabs for Clinics, Doctors, and Patients to manage each category.
- **Scheduling**: Follow a structured workflow to schedule appointments with procedure, clinic, and doctor selections.

## Testing
Unit tests are included for critical functionalities. Run tests with:
```bash
python manage.py test
```
### Endpoints Available
#### - /patients/add/<br />
      method: GET, POST
      body: {name:'', d_o_b:'', address:'', gender:'', ssn_last_4:'', phone_number:''}
      response: {}
      description: add patient record 
#### - /doctors/add/<br />
      method: GET, POST
      body: {npi:'', name:'', email:'', phone_number:'', office_address:'', specialties:''}
      response: {}
      description: add doctor record 
#### - /clinics/add/<br />
      method: GET, POST
      body: {name:'', phone_number:'', city:'', state:''}
      response: {}
      description: register clinic
#### - /clinics/view/<br />
      method: GET
      body: none 
      response: {}
      description: view registered clinics 
  

## Project Deliverables
- Functional prototype with main features and REST API.
- Unit tests for critical features.
- Documentation (README) with setup and usage instructions.

## Assumptions
The project assumes:
- Clinics have doctors affiliated with them, who in turn have patients assigned.
- Appointments are scheduled only within available doctor time slots.

---

This README should provide clear instructions and insights for setting up, using, and understanding the project’s functionalities. Let me know if there’s anything more specific you'd like to include!  
