from django.core.management.base import BaseCommand
from colors.models import Item, Color
from os.path import join

class Command(BaseCommand):
		help = 'Makes Items and Colors'

		def handle(self, *args, **options):
			with open(join('populate', 'items.txt')) as f:
				print('making items')
				for row in f.readlines():
						Item.objects.get_or_create(
							name=row
						)

			with open(join('populate', 'colors.txt')) as f:
				print('making colors')
				for row in f.readlines():
						Color.objects.get_or_create(
							name=row
						)

'''	
			for filename, classname in [
				('items.txt', Item),
				('colors.txt', Color),
			]:
				with open(join('populate', filename)) as f:
					for row in f.readlines():
						classname.objects.get_or_create(
							name=row[0]
						)
'''
