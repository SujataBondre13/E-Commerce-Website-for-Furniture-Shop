from django.shortcuts import render, redirect
from django.http import HttpResponse 
from AdminApp.models import Category, Furniture, OwnerAccount, OrderMaster
from UserApp.models import UserInfo, MyCart, Shipping_Details
from django.template.defaulttags import register

# Create your views here.
def hello(request):
    return HttpResponse("Hello")

def home(request):
    cats = Category.objects.all()
    return render(request, 'home.html', {"cats":cats})

def ShowFurniture(request,id):
    cat = Category.objects.get(id = id)
    products = Furniture.objects.filter(cat_fk = id)
    cats = Category.objects.all()
    return render(request,"product.html",{"products":products,"cats":cats, "cat": cat})

@register.filter(name="split")
def split(value,key):
    value.split("key")
    return value.split(key)


def viewDetails(request, id):
    product = Furniture.objects.get(id = id)
    cats = Category.objects.all()

    return render(request, "viewDetails.html", {"product": product, "cats": cats})

def AddToCart(request):
    if(request.method == "POST"):
        if("uname" in request.session):
            fid = request.POST["fid"]
            qty = request.POST["qty"]
            uname = request.session["uname"]
            item = MyCart()
            item.user = UserInfo.objects.get(username = uname)
            item.furniture = Furniture.objects.get(id = fid)
            item.qty = qty
            item.save()
            return redirect(ShowCart)
            # return HttpResponse("Added to Cart")
        else:
            return redirect(Login)

def contact(request):
    cats = Category.objects.all()
    return render(request, "contact.html", {"cats": cats})
        
def ShowCart(request):
    cats = Category.objects.all()
    items = MyCart.objects.filter(user = request.session["uname"])

    counts = MyCart.objects.filter(user = request.session["uname"]).count()

    request.session['cart'] = counts

    total = 0 
    for item in items:
        total += item.qty * item.furniture.price
    request.session["total"] = total
    return render(request, "ShowCart.html", {"items": items, "cats": cats })

def ModifyCart(request):
    action = request.POST["action"]
    fid = request.POST["fid"]
    item = MyCart.objects.get(user = request.session["uname"], furniture = fid)
    if(action == "Remove"):
        item.delete()
        return redirect(ShowCart)

    else:
        item.qty = request.POST["qty"]
        item.save()
        return redirect(ShowCart)

def Shipping(request):
        if(request.method == "GET"):
            return render(request, 'Shipping_Details.html', {})
        else:
            cname = request.POST["cname"]
            city = request.POST["city"]
            mobile = request.POST["mobile"]
            state = request.POST["state"]
            pincode = request.POST["pincode"]

            customer = Shipping_Details()
            customer.customer_name = cname
            customer.city = city
            customer.mobile = mobile
            customer.state = state
            customer.pincode = pincode
            customer.save()
            return redirect(MakePayment)
        
def MakePayment(request):
    if(request.method == "GET"):
        return render(request, "MakePayment.html", {})
    else: 
        cardno = request.POST["cardno"]
        cvv = request.POST["cvv"]
        expiry = request.POST["expiry"]
        try:
            buyer = UserInfo.objects.get(userCardNo = cardno)
        except:
            return redirect(MakePayment)
        else:
            owner = OwnerAccount.objects.get(Ownercardno = '0000')
            amount = request.session["total"]
            owner.balance += amount
            owner.save()
            # delete all items from cart
            items = MyCart.objects.filter(user = request.session["uname"])
            order = OrderMaster()
            order.user = UserInfo.objects.get(username = request.session["uname"])
            order.amount = request.session["total"]
            details = ""
            for item in items:
                details += item.furniture.name
                item.delete()

            order.details = details
            order.save()
            return redirect(ShowCart)

def SignUp(request):
    if(request.method == "GET"):
        return render(request, 'SignUp.html', {})
    else:
        uname  = request.POST["uname"]
        cardno = request.POST["cardno"]
        email = request.POST["email"]
        pwd1 = request.POST["pwd1"]        
        try:
            user = UserInfo.objects.get(username = uname)
        except:
            # return HttpResponse("User not Exist")
            user = UserInfo(uname,cardno,email,pwd1)
            user.save()
            return redirect(Login)
        
        else:
            return redirect(SignUp)
        
def Login(request):
    if(request.method == "GET"):
        return render(request, 'Login.html', {})
    else:
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        try:
            user = UserInfo.objects.get(username = uname, password = pwd)
        except:
            return redirect(Login)
        else:
            request.session["uname"]=uname
            return redirect(home)

def Logout(request):
    request.session.clear()
    return redirect(home)




