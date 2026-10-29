import json
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Dealer, Review

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "About.html")

def contact(request):
    return render(request, "Contact.html")

def get_dealers(request):
    data = list(Dealer.objects.all().values("id", "full_name", "city", "state", "address", "phone"))
    return JsonResponse({"dealers": data})

def get_dealers_by_state(request, state):
    data = list(Dealer.objects.filter(state__iexact=state).values("id", "full_name", "city", "state", "address", "phone"))
    return JsonResponse({"state": state, "dealers": data})

def get_dealer_by_id(request, dealer_id):
    try:
        d = Dealer.objects.get(id=dealer_id)
    except Dealer.DoesNotExist:
        return JsonResponse({"error": "Dealer not found"}, status=404)
    return JsonResponse({"id": d.id, "full_name": d.full_name, "city": d.city, "state": d.state, "address": d.address, "phone": d.phone})

def get_dealer_reviews(request, dealer_id):
    if not Dealer.objects.filter(id=dealer_id).exists():
        return JsonResponse({"error": "Dealer not found"}, status=404)
    data = list(Review.objects.filter(dealer_id=dealer_id).values("id", "name", "review", "purchase", "created_at"))
    return JsonResponse({"dealer_id": dealer_id, "reviews": data})

def get_cars(request):
    return JsonResponse({"makes": [
        {"make": "Toyota", "models": ["Camry", "Corolla", "RAV4"]},
        {"make": "Honda", "models": ["Civic", "Accord", "CR-V"]},
        {"make": "Ford", "models": ["Mustang", "Escape", "Explorer"]}
    ]})

@csrf_exempt
def analyze_review(request):
    if request.method != "POST":
        return JsonResponse({"error": "Use POST with JSON body"}, status=405)
    try:
        body = json.loads(request.body or "{}")
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    review = str(body.get("review", ""))
    positive_words = ["fantastic", "great", "excellent", "good", "helpful", "friendly"]
    sentiment = "positive" if any(word in review.lower() for word in positive_words) else "neutral"
    return JsonResponse({"review": review, "sentiment": sentiment, "note": "Simple keyword demo; not a production ML model."})

@csrf_exempt
def login_user(request):
    if request.method != "POST":
        return JsonResponse({"error": "Use POST with username and password"}, status=405)
    try:
        body = json.loads(request.body or "{}")
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    user = authenticate(request, username=body.get("username", ""), password=body.get("password", ""))
    if user is None:
        return JsonResponse({"error": "Invalid credentials"}, status=401)
    login(request, user)
    return JsonResponse({"message": "Login successful", "username": user.username})

@csrf_exempt
def logout_user(request):
    logout(request)
    return JsonResponse({"message": "Logout successful"})

@csrf_exempt
def add_review(request):
    if request.method != "POST":
        return JsonResponse({"error": "Use POST"}, status=405)
    try:
        body = json.loads(request.body or "{}")
        dealer = Dealer.objects.get(id=int(body.get("dealer_id", 0)))
    except (json.JSONDecodeError, ValueError, Dealer.DoesNotExist):
        return JsonResponse({"error": "Valid dealer_id required"}, status=400)
    text = str(body.get("review", "")).strip()
    if not text:
        return JsonResponse({"error": "Review text required"}, status=400)
    review = Review.objects.create(dealer=dealer, name=request.user.username if request.user.is_authenticated else "Demo User", review=text, purchase=bool(body.get("purchase", True)))
    return JsonResponse({"message": "Review added", "id": review.id, "dealer_id": dealer.id, "review": review.review}, status=201)
