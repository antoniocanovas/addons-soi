# Copyright 2021 IC - Pedro Guirao
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": " Factura soillums",
    "summary": "Reports Soillums",
    "version": "1.0.0.0.0",
    "category": "Reports",
    "author": "SerinCloud, ",
    "website": "https://ingeniriacloud.com",
    "license": "AGPL-3",
    "depends": ['account',
                'sale_management',
                ],
    "data": [
        "views/account_move_report.xml",
        "views/sale_order_report.xml",
    ],
    "installable": True,
}
