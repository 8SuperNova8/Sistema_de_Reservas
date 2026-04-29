-- ==========================================
-- INGRESO DE DATOS
-- ==========================================

-- Datos room_types
INSERT INTO room_types (id, name, description, base_price)
VALUES
    (1, 'Estándar', 'Perfecta para viajeros individuales o parejas que buscan comodidad a un precio accesible.', 130000.00),
    (2, 'Ejecutiva', 'Espacio amplio con áreas separadas para trabajar y descansar, ideal para viajes de negocios.', 220000.00),
    (3, 'Penthouse Premier', 'La máxima experiencia de lujo con espacios exclusivos y servicios personalizados', 450000.00);
SELECT setval(pg_get_serial_sequence('room_types','id'), (SELECT MAX(id) FROM room_types));

-- datos para la tabla rooms
INSERT INTO rooms (id, room_number, floor, status, room_type_id)
VALUES
    (1, 201, 2, 'active', 1),
    (2, 202, 2, 'active', 1),
    (3, 203, 2, 'active', 1),
    (4, 204, 2, 'active', 2),
    (5, 205, 2, 'active', 2),
    (6, 301, 3, 'active', 1),
    (7, 302, 3, 'maintenance', 1),
    (8, 303, 3, 'maintenance', 1),
    (9, 304, 3, 'active', 2),
    (10, 305, 3, 'active', 2),
    (11, 401, 4, 'inactive', 2),
    (12, 402, 4, 'inactive', 3),
    (13, 403, 4, 'active', 3),
    (14, 601, 5, 'active', 3),
    (15, 501, 5, 'active', 3),
    (16, 502, 5, 'active', 3);

SELECT setval(pg_get_serial_sequence('rooms','id'), (SELECT MAX(id) FROM rooms));

-- Datos para la tabla reservations
INSERT INTO public.reservations(
	id, room_id, check_in, check_out, reservation_date, status, total_amount, guest_name, guest_email, guest_phone, guest_document, token, extra_charges)
	VALUES (1, 4, '2026-03-10', '2026-03-11', '2026-03-09 21:34:30', 'confirmed', 120000.00, 'veronica', 'vero@mail.com', '1111', '101010', 'ddd72ab3259211f19c3b00090ffe0001', 0.00),
    (2, 15, '2026-03-28', '2026-04-03', '2026-03-10 04:22:03', 'confirmed', 1350000.00, 'leidy', 'lei@mail.com', '3333', '303030', 'ddd759f8259211f19c3b00090ffe0001', 0.00),
    (3, 15, '2026-04-03', '2026-04-05', '2026-03-14 04:21:21', 'confirmed', 1800000.00, 'Cielo', 'cie@mail.com', '4444', '404040', 'ddd75c6b259211f19c3b00090ffe0001', 0.00),
    (4, 12, '2026-03-15', '2026-03-19', '2026-03-22 01:37:46', 'confirmed', 880000.00, 'Alex', 'alex@mail.com', '5555', '505050', 'ddd75e58-2592-11f1-9c3b-00090ffe0001', 0.00),
    (5, 9, '2026-04-02', '2026-04-05', '2026-03-23 22:23:35', 'cancelled', 390000.00, 'Pedro', 'pedro@mail.com', '6666', '606060', 'c13656b0496747ac937d1b212d511e71', 0.00),
    (6, 1, '2026-04-05', '2026-04-09', '2026-03-25 22:45:27', 'confirmed', 880000.00, 'Adriana', 'adriana@mail.com', '7777', '707070', '5f07c1d7fe124900b86d7d0f5525deef', 0.00),
	(7, 15, '2026-03-29', '2026-03-31', '2026-03-10 04:19:17', 'confirmed', 900000.00, 'Laura', 'lau@mail.com', '2222', '202020', 'ddd7548b259211f19c3b00090ffe0001', 300000.00),
    (8, 3, '2026-04-11', '2026-04-15', '2026-04-11 02:50:26', 'confirmed', 520000.00, 'Laura', 'laura@mail.com', '8888', '808080', '69d8de14329848699d8b6109442fb03a', 0.00);

SELECT setval(pg_get_serial_sequence('reservations','id'), (SELECT MAX(id) FROM reservations));

-- ==============================================
-- ==============================================


-- Volcando datos para la tabla dj_infinite_harmony_hotel.accounts_user: ~3 rows (aproximadamente)
INSERT INTO accounts_user 
(id, password, last_login, is_superuser, first_name, last_name, is_active, date_joined, email, is_staff)
VALUES
(1, 'pbkdf2_sha256$1000000$ud89y7WPKa69iXeCwxrdnU$c1P9pE7CFpPzDyQa8Gl84ODzon96o0pzGNW2IqQ5KEY=', '2026-04-03 01:32:16.490288', TRUE, 'infinite', 'harmony', TRUE, '2026-04-03 01:31:35.462015', 'infinite@correo.com', TRUE),
(2, 'pbkdf2_sha256$1000000$na4o79hILr6Fy9qXokN6gu$59iuDDTwDIruw5KUVf7gVBQlIf+nXkFnlkZq7dn2OqM=', NULL, FALSE, 'Andrea', 'Pino', TRUE, '2026-04-05 04:08:00.084384', 'apino@correo.com', FALSE);

-- accounts_user_groups
INSERT INTO accounts_user_groups (id, user_id, group_id)
VALUES
    (1, 3, 1),
    (4, 2, 1);

-- auth_group
INSERT INTO auth_group (id, name) 
VALUES
	(1, 'Receptionist');

-- payments
INSERT INTO `payments` (`id`, `reservation_id`, `amount`, `payment_date`, `payment_method`, `status`) VALUES
	(1, 12, 300000.00, '2026-04-14 20:45:36', 'cash', 'completed'),
	(2, 1, 120000.00, '2026-04-21 20:12:51', 'cash', 'completed');

