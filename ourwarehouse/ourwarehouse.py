from openerp.osv import fields, orm


class iti_category(orm.Model):
    _name = "iti.category"

    _columns = {
        'name': fields.char("Category Name"),
    }


class iti_subcategory(orm.Model):
    _name = "iti.subcategory"

    _columns = {
        'name': fields.char("Sub Category Name"),
    }


class iti_subsubcategory(orm.Model):
    _name = "iti.subsubcategory"

    _columns = {
        'name': fields.char("Sub Sub Category Name"),
    }


class iti_warehouse(orm.Model):
    _name = "iti.warehouse"

    _columns = {
        'address': fields.char("Address"),
        # 'product_ids': fields.one2many('iti.product', string="Products"),
        'keeper_id': fields.many2one('res.users', "Keeper"),
        'manager_id': fields.many2one('res.users', "Manager"),
        'super_manager_id': fields.many2one('res.users', "Super Manager",
                                            domain="[('id','=','ref('ourwarehouse.group_iti_warehouse_supermanager')')]"),
        # 'super_manager_id': fields.many2one('res.users', "Super Manager", domain="[('id','=','ref('ourwarehouse.group_iti_warehouse_supermanager')')]"),
    }


def concate_code(self, cr, uid, ids, name, arg, context):
    result = {}
    products = self.browse(cr, uid, ids, context)
    for product in products:
        # cat = product.category_id,
        # sub = product.subcategory_id
        # sub_sub = product.subsubcategory_id
        # sub = str(product.subcategory_id)
        # sub_sub = str(product.subsubcategory_id)

        product.code = long(str(product.category_id.id) + "" +
                            str(product.subcategory_id.id) + "" +
                            str(product.subsubcategory_id.id)
        )
        result[product.id] = product.code

        # result[product.id] = str(cat) + str(sub) + str(sub_sub)

    return result


class iti_product(orm.Model):
    _name = "iti.product"

    _columns = {
        'name': fields.char("Name"),
        'min': fields.integer("Min Quantity"),
        'max': fields.integer("Max Quantity"),
        'price': fields.integer("Price"),
        'status': fields.selection(string="Status", selection=[
            ("new", "New"),
            ('used', "Used"),
            ('damaged', 'Damaged'),
        ]),
        'state': fields.selection(string="State", selection=[
            ('new', 'New'),
            ('recieved', 'Recieved'),
            ('underReview', 'Under Review'),
            ('approved', 'Approved'),
            ('keeperConfirm', 'Keeper Confirm'),
            ('managerConfirm', 'Manager Confirm'),
            ('inStock', 'In Stock'),
        ], readonly=True),
        'warehouse_id': fields.many2one("iti.warehouse", "Warehouse"),
        'category_id': fields.many2one('iti.category', 'Category'),
        'subcategory_id': fields.many2one('iti.subcategory', 'Sub category'),
        'subsubcategory_id': fields.many2one('iti.subsubcategory', 'Sub Sub category'),
        'quantity': fields.integer("Available Quantity"),
        'code': fields.function(concate_code, string='Code', type='char', store=True)
    }

    def product_new(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'new'})
        return True

    def product_recieved(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'recieved'})
        return True

    def product_underReview(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'underReview'})
        return True

    def product_approved(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'approved'})
        return True

    def product_keeper_confirm(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'keeperConfirm'})
        return True

    def product_manager_confirm(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'managerConfirm'})
        return True

    def product_in_stock(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'inStock'})
        return True