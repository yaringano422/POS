# Sistema POS (Punto de Venta)

Este proyecto es un sistema de Punto de Venta (POS) diseñado para manejar inventarios, ventas y reportes. Está desarrollado en Python y utiliza una base de datos relacional para la sincronización entre múltiples computadoras.

## Características
- Gestión de inventario con categorías.
- Registro de ventas por usuario.
- Reportes por vendedor y administrador.
- Sincronización en tiempo real usando una base de datos centralizada.
- Búsquedas insensibles a mayúsculas/minúsculas.

## Requisitos
- Python 3.8 o superior.
- PostgreSQL o MySQL (configuración en `config.py`).
- Paquetes de Python (ver `requirements.txt`).

## Instalación
1. Clona el repositorio:
   ```bash
   git clone https://github.com/yaringano422/POS.git
   cd POS