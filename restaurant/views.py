from http import HTTPStatus
from django.shortcuts import render,redirect
from django.http import HttpResponse


from .models import Meal,OrderTransaction

from .forms import UserLoginForm
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required

# Create your views here.




#@login_required
def index(request):
    if request.method =='GET':
        #to store the meals
        meals = []
        #to control the meals (pour controler les repas)
        temp_list = []
        #Ensuite, nous collectons tous nos repas, tous les repas de la base de données et les stockons dans tous les repas.
        all_meals = Meal.objects.all()
        #Ensuite, nous examinons tous les repas et ici, lors de la boucle, nous ajoutons le repas à la liste temporaire.
        for cnt in range(all_meals.count()):
             #Ok, donc nous devons également nous assurer, oh ok, que c'est un plus un.
            temp_list.append(all_meals[cnt])

           

            #Maintenant, si nous avons trois repas, nous ajoutons la liste temporaire à la liste des repas et nous vidons la liste temporaire.
            if (cnt + 1) %3 == 0 and cnt + 1 > 2:
                meals.append(temp_list)
                temp_list = []
        #Et maintenant, voici si nous avons des repas en retard.,ajouter simplement les repas
        if temp_list:
            meals.append(temp_list)

        context = {
            'meals':meals
        }

 

        return render(request=request,template_name='restaurant/index.html',context=context)

    return HttpResponse(HTTPStatus.BAD_REQUEST)
#@login_required
def order(request,pk=None):
    """
    View for the order page.
    Author: Omar
    """
    if pk:
        got_meal = Meal.objects.filter(id=pk).last()

        if  got_meal and got_meal.stock > 0:
              OrderTransaction.objects.create(
                  meal=got_meal,customer=request.user,amount=got_meal.price
                  )

              got_meal.stock -= 1

              got_meal.save()

              return redirect('index')
        
        return HttpResponse(HTTPStatus.BAD_REQUEST)
#@login_required   
def details(request):
    transaction = OrderTransaction.objects.filter(customer=request.user)

    context ={
        'transaction':transaction,
    }
    return render(request=request,template_name='restaurant/details.html',context=context)


def about(request):
    return render(request=request,template_name='restaurant/about.html')

def login_user(request):

    if request.method == 'POST':
       login_form = UserLoginForm(request.POST,request.FILES)

       if login_form.is_valid():
           username = login_form.cleaned_data.get('username')
           password = login_form.cleaned_data.get('password')
           
           authenticateUser = authenticate(request,username=username,password=password)
           
           if authenticateUser is not None:
               login(request,authenticateUser)

               return redirect('details')
           #pour afficher un message d'erreur
           login_form.add_error('username','Invalid username or password')
           login_form.add_error('password','Invalid username or password')
    else:    
        login_form = UserLoginForm()

        login_form.fields['password'].widget.attrs['placeholder'] = 'Your password'

    context = {
        'login_form':login_form
    }



    return render(request=request,template_name='restaurant/login.html',context=context)


def logout_user(request):
    logout(request)

    return redirect('index')