from django.shortcuts import render

# Create your views here. Es donde ponemos la logica de nuetsra app, toma info del model y pasa a una view

#def uti_list(request):
    #if request.method == "POST":
      #  form = proForm(request.POST)
      #  post = form.save(commit=False)
       # post.save()
  #  else:
      #  form = proForm()
   # return render(request, 'esigapp/formB.html', {'form': form})
 #   return render(request, 'formulaireEsig/uti_list.html', {})
def uti_list(request):
    return render(request, 'formulaireEsig/uti_list.html', {})
