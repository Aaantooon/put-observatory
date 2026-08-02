from django.shortcuts import render

def home(request):
    # Главная страница — отдаём index.html (как у тебя уже настроено в проекте)
    return render(request, 'index.html', {
        'title': 'Главная — Путь наблюдателя',
        'subtitle': 'Фонарь рассеивает туман: шаг за шагом мы видим путь'
    })

def about(request):
    # Для about делаем полноценный шаблон (не HttpResponse), чтобы было красиво
    return render(request, 'about.html', {
        'title': 'О проекте — Путь наблюдателя'
    })

def map_view(request):
    return render(request, 'map.html', {
        'title': 'Карта пути наблюдателя'
    })
