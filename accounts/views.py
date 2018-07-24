from django.shortcuts import render
from django.views.generic import FormView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import mixins
from django.shortcuts import get_object_or_404
from .models import Account
from .forms import UserCreateForm


# Create your views here.
class RegisterUser(mixins.PermissionRequiredMixin, mixins.LoginRequiredMixin, FormView):
    permission_required = ("accounts.custom_can_add_user", )
    permission_denied_message = "You have to be an admin to access this page"
    form_class = UserCreateForm
    success_url = reverse_lazy('account:register_success')
    template_name = 'account/user_register_form.html'

    def form_valid(self, form):
        form.save_user()
        return super(RegisterUser, self).form_valid(form)


def success_user_create(request):
    return render(request, 'account/success_user_create.html')


@login_required
def profile(request):
    context = {
        "user": request.user,
        "account": get_object_or_404(Account, user=request.user),
    }
    return render(request, 'account/user_profile_details.html', context)


class UpdateAccount(mixins.LoginRequiredMixin, UpdateView):
    model = Account
    template_name = 'account/account_update_form.html'
    success_url = reverse_lazy('account:profile')
