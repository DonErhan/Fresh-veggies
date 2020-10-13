# -*- coding: utf-8 -*-
# try something like
def index(): return dict(message="hello from Products.py")

response.menu = [['Home', False, URL('basic','home')],
                 ['My products', False, URL('myposts')],
                 ['Post product', False, URL('post')],
                 ['Product list', False, URL('product_list')],
                 ['Subscribe', False, URL('promotion','subscribe')],
                 ['Cart', False, URL('order')]]


@auth.requires_login()
def product_list():
    prodrows = db(db.product.avability == 'Active').select(orderby=~db.product.id)

    return locals()

    
@auth.requires_membership('Farmer')
def post():
    db.product.seller.default = session.auth.user.first_name
    form = SQLFORM(db.product).process()
    return locals()
     

@auth.requires_membership('Farmer')
def myposts():
    rows = db(db.product.created_by == session.auth.user.id).select(
        orderby=db.product.avability | ~db.product.id)
    return locals()


def update():
    record = db.product(request.args(0)) or redirect(URL('product_list'))
    form = SQLFORM(db.product, record)
    if form.process().accepted:
        response.flash = T('Record Updated')
    else:
        response.flash = T('Please complete the form.')
    return locals()




@auth.requires_login()
def order():
    record = db.product(request.args(0))
    date_ordered = str(request.now.year) + "-" + str(request.now.month) + "-" + str(request.now.day)
    user_id = session.auth.user.id
    qty = request.vars.qty
    sql = "INSERT INTO purchase (product_id, buyer_id,quantity, date_ordered) values "
    sql += "({},{},{},'{}')".format(record['id'], user_id,qty, str(date_ordered))
    r = db.executesql(sql)
    rows = db(db.purchase.user_id == session.auth.user.id).select(
        orderby=~db.purchase.id)
    return locals()

#def proc():
#    prod_dict = {}
#    product_rows = db(db.products).select()
#    for x in product_rows:
#        prod_dict[str(x.id)] = x.product_name
#    date_ordered = str(request.now.year) + "-" + str(request.now.month) + "-" + str(request.now.day)
#    qty = request.vars.qty
#    product_id = request.vars.product_id
#    user_id = session.auth.user.id
#    sql = "INSERT INTO orders (product_id, user_id, qty, status, date_ordered) values "
#    sql += "({},{},{},'{}','{}')".format(product_id, user_id, qty, "cart", str(date_ordered))
#    r = db.executesql(sql)
#    rows = db(db.orders.user_id == session.auth.user.id).select(
#        orderby=~db.orders.id)
#    return locals()
