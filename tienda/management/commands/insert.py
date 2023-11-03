import random
from django.core.management.base import BaseCommand
from faker import Faker
from tienda.models import Categoria, Producto

class Command(BaseCommand):
    help = 'Genera e inserta 100 productos falsos con categorías'

    def handle(self, *args, **options):
        fake = Faker()

        # Crea categorías si no existen
        if not Categoria.objects.exists():
            for _ in range(5):  # numero de categorias
                categoria = Categoria(
                    codigo=random.randint(1, 1000),
                    nombre=fake.word(),
                    descripcion=fake.sentence(),
                )
                categoria.save()

        # Obtiene todas las categorías
        categories = Categoria.objects.all()

        # Crea y inserta 100 productos falsos
        for _ in range(100):
            product = Producto(
                codigo=random.randint(1001, 2000),
                nombre=fake.word(),
                precio=random.randint(10, 200),
                stock=random.randint(1, 100),
                categoria=random.choice(categories),
            )
            product.save()

        self.stdout.write(self.style.SUCCESS('Se han insertado 100 productos falsos con categorías.'))
