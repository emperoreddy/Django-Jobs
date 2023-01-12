import time
from django.contrib.auth.decorators import login_required
from django.forms import TextInput
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from jobs.models import Job


# Create your views here.
class JobView(ListView):
    model = Job
    template_name = 'jobs/jobs_index.html'


class CreateJobView(CreateView):
    model = Job
    fields = ['url', 'title', 'description']
    template_name = 'jobs/jobs_form.html'

    def get_success_url(self):
        return reverse('jobs:list_jobs')


class UpdateJobView(UpdateView):
    model = Job
    fields = ['url', 'title', 'description']
    template_name = 'jobs/jobs_form_edit.html'

    def get_success_url(self):
        return reverse('jobs:list_jobs')


class DeleteJobView(DeleteView):
    model = Job
    fields = ['url', 'title', 'description']
    template_name = 'jobs/jobs_form_edit.html'

    def get_success_url(self):
        # reverse('jobs:delete')
        # time.sleep(3)
        return reverse('jobs:list_jobs')


def deactivate(request, pk):
    Job.objects.filter(id=pk).update(active=0)
    return redirect('jobs:list_jobs')


def activate(request, pk):
    Job.objects.filter(id=pk).update(active=1)
    return redirect('jobs:list_jobs')


def website(request, url):
    return redirect(url)
