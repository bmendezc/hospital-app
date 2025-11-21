-- 1. users Table (For Authentication)
CREATE TABLE users (
    id INTEGER NOT NULL, 
    username VARCHAR(80) NOT NULL, 
    password_hash VARCHAR(128) NOT NULL, 
    PRIMARY KEY (id), 
    UNIQUE (username)
);

-- 2. departments Table
CREATE TABLE departments (
    department_id INTEGER NOT NULL, 
    department_name VARCHAR(100) NOT NULL, 
    department_location VARCHAR(100) NOT NULL, 
    PRIMARY KEY (department_id), 
    UNIQUE (department_name)
);

-- 3. staff_information Table
CREATE TABLE staff_information (
    employee_id INTEGER NOT NULL, 
    employee_first_name VARCHAR(50) NOT NULL, 
    employee_last_name VARCHAR(50) NOT NULL, 
    staff_role VARCHAR(50) NOT NULL, 
    department_id INTEGER NOT NULL, 
    PRIMARY KEY (employee_id), 
    FOREIGN KEY(department_id) REFERENCES departments (department_id)
);

-- 4. patient_information Table
CREATE TABLE patient_information (
    patient_id INTEGER NOT NULL, 
    patient_first_name VARCHAR(50) NOT NULL, 
    patient_last_name VARCHAR(50) NOT NULL, 
    patient_phone_number VARCHAR(15), 
    patient_DOB VARCHAR(10), 
    patient_email VARCHAR(100), 
    PRIMARY KEY (patient_id), 
    UNIQUE (patient_email)
);

-- 5. appointments Table
CREATE TABLE appointments (
    appointment_id INTEGER NOT NULL, 
    date VARCHAR(10) NOT NULL, 
    time VARCHAR(5) NOT NULL, 
    description TEXT, 
    patients_id INTEGER NOT NULL, 
    employee_id INTEGER NOT NULL, 
    PRIMARY KEY (appointment_id), 
    FOREIGN KEY(patients_id) REFERENCES patient_information (patient_id), 
    FOREIGN KEY(employee_id) REFERENCES staff_information (employee_id)
);

-- 6. transactions Table
CREATE TABLE transactions (
    transaction_id INTEGER NOT NULL, 
    payment_method VARCHAR(50) NOT NULL, 
    amount FLOAT NOT NULL, 
    transaction_date VARCHAR(10) NOT NULL, 
    patient_id INTEGER NOT NULL, 
    PRIMARY KEY (transaction_id), 
    FOREIGN KEY(patient_id) REFERENCES patient_information (patient_id)
);