from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Item, Color, Review, ReviewAvg

def index(request):
	if request.method == 'POST': # if it's a post request
		print(request.body)
		# get info out of request
		post_item_id = int(request.POST['item']) 
		post_color_id = int(request.POST['color'])
		post_score = int(request.POST['score'])
		
		# make a new review with that information
		new_rev = Review(
			item_id=post_item_id,
			color_id=post_color_id,
			score=post_score,
		)
		new_rev.save()

		# try to update review average for that item and color
		try:
			rev_avg = ReviewAvg.objects.get(
				item_id = post_item_id,
				color_id = post_color_id,
			)
			rev_avg.add_review(new_rev)

		except ObjectDoesNotExist:
			ReviewAvg(
				item_id=post_item_id,
				color_id=post_color_id,
				score=post_score,
				count=1
			).save()
		
		item = Item.objects.get(pk=post_item_id)
		item.reset_highest()

		return HttpResponseRedirect('/colors/')

	# If it's a get request
	context = {
		'items_context': Item.objects.all(),
		'colors_context': Color.objects.all(),
		'scores_context': range(5, 0, -1),
	}
	print( render(
		request,
		'colors/index.html',
		context
	).content)
	return render(
		request,
		'colors/index.html',
		context
	)
