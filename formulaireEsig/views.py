from django.shortcuts import render,redirect,render_to_response
from .forms import UtiForm
from .models import Sie_Utilisateur

# Create your views here. Es donde ponemos la logica de nuetsra app, toma info del model y pasa a una view

#def uti_new(request):
    #if request.method == "POST":
      #  form = proForm(request.POST)
      #  post = form.save(commit=False)
       # post.save()
  #  else:
      #  form = proForm()
   # return render(request, 'esigapp/formB.html', {'form': form})
 #   return render(request, 'formulaireEsig/uti_list.html', {})
def uti_list(request):
    sie_utilisateur = Sie_Utilisateur.objects.filter()
    return render(request, 'formulaireEsig/uti_list.html', {'sie_utilisateur':sie_utilisateur})


def uti_new(request):
    if request.method == 'POST':
        form = UtiForm(request.POST)
        if form.is_valid():
            sie_utilisateur = form.save(commit=False)
            sie_utilisateur.UTI_SUPPRIME = False
            sie_utilisateur.save()
            return redirect('/uti_list', pk=sie_utilisateur.pk)
    else:
        form = UtiForm()
    return render(request, 'formulaireEsig/formulaire.html', {'form':form})


# Ajax qui permet de chercher les utilisateurs
def chercher(request):
    if request.method == "POST":
        text_cherche = request.POST['text_cherche']
        if text_cherche == "":
            sie_utilisateur = Sie_Utilisateur.objects.filter()
        else:
            sie_utilisateur = Sie_Utilisateur.objects.filter(UTI_NOM__contains=text_cherche)

    return render_to_response('formulaireEsig/uti_list.html',{'sie_utilisateur' : sie_utilisateur })