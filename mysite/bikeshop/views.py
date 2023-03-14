from django.shortcuts import render, redirect, reverse
from django.views import generic
from django.db.models import Q
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.views.generic.edit import FormMixin
from .models import Bike, Category, Brand, Order
from .forms import OrderForm, CommentForm, UserUpdateForm, ProfilisUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Count
from django.contrib.auth.models import User


def index(request):
    brandu_kiekis = Brand.objects.count()
    modeliu_kiekis = Bike.objects.count()
    atliktu_uzsakymu_kiekis = Order.objects.filter(status__exact='Pending').count()
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    kontekstas = {
        'brandu_kiekis': brandu_kiekis,
        'modeliu_kiekis': modeliu_kiekis,
        'atliktu_uzsakymu_kiekis': atliktu_uzsakymu_kiekis,
        'num_visits': num_visits,
    }
    return render(request, 'index.html', context=kontekstas)


@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'Vartotojas {username} užregistruotas!')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'register.html')


class BikeListView(generic.ListView):
    model = Bike
    template_name = 'bike_list.html'
    paginate_by = 6
    context_object_name = 'bikes'


class BikeDetailView(FormMixin, generic.DetailView):
    model = Bike
    template_name = 'bike_detail.html'
    context_object_name = 'bike'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('bike_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = self.get_form()
        return context


class OrderListView(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    model = Order
    template_name = 'order_list.html'
    context_object_name = 'orders'
    ordering = ['-date_ordered']

    def test_func(self):
        return self.request.user.is_authenticated

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class CategoryListView(generic.ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'
    queryset = model.objects.annotate(num_bikes=Count('bike'))


class CategoryDetailView(FormMixin, generic.DetailView):
    model = Category
    template_name = 'category_detail.html'
    context_object_name = 'category'
    form_class = CommentForm


class BrandListView(generic.ListView):
    model = Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'
    queryset = model.objects.annotate(num_bikes=Count('bike'))


class BrandDetailView(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
    model = Brand
    template_name = 'brand_detail.html'
    context_object_name = 'brand'

    def test_func(self):
        return self.request.user.is_authenticated


class OrderCreateView(LoginRequiredMixin, generic.CreateView):
    model = Order
    template_name = 'order_create.html'
    form_class = OrderForm
    success_url = '/bikeshop/orders/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.status = 'pending'
        messages.success(self.request, 'Your order has been created!')
        return super().form_valid(form)


class OrderDetailView(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
    model = Order
    template_name = 'order_detail.html'
    context_object_name = 'order'

    def test_func(self):
        return self.request.user.is_authenticated


class OrderUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Order
    template_name = 'order_update.html'
    form_class = OrderForm
    context_object_name = 'order'
    success_url = '/bikeshop/orders/'

    def form_valid(self, form):
        messages.success(self.request, 'Your order has been updated!')
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_authenticated


class OrderDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Order
    template_name = 'order_delete.html'
    context_object_name = 'order'

    def get_success_url(self):
        messages.success(self.request, 'Your order has been deleted.')
        return reverse('order_list')

    def test_func(self):
        return self.request.user.is_authenticated


def search(request):
    query = request.GET.get('query')
    search_results = Bike.objects.filter(
        Q(name__icontains=query) | Q(category__name__icontains=query) | Q(brand__name__icontains=query))
    return render(request, 'search.html', {'bikes': search_results, 'query': query})


@login_required
def profilis(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfilisUpdateForm(request.POST, request.FILES, instance=request.user.profilis)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Profilis atnaujintas")
            return redirect('profilis')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfilisUpdateForm(instance=request.user.profilis)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'profilis.html', context)
