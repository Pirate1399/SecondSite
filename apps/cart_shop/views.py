from django.shortcuts import render, get_object_or_404, redirect
from  django.views import View

from .models import CartItemShop, Product, Cart, Wishlist


# def save_product_in_cart(request, product_id):
#    product = get_object_or_404(Product, id=product_id)
#    cart_user = get_object_or_404(Cart, user=request.user)
#    cart_item = CartItemShop(cart=cart_user, product=product)
#    cart_item.save()


class ViewCartBuy(View):
   def get(self, request, product_id):
       if request.user.is_authenticated:
           save_product_in_cart(request, product_id)
           return redirect('cart_shop:cart')
       return redirect('auth_shop:login')

class ViewCart(View):
   def get(self, request):
       if request.user.is_authenticated:
           cart_items = CartItemShop.objects.filter(cart__user=request.user)
           data = list(cart_items)
           total_price_no_discount = int(sum(item.product.price * item.quantity
                                         for item in data))
           total_discount = sum(item.product.price * item.product.discount * item.quantity
                                for item in data if item.product.discount is not None)/100
           total_sum = total_price_no_discount - total_discount
           context = {'cart_items': data,
                      'total_price_no_discount': total_price_no_discount,
                      'total_discount': total_discount,
                      'total_sum': total_sum,
                      }
           return render(request, 'cart_shop/cart.html', context)
       return redirect('auth_shop:login')

class ViewCartDel(View):
   def get(self, request, item_id):
       cart_item = get_object_or_404(CartItemShop, id=item_id)
       cart_item.delete()
       return redirect('cart_shop:cart')

class ViewCartAdd(View):
    def get(self, request, product_id):
        if request.user.is_authenticated:
            save_product_in_cart(request, product_id)
            return redirect('home:index')
        return redirect('auth_shop:login')


def save_product_in_cart(request, product_id):
   cart_items = CartItemShop.objects.filter(cart__user=request.user,
                                            product__id=product_id)
   if cart_items:
       cart_item = cart_items[0]
       cart_item.quantity += 1
   else:
       product = get_object_or_404(Product, id=product_id)
       cart_user = get_object_or_404(Cart, user=request.user)
       cart_item = CartItemShop(cart=cart_user, product=product)
   cart_item.save()


def save_in_wishlist(request, product_id):
    wishlist_items = Wishlist.objects.filter(wishlist__user=request.user, product__id=product_id)
    product = get_object_or_404(Product, id=product_id)
    wishlist = get_object_or_404(Cart, user=request.user)
    wishlist_item = Wishlist(wishlist=wishlist, product=product)
    wishlist_item.save()



class ViewWishlist(View):
    def get(self, request):
        if request.user.is_authenticated:
            wishlist_items = Wishlist.objects.filter(wishlist__user=request.user)
            data = list(wishlist_items)
            context = {'wishlist_items': data}
            return render(request, 'cart_shop/wishlist.html', context)
        return redirect('auth_shop:login')

class WishlistAdd(View):
    def get(self, request, product_id):
        if request.user.is_authenticated:
            save_in_wishlist(request, product_id)
            return redirect('home:index')
        return redirect('auth_shop:login')


class DelWishlist(View):
    def get(self, request, item_id):
        wishlist_item = get_object_or_404(Wishlist, id=item_id)
        wishlist_item.delete()
        return redirect('cart_shop:wishlist')





