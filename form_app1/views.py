# formularz - metoda GET

from django.shortcuts import render

TASKS = []


def task_create_view(request):
    task = request.GET.get['task']
    TASKS.append(task)
    print(TASKS)

    return render(
        request,
        'form_app1/task_form.html',
        {
            'task': TASKS

        }
    )
