# -*- coding: utf-8 -*-
{
    'name': "Base Attachment",
    'version': '1.0',
    'category': 'Document Management',
    'summary': 'Created to help upload files for specifique module',
    'description': "",

    'author': "Mounir LAHSINI",
    'website': "https://github.com/mounirlahsini/base_attachment",
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/base_attachment.xml',
    ],
    'installable': True,
}