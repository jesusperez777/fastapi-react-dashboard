# app/seed_items.py

from app.core.db import SessionLocal, Base
from app.models import Item  # Cambia 'Item' por tu modelo real si es diferente

# Crear la sesión de la base de datos
db = SessionLocal()

# Función para crear items de prueba
def seed_items():
    try:
        # Lista de items de ejemplo
        items = [
            Item(name="Item de prueba 1", description="Descripción del item 1"),
            Item(name="Item de prueba 2", description="Descripción del item 2"),
            Item(name="Item de prueba 3", description="Descripción del item 3"),
        ]

        for item in items:
            db.add(item)

        db.commit()
        print("✅ Items de prueba insertados correctamente")

    except Exception as e:
        print(f"❌ Error al insertar items: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_items()
