from django.shortcuts import render

# Create your views here.
def index_home_page(requests):
    return render(requests, 'home_page.html')

def index_contacts(requests):
    if requests.method == 'POST':
        name = requests.POST.get('name')
        phone = requests.POST.get('phone')
        message = requests.POST.get('message')

        print(requests)
        print(f"Имя: {name}\nНомер телефона: {phone}\nСообщение:{message}")
    return render(requests, 'contacts.html')
