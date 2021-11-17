from decimal import Decimal

from account.models import User
from comic.models import Comic, ComicType

from .models import LoginCart


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get("sessionKey")  # in session

        # if sessionKey is not in sessions then craete new sessionKey and update sessions
        if "sessionKey" not in request.session:  # not in session
            cart = self.session["sessionKey"] = {
                "cartItems": {},
                "subtotal": 0,
                "count": 0,
            }

        # if user is logged in then update sessions
        if request.user.is_authenticated:

            # get myCart and id of comics present in my cart
            user = User.objects.get(id=request.user.id)
            myCart, created = LoginCart.objects.get_or_create(user=user)
            myCartItemsId = myCart.comic.all().values_list(flat=True)

            # if my cart is not empty then update my sessions
            if myCart.count is not None and myCart.count > 0:

                # get id, title, type, image, price of comics present in my cart
                cartItems, singleItem = {}, {}
                myCartItems_qs = Comic.objects.filter(
                    id__in=list(myCartItemsId)
                ).values_list(
                    "id", "title", "comic_type__comic_type_title", "main_image", "price"
                )

                # iterate throught queryset and update
                for qs in myCartItems_qs:
                    singleItem.update({"title": qs[1]})
                    singleItem.update({"type": qs[2]})
                    singleItem.update({"main_image": qs[3]})
                    singleItem.update({"price": qs[4]})

                    cartItems[str(qs[0])] = singleItem.copy()

                # update my cart subtotal and count
                subtotal = myCart.subtotal
                count = myCart.count
                cart = self.session["sessionKey"] = {
                    "cartItems": cartItems,
                    "subtotal": subtotal,
                    "count": count,
                }

        # my update sessions
        self.cart = cart
        self.save()

    def save(self):
        self.session.modified = True

    def add(self, comic, loggedInStatus, userId):

        # get comic id from comic
        comicId = comic.id

        # if that id is not in current cart then
        if str(comicId) not in self.cart["cartItems"]:

            # add to current cart
            self.cart["cartItems"][str(comicId)] = {
                "title": comic.title,
                "type": comic.comic_type.comic_type_title,
                "main_image": str(comic.main_image),
                "price": comic.price,
            }

            # update subtotal and count
            self.cart["subtotal"] += comic.price
            self.cart["count"] += 1

            # if user is loggedin then
            if loggedInStatus:

                # get user cart add that id to user cart
                user = User.objects.get(id=userId)
                myCart, created = LoginCart.objects.get_or_create(user=user)
                myCart.comic.add(comicId)

                # update subtotal and count and then save user cart object
                myCart.subtotal += comic.price
                myCart.count += 1
                myCart.save()

            # save current cart in sessions and return true
            self.save()
            return True

        # else return false
        else:
            return False

    def delete(self, comic, loggedInStatus, userId):

        # get comic id from comic
        comicId = comic.id

        # if that id is in current cart then
        if str(comicId) in self.cart["cartItems"]:

            # delete from current cart
            self.cart["cartItems"].pop(str(comicId))

            # update subtotal and count
            self.cart["subtotal"] -= comic.price
            self.cart["count"] -= 1

            # if user is loggedin then
            if loggedInStatus:

                # get user cart remove that id from user cart
                user = User.objects.get(id=userId)
                myCart, created = LoginCart.objects.get_or_create(user=user)
                myCart.comic.remove(comicId)

                # update subtotal and count and then save user cart object
                myCart.subtotal -= comic.price
                myCart.count -= 1
                myCart.save()

            # save current cart in sessions and return true
            self.save()
            return True

        # else return false
        else:
            return False

    def add_after_login(self, user):

        # if cart is not empty then
        if self.cart["count"] > 0:

            # get user cart and id of comics in cart
            myCart, created = LoginCart.objects.get_or_create(user=user)
            myCartItemsId = myCart.comic.all().values_list(flat=True)

            # iterate through current cart using comic id
            for comicId in self.cart["cartItems"].keys():
                comicPrice = self.cart["cartItems"][comicId]["price"]
                comicId = int(comicId)

                # if comic id not in user cart then
                if comicId not in myCartItemsId:

                    # add to cart
                    myCart.comic.add(comicId)

                    # update subtotal and count and then save user cart object
                    myCart.subtotal += comicPrice
                    myCart.count += 1
                    myCart.save()
