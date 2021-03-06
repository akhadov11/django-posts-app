from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


class SignUpView(generic.CreateView):
    """
    Basic signup view.
    """

    form_class = UserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy("login")
