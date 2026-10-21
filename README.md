# Cresly Menú Digital

Menú digital web de **Cresly Pizzería** (Cuenca, Ecuador), **en producción** y usado por los clientes para consultar productos, precios y promociones desde el celular.

**Demo en vivo:** [web-production-af4e4.up.railway.app](https://web-production-af4e4.up.railway.app/)

## Funcionalidades

- Menú organizado por categorías: Pizzas, Alitas, Mega Combos, Hamburguesas, Bebidas, Para Compartir, Para Picar y Combos al Instante.
- Navegación rápida entre categorías y buscador de productos.
- Precios por tamaño (pizza pequeña, mediana, familiar y por porción) y por cantidad (alitas de 4 a 30 unidades).
- Selector de sabores de pizza y salsas para alitas.
- Banners de promociones (2x1, fin de semana, temporada).
- Diseño responsive pensado para móvil, con identidad visual de la marca (logo y tipografía propia).
- Carga inicial de datos del menú y sabores mediante scripts (`load_data.py`, `load_flavors.py`).
- [Panel de administración para editar productos y precios — confirmar si aplica]

## Stack tecnológico

| Capa | Tecnologías |
| --- | --- |
| Backend | Python 3.12 · Django |
| Frontend | HTML · CSS · JavaScript · plantillas de Django |
| Base de datos | SQLite en desarrollo · [base de datos de producción — confirmar] |
| Archivos | Estáticos (`/static/`) e imágenes de productos (`/media/`) |
| Despliegue | Railway |

## Estructura del proyecto

```
MenuDigital/
├── cresly_pizzeria/
│   ├── core/          # Configuración del proyecto (settings, urls, asgi, wsgi)
│   ├── menu/          # App del menú: categorías, productos y sabores
│   ├── templates/     # Plantillas HTML
│   ├── static/        # CSS, JS, fuentes e imágenes de marca
│   └── media/         # Imágenes de productos
├── load_data.py       # Carga inicial del menú
├── load_flavors.py    # Carga de sabores
├── manage.py
├── requirements.txt
├── Procfile
└── railway.toml
```

## Instalación local

```bash
git clone https://github.com/JimmyCoro/cresly-menu.git
cd cresly-menu
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

python manage.py migrate
python load_data.py
python load_flavors.py
python manage.py runserver
```

Abre `http://127.0.0.1:8000/` en el navegador.

## Capturas

<!-- Agrega aquí capturas del menú en móvil, una categoría y el selector de sabores -->

## Autor

**Jimmy Coro** — Tecnólogo en Desarrollo de Software
[github.com/JimmyCoro](https://github.com/JimmyCoro)

Desarrollado con apoyo de herramientas de IA (Claude Code).
