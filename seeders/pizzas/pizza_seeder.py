import json
import os

from django.core.management.base import BaseCommand

from apps.pizzas.models import Pizza


class Command(BaseCommand):
    help = 'Popula a tabela Pizza com dados iniciais'

    def handle(self, *args, **options):
        self.load_data_from_json('pizza.json')

        self.stdout.write(self.style.SUCCESS(
            "Dados de Pizza carregados com sucesso!"
        ))

    def load_data_from_json(self, filename):
        """Carrega dados de um arquivo JSON"""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        data_path = os.path.join(base_dir, 'data', filename)

        if not os.path.exists(data_path):
            self.stdout.write(self.style.WARNING(
                f"Arquivo de dados não encontrado: {data_path}"
            ))
            return

        with open(data_path, 'r') as f:
            data = json.load(f)

        created_count = 0
        for item in data:
            try:
                # Campos únicos para get_or_create
                unique_data = {'name': item.get('name')}

                # Campos padrão (incluindo ForeignKeys)
                defaults_data = {'image': item.get('image'),
                                 'price': item.get('price'),
                                 'description': item.get('description')}

                obj, created = Pizza.objects.get_or_create(
                    **unique_data,
                    defaults=defaults_data
                )
                if created:
                    created_count += 1
            except Exception as e:
                self.stdout.write(self.style.WARNING(
                    f"Erro ao criar registro: {str(e)}"
                ))

        self.stdout.write(self.style.SUCCESS(
            f"{created_count} registros de Pizza criados a partir de {filename}"
        ))
