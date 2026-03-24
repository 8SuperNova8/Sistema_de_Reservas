# Sistema de Reservas (API Backend en desarrollo)

Proyecto backend desarrollado con Django REST Framework enfocado en la gestión de reservas, con énfasis en lógica de negocio, control de acceso y seguridad de endpoints.

## Estado
En desarrollo activo. Actualmente se están implementando endpoints principales y validaciones de negocio.

## Funcionalidades actuales
- Estructura base del proyecto
- Modelado de base de datos relacional
- Endpoints para consulta de disponibilidad y creación de reservas
- Control de estados de reserva (confirmed, cancelled, no_show, checked_in, finished) con validación de transiciones según reglas de negocio
- Restricción de acciones según reglas de negocio
- Implementación de rate limiting para protección de endpoints

## En proceso
- Sistema de autenticación con JWT (administrador)
- Gestión de roles (admin / público)
- Envío de notificaciones

## Tecnologías
- Python
- Django
- Django REST Framework
- MySQL 