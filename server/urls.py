from django.contrib import admin
from django.urls import path
from serverapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("api/dealers/", views.get_dealers),
    path("api/dealers/state/<str:state>/", views.get_dealers_by_state),
    path("api/dealers/<int:dealer_id>/", views.get_dealer_by_id),
    path("api/dealers/<int:dealer_id>/reviews/", views.get_dealer_reviews),
    path("api/cars/", views.get_cars),
    path("api/analyze-review/", views.analyze_review),
    path("api/login/", views.login_user),
    path("api/logout/", views.logout_user),
    path("review/add/", views.add_review),
]
