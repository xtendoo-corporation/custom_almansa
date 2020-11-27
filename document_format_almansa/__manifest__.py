# -*- coding: utf-8 -*-

{
    "name": "document_format_almansa",
    "summary": """Formatos de documentos Almansa Santos""",
    "version": "12.0.1.0.0",
    "description": """Formatos de documentos Almansa Santos""",
    "author": "DDL",
    "company": "Xtendoo",
    "website": "http://www.xtendoo.com",
    "category": "Extra Tools",
    "depends": ["base", "account", "sale", "web", "stock", "product",],
    "license": "AGPL-3",
    "data": [
        # delivery
        "views/delivery/report_delivery_document.xml",
        # layout
        "views/layout/external_layout_clean.xml",
        # sale_order
        # "views/sale/report_saleorder_document.xml",
        # Purchase_order
        # "views/purchase/report_purchaseorder_document.xml",
        # Invoice
        # "views/invoice/report_invoice_document.xml",
        # Product Label
        "views/label/product_label.xml",
    ],
    "demo": [],
    "installable": True,
    "auto_install": False,
}
