from django.shortcuts import render

# Create your views here.
def employee_add(request):
   if request.method=="GET":
       form=BookFormAdd()
       context={}
       context["form"]=form
       return render(request,'book_add.html',context)
   elif request.method=="POST":
       form=BookFormAdd(request.POST)
       if form.is_valid():
           book_name=form.cleaned_data["book_name"]
           Author = form.cleaned_data["author"]
           price = form.cleaned_data["price"]
           copies = form.cleaned_data["copies"]
           print(form.cleaned_data)
           book=Book(book_name=book_name,author=Author,price=price,copies=copies)
           book.save()
           return render(request, 'book_add.html',{"form":form})
       else:
           return render(request, 'book_add.html', {"form": form})