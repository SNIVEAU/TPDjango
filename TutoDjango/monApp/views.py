from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import *


from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name = "monApp/page_home.html"
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['titreh1'] = "Hello DJANGO"
        return context
    def post(self, request, **kwargs):
        return render(request, self.template_name)

class AboutView(TemplateView):
    template_name = "monApp/page_home.html"
    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['titreh1'] = "About us..."
        return context
    def post(self, request, **kwargs):
        return render(request, self.template_name)
# class ContactView(TemplateView):
#     template_name = "monApp/page_home.html"
#     def get_context_data(self, **kwargs):
#         context = super(ContactView, self).get_context_data(**kwargs)
#         context['titreh1'] = "Nous contacter"
#         return context
#     def post(self, request, **kwargs):
#         return render(request, self.template_name)


from django.shortcuts import redirect

def ContactView(request):
    titreh1 = "Contact us !"
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MonProjet Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@monprojet.com'],
            )
            return redirect('email-sent')
    else:
        form = ContactUsForm()
    return render(request, "monApp/page_home.html", {'titreh1': titreh1, 'form': form})


#     prdts = Produit.objects.all()
#     html = """
#             <h1> Produits
#             <li>
#             """
#     for prod in prdts:
#         html += "<ul> " + prod.intituleProd + "</ul>"

#     html += "</li>"
#     return HttpResponse(html)

class ProduitListView(ListView):
    model = Produit
    template_name = "monApp/list_produits.html"
    context_object_name = "prdts"
    def get_queryset(self ) :
        return Produit.objects.order_by("prixUnitaireProd")
    
    def get_context_data(self, **kwargs):
        context = super(ProduitListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes produits"
        return context
    
class StatutListView(ListView):
    model = Statut
    template_name = "monApp/list_statuts.html"
    context_object_name = "status"
    def get_queryset(self ) :
        return Statut.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(StatutListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes Statuts"
        return context

class RayonsListView(ListView):
    model = Rayon
    template_name = "monApp/list_rayons.html"
    context_object_name = "rayons"
    def get_queryset(self ) :
        return Rayon.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(RayonsListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes rayons"
        return context


class CategorieListView(ListView):
    model = Categorie
    template_name = "monApp/list_categories.html"
    context_object_name = "categories"
    def get_queryset(self ) :
        return Categorie.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(CategorieListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes catégories"
        return context

class ProduitDetailView(DetailView):
    model = Produit
    template_name = "monApp/detail_produit.html"
    context_object_name = "prdt"

    def get_context_data(self, **kwargs):
        context = super(ProduitDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du produit"
        return context

class RayonDetailView(DetailView):
    model = Rayon
    template_name = "monApp/detail_rayon.html"
    context_object_name = "rayon"

    def get_context_data(self, **kwargs):
        context = super(RayonDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du rayon"
        return context

class CategorieDetailView(DetailView):
    model = Categorie
    template_name = "monApp/detail_categorie.html"
    context_object_name = "categorie"

    def get_context_data(self, **kwargs):
        context = super(CategorieDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail de la catégorie"
        return context

#  # Ancienne version de gestion des vues en faisant un render du template
# def ListStatus(request):
#     status = Statut.objects.all()
    
#     return render(request, 'monApp/list_statuts.html',{'status': status})

# def ListCategorie(request):
#     categories = Categorie.objects.all()
    
#     return render(request, 'monApp/list_categories.html',{'categories': categories})

# def ListRayon(request):
#     rayons = Rayon.objects.all()
#     return render(request, 'monApp/list_rayons.html',{'rayons': rayons})


class ConnectView(LoginView):
    template_name = 'monApp/page_login.html'

    def post(self, request, **kwargs):
        lgn = request.POST.get('username', False)
        pswrd = request.POST.get('password', False)
        user = authenticate(username=lgn, password=pswrd)
        if user is not None and user.is_active:
            login(request, user)
            return render(request, 'monApp/page_home.html', {'param': lgn, 'message': "You're connected"})
        else:
            return render(request, 'monApp/page_register.html')
        
class RegisterView(TemplateView):
    template_name = 'monApp/page_register.html'

    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        mail = request.POST.get('mail', False)
        password = request.POST.get('password', False)
        if (len(User.objects.filter(username=username)) != 0):
            return render(request, 'monApp/page_register.html', {'error': "Ce nom d'utilisateur existe déjà."})
        
        user = User.objects.create_user(username, mail, password)
        user.save()
        if user is not None and user.is_active:
            return render(request, 'monApp/page_login.html')
        else:
            return render(request, 'monApp/page_register.html')
        
class DisconnectView(TemplateView):
    template_name = 'monApp/page_logout.html'
    def get(self, request, **kwargs):
        logout(request)
        return render(request, self.template_name)
    
# def ProduitCreate(request):
#     if request.method == 'POST':
#         form = ProduitForm(request.POST)
#         if form.is_valid():
#             prdt = form.save()
#             return redirect('lst_prdts',)
#     else:
#         form = ProduitForm()
#     return render(request, "monApp/create_produit.html", {'form': form})


class ProduitCreateView(CreateView):
    model = Produit
    form_class = ProduitForm
    template_name = "monApp/create_produit.html"

    def form_valid(self, form):
        prdt = form.save()
        return redirect('dtl-prdt', prdt.refProd)
    

class ProduitUpdateView(UpdateView):
    model = Produit
    form_class = ProduitForm
    template_name = "monApp/update_produit.html"

    def form_valid(self, form):
        prdt = form.save()
        return redirect('dtl-prdt', prdt.refProd)
    
class ProduitDeleteView(DeleteView):
    model = Produit
    template_name = "monApp/delete_produit.html"
    success_url = reverse_lazy('lst_prdts')


class RayonCreateView(CreateView):
    model = Rayon
    form_class = RayonForm
    template_name = "monApp/create_rayon.html"
    def form_valid(self, form):
        rayon = form.save()
        return redirect('dtl_rayon', rayon.refRayon)
    

class RayonUpdateView(UpdateView):
    model = Rayon
    form_class = RayonForm
    template_name = "monApp/update_rayon.html"

    def form_valid(self, form):
        rayon= form.save()
        return redirect('dtl_rayon', rayon.refRayon)
    
class RayonDeleteView(DeleteView):
    model = Rayon
    template_name = "monApp/delete_rayon.html"
    success_url = reverse_lazy('lst_rayons')


class CategorieCreateView(CreateView):
    model = Categorie
    form_class = CategorieForm
    template_name = "monApp/create_categorie.html"
    
    def form_valid(self, form):
        categorie = form.save()
        return redirect('dtl-categorie', categorie.idCat)

class CategorieUpdateView(UpdateView):
    model = Categorie
    form_class = CategorieForm
    template_name = "monApp/update_categorie.html"

    def form_valid(self, form):
        categorie = form.save()
        return redirect('dtl-categorie', categorie.idCat)

class CategorieDeleteView(DeleteView):
    model = Categorie
    template_name = "monApp/delete_categorie.html"
    success_url = reverse_lazy('lst_categories')