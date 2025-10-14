from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import *
from django.db.models import Count, Prefetch
from decimal import Decimal
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


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
@method_decorator(login_required, name='dispatch')

class ProduitListView(ListView):
    model = Produit
    template_name = "monApp/list_produits.html"
    context_object_name = "prdts"
    def get_queryset(self ) :
        query = self.request.GET.get('search')
        if query:
            return Produit.objects.filter(intituleProd__icontains=query).select_related('categorie').select_related('statut')
        return Produit.objects.select_related('categorie').select_related('statut')    
    
    
    def get_context_data(self, **kwargs):
        context = super(ProduitListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes produits"
        return context
@method_decorator(login_required, name='dispatch')
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
@method_decorator(login_required, name='dispatch')

class RayonsListView(ListView):
    model = Rayon
    template_name = "monApp/list_rayons.html"
    context_object_name = "rayons"
    
    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return Rayon.objects.filter(refRayon__icontains=query).prefetch_related(
                Prefetch('rayons', queryset=Contenir.objects.select_related('refProd'))
            )
        return Rayon.objects.all().prefetch_related(
            Prefetch('rayons', queryset=Contenir.objects.select_related('refProd'))
        )

    def get_context_data(self, **kwargs):
        context = super(RayonsListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes rayons"
        
        ryns_dt = []
        for rayon in context['rayons']:
            contenirs = rayon.rayons.all()
            
            total = Decimal('0.00')
            for contenir in contenirs:
                prix = contenir.refProd.prixUnitaireProd or Decimal('0.00')
                qte = contenir.Qte or 0
                total += prix * qte
                print(total)
            ryns_dt.append({
                'rayon': rayon,
                'nb_produits': contenirs.count(),
                'total_stock': total
            })
        
        context['ryns_dt'] = ryns_dt
        return context


@method_decorator(login_required, name='dispatch')
class CategorieListView(ListView):
    model = Categorie
    template_name = "monApp/list_categories.html"
    context_object_name = "categories"
    
    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return Categorie.objects.filter(nomCat__icontains=query).annotate(nb_produits=Count('produits'))        # Annoter chaque catégorie avec le nombre de produits liés
        return Categorie.objects.annotate(nb_produits=Count('produits'))

    def get_context_data(self, **kwargs):
        context = super(CategorieListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes catégories"
        return context
@method_decorator(login_required, name='dispatch')
class ProduitDetailView(DetailView):
    model = Produit
    template_name = "monApp/detail_produit.html"
    context_object_name = "prdt"

    def get_context_data(self, **kwargs):
        context = super(ProduitDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du produit"
        return context
@method_decorator(login_required, name='dispatch')

class RayonDetailView(DetailView):
    model = Rayon
    template_name = "monApp/detail_rayon.html"
    context_object_name = "rayon"

    def get_context_data(self, **kwargs):
        context = super(RayonDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du rayon"
        rayon = self.object
        contenirs = (
            Contenir.objects
            .filter(refRayon=rayon.refRayon)
            .select_related('refProd')
        )
        produits = [c.refProd for c in contenirs]
        total = sum(c.refProd.prixUnitaireProd * c.Qte for c in contenirs)
        context['prdts_dt'] = produits
        context['total_nb_produit'] = total
        return context
@method_decorator(login_required, name='dispatch')

class CategorieDetailView(DetailView):
    model = Categorie
    template_name = "monApp/detail_categorie.html"
    context_object_name = "categorie"

    def get_queryset(self):
# Annoter chaque catégorie avec le nombre de produits liés
        return Categorie.objects.annotate(nb_produits=Count('produits'))
    def get_context_data(self, **kwargs):
        context = super(CategorieDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail de la catégorie"
        context['prdts'] = self.object.produits.all()

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

@method_decorator(login_required, name='dispatch')

class ProduitCreateView(CreateView):
    model = Produit
    form_class = ProduitForm
    template_name = "monApp/create_produit.html"

    def form_valid(self, form):
        prdt = form.save()
        return redirect('dtl-prdt', prdt.refProd)
    
@method_decorator(login_required, name='dispatch')

class ProduitUpdateView(UpdateView):
    model = Produit
    form_class = ProduitForm
    template_name = "monApp/update_produit.html"

    def form_valid(self, form):
        prdt = form.save()
        return redirect('dtl-prdt', prdt.refProd)
@method_decorator(login_required, name='dispatch')
 
class ProduitDeleteView(DeleteView):
    model = Produit
    template_name = "monApp/delete_produit.html"
    success_url = reverse_lazy('lst_prdts')

@method_decorator(login_required, name='dispatch')

class RayonCreateView(CreateView):
    model = Rayon
    form_class = RayonForm
    template_name = "monApp/create_rayon.html"
    def form_valid(self, form):
        rayon = form.save()
        return redirect('dtl_rayon', rayon.refRayon)
    
@method_decorator(login_required, name='dispatch')

class RayonUpdateView(UpdateView):
    model = Rayon
    form_class = RayonForm
    template_name = "monApp/update_rayon.html"

    def form_valid(self, form):
        rayon= form.save()
        return redirect('dtl_rayon', rayon.refRayon)
@method_decorator(login_required, name='dispatch')

class RayonDeleteView(DeleteView):
    model = Rayon
    template_name = "monApp/delete_rayon.html"
    success_url = reverse_lazy('lst_rayons')

@method_decorator(login_required, name='dispatch')

class CategorieCreateView(CreateView):
    model = Categorie
    form_class = CategorieForm
    template_name = "monApp/create_categorie.html"
    
    def form_valid(self, form):
        categorie = form.save()
        return redirect('dtl-categorie', categorie.idCat)
@method_decorator(login_required, name='dispatch')

class CategorieUpdateView(UpdateView):
    model = Categorie
    form_class = CategorieForm
    template_name = "monApp/update_categorie.html"

    def form_valid(self, form):
        categorie = form.save()
        return redirect('dtl-categorie', categorie.idCat)
@method_decorator(login_required, name='dispatch')

class CategorieDeleteView(DeleteView):
    model = Categorie
    template_name = "monApp/delete_categorie.html"
    success_url = reverse_lazy('lst_categories')

@method_decorator(login_required, name='dispatch')
class ContenirCreateView(CreateView):
    form_class = ContenirForm  # Supprime model = Contenir
    template_name = "monApp/create_contenir.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rayon_id = self.kwargs.get('pk')
        if rayon_id:
            context['rayon'] = Rayon.objects.get(refRayon=rayon_id)  # Corrige pk → refRayon
        return context
    
    def form_valid(self, form):
        rayon_id = self.kwargs.get('pk')
        rayon = Rayon.objects.get(refRayon=rayon_id)
        
        produit = form.save()
        
        contenir = Contenir.objects.create(
            refProd=produit,
            refRayon=rayon,
            Qte=form.cleaned_data['Qte']  # Utilise la quantité du formulaire
        )
        
        return redirect('dtl_rayon', rayon.refRayon)
    
    def get_success_url(self):
        return reverse_lazy('dtl_rayon', kwargs={'pk': self.kwargs.get('pk')})