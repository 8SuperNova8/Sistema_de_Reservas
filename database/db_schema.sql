
-- ==================================================
-- CREACIÓN DE TABLAS PARA SISTEMA DE RESERVAS 
-- ==================================================


-- ENUM TYPES
CREATE TYPE payment_method_enum AS ENUM ('cash', 'card', 'transfer');
CREATE TYPE payment_status_enum AS ENUM ('pending', 'completed', 'failed');
CREATE TYPE reservation_status_enum AS ENUM ('confirmed', 'checked_in', 'cancelled', 'no_show', 'finished');
CREATE TYPE room_status_enum AS ENUM ('active', 'maintenance', 'inactive');


-- ==============================
-- TABLE: room_types
-- ==============================
CREATE TABLE room_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    base_price NUMERIC(10,2) NOT NULL
);


-- ==============================
-- TABLE: rooms
-- ==============================
CREATE TABLE rooms (
    id SERIAL PRIMARY KEY,
    room_number INT NOT NULL UNIQUE,
    floor INT NOT NULL,
    status room_status_enum NOT NULL DEFAULT 'active',
    room_type_id INT NOT NULL,
    CONSTRAINT rooms_room_type_fk
        FOREIGN KEY (room_type_id)
        REFERENCES room_types(id)
        ON DELETE RESTRICT
);

-- INDEX for FK
CREATE INDEX idx_rooms_room_type_id ON rooms(room_type_id);


-- ==============================
-- TABLE: reservations
-- ==============================
CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE reservations (
    id SERIAL PRIMARY KEY,
    room_id INT NOT NULL,
    check_in DATE NOT NULL,
    check_out DATE NOT NULL,
    reservation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status reservation_status_enum NOT NULL DEFAULT 'confirmed',
    total_amount NUMERIC(10,2) NOT NULL,
    guest_name VARCHAR(100) NOT NULL,
    guest_email VARCHAR(100) NOT NULL,
    guest_phone VARCHAR(20) NOT NULL,
    guest_document VARCHAR(50) NOT NULL,

    token UUID NOT NULL DEFAULT gen_random_uuid(),

    extra_charges NUMERIC(10,2) DEFAULT 0.00,

    CONSTRAINT uq_reservation UNIQUE (room_id, check_in, check_out),

    CONSTRAINT reservations_room_fk
        FOREIGN KEY (room_id)
        REFERENCES rooms(id)
        ON DELETE RESTRICT
);

-- INDEX for FK
CREATE INDEX idx_reservations_room_id ON reservations(room_id);


-- ==============================
-- TABLE: payments
-- ==============================
CREATE TABLE payments (
    id SERIAL PRIMARY KEY,
    reservation_id INT NOT NULL,
    amount NUMERIC(10,2) NOT NULL,
    payment_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    payment_method payment_method_enum NOT NULL,
    status payment_status_enum NOT NULL DEFAULT 'completed',

    CONSTRAINT payments_reservation_fk
        FOREIGN KEY (reservation_id)
        REFERENCES reservations(id)
        ON DELETE RESTRICT
);

-- INDEX for FK
CREATE INDEX idx_payments_reservation_id ON payments(reservation_id);


