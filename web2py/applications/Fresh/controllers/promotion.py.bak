def index(): return dict(message="hello from promotion.py")
# -*- coding: utf-8 -*-
# try something like
from gluon.tools import Mail

mail = Mail()
mail.settings.server = 'smtp.gmail.com: 587'     
mail.settings.sender = 'my.don.erhan@gmail.com'       
mail.settings.login = 'my.don.erhan@gmail.com:MyPythonTest123!'

@auth.requires_login()
def subscribe():
    form = SQLFORM(db.promotion)
    if form.process().accepted:
        send_email(form.vars.email)
        response.flash ='Thank you for subscribing. Please check your email'
    return dict(form = form)

# send email
def send_email(email):
    mail.send(to= email,
          subject='Welcome to Fresh Vegies!',
          message='''Lemon
Yellow lemon
Seller: Farmer2
28 MDL\KG

Peach
Pile of Peaches
Seller: Farmer2
36 MDL\KG

Watermelon
Juicy watermelon
Seller: Farmer2
8 MDL\KG

Mandarin
Mandarin Fruit
Seller: Farmer2
35 MDL\KG


Raspberry
Multianual raspberry
Seller: Farmer2
80 MDL\KG

Apples
Country apples
Seller: Farmer2
18 MDL\KG

Red grapes
Sweet grapes
Seller: Farmer2
44 MDL\KG

Strawberry
Delicious strawberry
Seller: Farmer2
60 MDL\KG

Banana
Yellow bananas
Seller: Farmer2
22 MDL\KG

Cornichon cucumber
Parisienne cornichon de bourbonne cucumber
Seller: Farmer1
35 MDL\KG

Corn
Sweet corn
Seller: Farmer1
10 MDL\KG

Cherry tomatoes
Colorful cherry tomatoes
Seller: Farmer1
35 MDL\KG

Asparagus
Healthy asparagus
Seller: Farmer1
150 MDL\KG

Brown Mushroom
Edible basidiomycete mushroom
Seller: Farmer1
55 MDL\KG

Carrot
Eco Carrot
Seller: Farmer1
18 MDL\KG

Green peas
Tasty green peas
Seller: Farmer1
15 MDL\KG

Tomatoes
Fresh tomatoes
Seller: Farmer1
25 MDL\KG''')
