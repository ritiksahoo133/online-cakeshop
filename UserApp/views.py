from django.db import close_old_connections
from django.http import HttpResponse
from django.shortcuts import redirect, render
from AdminApp.models import Cake,Category
from UserApp.models import UserInfo,MyCart,Payment
# Create your views here.
def Home(request):
      cats=Category.objects.all()
      cakes=Cake.objects.all()
      return  render(request,"master.html",{"cats":cats,"cakes":cakes})

      
def showCakes(request,cid):
      cakes=Cake.objects.filter(category=cid)
      cats=Category.objects.all()
      cat=Category.objects.get(id=cid)
      
      return render(request,"master.html",{"cakes":cakes,"cats":cats,"cat_name":cat.cat_name})

def showDetails(request,cid):
      if(request.method=="GET"):
            cake=Cake.objects.filter(id=cid)
            cats=Category.objects.all()
            return render(request,"showCakeDetails.html",{"cake":cake,"cats":cats})
      else:
            if("uname" in request.session):
                  cid=request.POST["cake_id"]
                  qty=request.POST["qty"]
                  user=UserInfo.objects.get(username=request.session["uname"])
                  cake=Cake.objects.get(id=cid)
                  try:
                        cart=MyCart.objects.get(user=user,cake=cake)
                  except:
                        cart=MyCart()
                        cart.user=user
                        cart.cake=cake
                        cart.qty=qty
                        cart.save()
                        return redirect(Home)
                  else:
                        return HttpResponse("already present in the cart")
            else:
                  return redirect(Login)

def Signup(request):
      cats=Category.objects.all()
      if(request.method=="GET"):
            return render(request,"Signup.html",{"cats":cats})
      else:
            uname=request.POST["uname"]
            pwd=request.POST["pwd"]
            try:
                  u1=UserInfo.objects.get(username=uname)
            except:
                  u1=UserInfo(uname,pwd,'inactive')
                  u1.save()
                  return redirect(Home)
            else:
                  return HttpResponse("User already exists")


def Login(request):
      cats=Category.objects.all()
      if(request.method=="GET"):
            return render(request,"Login.html")
      else:
            uname=request.POST["uname"]
            pwd=request.POST["pwd"]
            try:
                  u1=UserInfo.objects.get(username=uname,password=pwd)
            except:
                  pass
            else:
                  request.session["uname"]=uname
                  u1.status="active"
                  u1.save()
            return redirect(Home)


def Logout(request):
      u1=UserInfo.objects.get(username=request.session["uname"])
      u1.status="inactive"
      request.session.clear()
      return redirect(Home)

def showAllCartItems(request):
      if(request.method=="GET"):
            cats=Category.objects.all()
            user=UserInfo.objects.get(username=request.session["uname"])
            cart_items=MyCart.objects.filter(user=user)
            total=0
            
            for item in cart_items:
                  total+=item.cake.price * item.qty
            request.session["total"]=total
            
            return render(request,"showAllCartItems.html",{"user":user,"cart_items":cart_items,"cats":cats})
      else:

           action=request.POST["action"]
           id=request.POST["item_id"]
           item=MyCart.objects.get(id=id)

           if(action=="update"):
                 qty=request.POST["qty"]
                 item.qty=qty
                 item.save()
           else:
                item.delete()
           return redirect(showAllCartItems)



def MakePayment(request):
      if(request.method=="GET"):
            cats=Category.objects.all()
            return render(request,"MakePayment.html",{"cats":cats})
      else:
            card_no=request.POST["card_no"]
            cvv=request.POST["cvv"]
            expiry=request.POST["expiry"]
            try:
                  buyer=Payment.objects.get(card_no=card_no,cvv=cvv,expiry=expiry)
            except:
                  return HttpResponse("Invalid card details")
            else:
                  owner=Payment.objects.get(card_no="333",cvv="222",expiry="12/2025")
                  buyer.balance-=request.session["total"]
                  owner.balance+=request.session["total"]
                  buyer.save()
                  owner.save()
            return redirect(Home)
def Loginclient(request):
      if(request.method==GET):
            return HttpResponse("Successful")
            








