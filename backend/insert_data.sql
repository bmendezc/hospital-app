-- 1. Users Table (Test Account)
INSERT INTO users (id, username, password_hash) VALUES
(1, 'testuser', 'placeholder_hash_for_testuser_password123_');

-- 2. Departments Table (10 Rows)
INSERT INTO departments (department_id, department_name, department_location) VALUES
(1, 'Cardiology', 'Tower A, Floor 5'),
(2, 'Neurology', 'Tower B, Floor 2'),
(3, 'Pediatrics', 'Tower A, Floor 1'),
(4, 'Orthopedics', 'Tower B, Floor 4'),
(5, 'Radiology', 'Main Floor'),
(6, 'Oncology', 'Tower C, Floor 6'),
(7, 'General Surgery', 'Tower B, Floor 3'),
(8, 'Dermatology', 'Tower A, Floor 2'),
(9, 'Emergency', 'Main Floor'),
(10, 'Pharmacy', 'Main Floor');

-- 3. Staff Information Table (15 Rows)
INSERT INTO staff_information (employee_id, employee_first_name, employee_last_name, staff_role, department_id) VALUES
(1, 'Alice', 'Smith', 'Cardiologist', 1),
(2, 'Bob', 'Jones', 'Neurosurgeon', 2),
(3, 'Charlie', 'Brown', 'Pediatrician', 3),
(4, 'Diana', 'Prince', 'Orthopedic Surgeon', 4),
(5, 'Ethan', 'Hunt', 'Radiology Technician', 5),
(6, 'Fiona', 'Gale', 'Oncologist', 6),
(7, 'George', 'Clark', 'General Surgeon', 7),
(8, 'Hannah', 'Scott', 'Dermatologist', 8),
(9, 'Ivan', 'Drago', 'ER Physician', 9),
(10, 'Jenna', 'Kare', 'Pharmacist', 10),
(11, 'Kyle', 'Reese', 'Nurse', 1),
(12, 'Laura', 'Palmer', 'Nurse', 3),
(13, 'Mike', 'Tyson', 'Admin Assistant', 10),
(14, 'Olivia', 'Benson', 'Surgeon', 7),
(15, 'Peter', 'Parker', 'Resident', 2);


-- 4. Patient information Table (12 Rows)
INSERT INTO patient_information (patient_id, patient_first_name, patient_last_name, patient_phone_number, patient_DOB, patient_email) VALUES
(1, 'Sam', 'Vance', '555-1001', '1985-04-12', 'sam.vance@example.com'),
(2, 'Jane', 'Doe', '555-1002', '1990-11-20', 'jane.doe@example.com'),
(3, 'John', 'Smith', '555-1003', '1975-01-05', 'john.smith@example.com'),
(4, 'Mary', 'Queen', '555-1004', '2010-08-15', 'mary.queen@example.com'),
(5, 'David', 'Lee', '555-1005', '1962-03-22', 'david.lee@example.com'),
(6, 'Lisa', 'Ray', '555-1006', '1995-07-30', 'lisa.ray@example.com'),
(7, 'Tom', 'Hanks', '555-1007', '1956-06-09', 'tom.hanks@example.com'),
(8, 'Sarah', 'Connor', '555-1008', '1980-12-04', 'sarah.c@example.com'),
(9, 'Alex', 'Jones', '555-1009', '1970-02-18', 'alex.jones@example.com'),
(10, 'Betty', 'White', '555-1010', '1922-01-17', 'betty.w@example.com'),
(11, 'Chris', 'Pine', '555-1011', '1980-08-26', 'chris.p@example.com'),
(12, 'Emily', 'Blunt', '555-1012', '1983-02-23', 'emily.b@example.com');

-- 5. Appointments Table (15 Rows)
INSERT INTO appointments (appointment_id, date, time, description, patients_id, employee_id) VALUES
(1, '2025-11-15', '10:00', 'Routine check-up', 3, 1),
(2, '2025-11-17', '14:30', 'Follow up on neurological scan', 7, 2),
(3, '2025-11-18', '09:00', 'Vaccination', 4, 3),
(4, '2025-11-19', '11:00', 'Knee injury consultation', 1, 4),
(5, '2025-11-16', '16:00', 'X-ray of chest', 10, 5),
(6, '2025-11-20', '13:00', 'Chemotherapy session', 6, 6),
(7, '2025-11-15', '15:00', 'Pre-op consultation', 11, 7),
(8, '2025-11-17', '10:30', 'Skin rash examination', 2, 8),
(9, '2025-11-18', '12:00', 'Emergency triage', 9, 9),
(10, '2025-11-19', '14:00', 'Medication review', 5, 10),
(11, '2025-11-20', '10:00', 'Cardiology consult', 12, 11),
(12, '2025-11-15', '11:30', 'Pediatric examination', 8, 12),
(13, '2025-11-16', '13:30', 'Surgery follow-up', 3, 14),
(14, '2025-11-17', '15:30', 'Neurology testing', 1, 15),
(15, '2025-11-18', '16:30', 'General check-up', 7, 1);

-- 6. Transactions Table (12 Rows)
INSERT INTO transactions (transaction_id, payment_method, amount, transaction_date, patient_id) VALUES
(1, 'Credit Card', 150.75, '2025-10-25', 1),
(2, 'Insurance', 300.00, '2025-11-01', 2),
(3, 'Cash', 50.00, '2025-11-10', 3),
(4, 'E-Transfer', 450.50, '2025-11-12', 4),
(5, 'Credit Card', 220.00, '2025-11-14', 5),
(6, 'Insurance', 180.25, '2025-11-05', 6),
(7, 'Cash', 75.00, '2025-10-30', 7),
(8, 'Credit Card', 345.99, '2025-11-11', 8),
(9, 'E-Transfer', 100.00, '2025-11-08', 9),
(10, 'Insurance', 490.10, '2025-11-15', 10),
(11, 'Credit Card', 125.50, '2025-11-03', 11),
(12, 'Cash', 370.00, '2025-10-20', 12);