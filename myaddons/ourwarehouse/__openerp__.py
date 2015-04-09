{
    'name': 'Warehouse Application',
    'version': '0.1',
    'author': 'Group 5',
    'website': 'http://www.coding4all.com',
    'summary': 'just another project',
    'description': """
        Warehouse Module For OpenERP/odoo Project
            ==========================
        This is just another project
    """,
    'depends': ['base', 'report_webkit'],
    'data': [
        'ourwarehouse_view.xml',
        'ourwarehouse_workflow.xml',
        'security/iti_security.xml',
        'report/report.xml',
    ],

}

