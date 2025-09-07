from app.db.session import SessionLocal
from app.models.item import Item
from app.models.user import User
from app.core.security import get_password_hash

def create_seed_data():
    db = SessionLocal()

    # Crear un usuario de prueba
    user = User(
        email="user@example.com",
        full_name="Usuario Ejemplo",
        hashed_password=get_password_hash("password"),
        is_active=True
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    # Crear items de prueba
    items = [
        Item(title="Item 1", description="Descripción del Item 1", owner_id=user.id),
        Item(title="Item 2", description="Descripción del Item 2", owner_id=user.id),
        Item(title="Item 3", description="Descripción del Item 3", owner_id=user.id)
    ]

    db.add_all(items)
    db.commit()
    db.close()
    print("Seed data creada exitosamente")

if __name__ == "__main__":
    create_seed_data()
