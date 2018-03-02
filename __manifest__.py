# -*- coding: utf-8 -*-
{
    'name': "Open Academy",
    'summary': """Manage trainings / Exercise Purpose Only""",
    'description': """
        Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,

    'author': "Alfie Qashwa",
    'website':"https://alfieqashwa.github.io",
    'category': 'Test',
    'version': '0.1',

    'depends':['base'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/templates.xml',
        'views/openacademy.xml',
        'views/partner.xml',
        'views/session_workflow.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
