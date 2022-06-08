from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth import login  # , authenticate
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from .forms.user import CustomLoginForm


class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'login.html'

    def get_success_url(self):
        # here method should be GET or POST.
        next_url = self.request.GET.get('next', None)
        if next_url:
            # you can include some query strings as well
            return "%s" % (next_url)
        else:
            return reverse('dashboard')  # what url you wish to return

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.request.user.is_staff:
            return redirect('{}'.format(self.request.GET.get('next', 'dashboard')))
        return super(CustomLoginView, self).get(*args, **kwargs)

