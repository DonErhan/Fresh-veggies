# -*- coding: utf-8 -*-
# try something like
def index(): return dict(message="hello from Account.py")

response.menu = [['Home', False, URL('basic','home')],
                ['Products', False, URL('Products','product_list')]]

@auth.requires_membership('Farmer')
def update():
    is_valid = False
    row = db(db.person.id == request.args(0)).select()
    for x in row:
        if x.created_by == session.auth.user.id:
            is_valid = True
    if is_valid:
        record = db.person(request.args(0)) or redirect(URL('main'))
        form = SQLFORM(db.person, record)
        if form.process().accepted:
            response.flash = T("Record Updated")
        else:
            response.flash = T("Please complete the form.")
    return locals()






@auth.requires_login()
def main():
    rows = db(db.person.created_by == session.auth.user.id).select(orderby=~db.person.id)

    return locals()


@auth.requires_login()
def edit():
    db.person.first_name.default = session.auth.user.first_name
    db.person.email.default = session.auth.user.email
    form = SQLFORM(db.person).process()
    return locals()
