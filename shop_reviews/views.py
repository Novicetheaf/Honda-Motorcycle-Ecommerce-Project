from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import ShopReview
from .forms import ShopReviewForm


def get_shop_reviews(request):
    """Renders all reviews currently in the database"""
    shop_reviews = ShopReview.objects.filter(review_date__lte=timezone.now()).order_by('-review_date')
    return render(request, "shop-reviews.html", {'shop_reviews': shop_reviews})


def shop_review_detail(request, pk):
    """
    Returns a single review and 
    adds one view to it or 404
    error if not found
    """
    shop_review = get_object_or_404(ShopReview, pk=pk)
    shop_review.review_views += 1
    shop_review.save()
    return render(request, "shop-review-detail.html", {'shop_review': shop_review})


def add_or_edit_shop_review(request, pk=None):
    """
    Allows us to add a review
    or edit a review depending
    on if shop_review's ID is
    Null or not.
    """
    shop_review = get_object_or_404(ShopReview, pk=pk) if pk else None
    review_form = ShopReviewForm(request.POST, instance=shop_review)
    if request.method == "POST":

        if review_form.is_valid():
            shop_review = review_form.save()
            return redirect(shop_review_detail, shop_review.pk)

        else:
            review_form = ShopReviewForm(instance=shop_review)

    return render(request, 'shop-review-form.html', {'review_form': review_form})
