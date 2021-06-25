from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView
from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    context_object_name = 'target_profile'
    template_name = 'profileapp/create.html'

    # models를 보면 user가 있지만 models를 보면 없다. 모르는 사람이 내 계정으로와서 나쁜짓을 하는걸 방지하기 위해서다.
    # form_valid를 통해 서버에서 user 내용을 넘겨준다.
    def form_valid(self, form):
        temp_profile = form.save(commit=False)#form임시저장
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})


@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileCreationForm
    context_object_name = 'target_profile'
    template_name = 'profileapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})