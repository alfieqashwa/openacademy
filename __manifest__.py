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

    # any module necessary for this one to work correctly
    'depends':['base', 'report', 'board'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/openacademy.xml',
        'views/partner.xml',
        'views/session_workflow.xml',
        'views/session_board.xml',
        'views/reports.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
