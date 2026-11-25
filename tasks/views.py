from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.decorators.http import require_POST
from django.db.models import Q
from django.utils import timezone

from .models import Task
from .forms import TaskForm


@login_required
def dashboard(request):
    all_tasks = Task.objects.filter(user=request.user)

    search = request.GET.get('search', '')
    status = request.GET.get('status', 'all')

    tasks = all_tasks

    if search:
        tasks = tasks.filter(
            Q(title__icontains=search) |
            Q(description__icontains=search)
        )

    if status == 'pending':
        tasks = tasks.filter(completed=False)

    elif status == 'completed':
        tasks = tasks.filter(completed=True)

    total_tasks = all_tasks.count()
    completed_tasks = all_tasks.filter(completed=True).count()
    pending_tasks = all_tasks.filter(completed=False).count()

    overdue_tasks = all_tasks.filter(
        completed=False,
        due_date__lt=timezone.localdate()
    ).count()

    progress = 0

    if total_tasks > 0:
        progress = round(completed_tasks / total_tasks * 100)

    context = {
        'tasks': tasks,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'overdue_tasks': overdue_tasks,
        'progress': progress,
        'search': search,
        'status': status,
        'today': timezone.localdate(),
    }

    return render(request, 'tasks/dashboard.html', context)


@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()

            return redirect('dashboard')
    else:
        form = TaskForm()

    return render(request, 'tasks/task_form.html', {
        'form': form,
        'heading': 'Add New Task',
    })


@login_required
def edit_task(request, pk):
    task = get_object_or_404(
        Task, pk=pk, user=request.user
    )

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/task_form.html', {
        'form': form,
        'heading': 'Edit Task',
    })


@login_required
@require_POST
def delete_task(request, pk):
    task = get_object_or_404(
        Task, pk=pk, user=request.user
    )

    task.delete()
    return redirect('dashboard')


@login_required
@require_POST
def complete_task(request, pk):
    task = get_object_or_404(
        Task, pk=pk, user=request.user
    )

    task.completed = not task.completed
    task.save()

    return redirect('dashboard')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'tasks/register.html', {
        'form': form,
    })@login_required
def tasks_api(request):
    tasks = Task.objects.filter(user=request.user)

    data = list(tasks.values(
        'id',
        'title',
        'description',
        'due_date',
        'priority',
        'completed',
    ))

    return JsonResponse({'tasks': data})
