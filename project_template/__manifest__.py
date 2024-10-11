# -*- coding: utf-8 -*-

{
    'name': 'Project Template',
    'version': '18.0.1.0.0',
    'summary': 'to create project and tasks from templates',
    'description': 'creates 2 menus project template and task template and user can create project and task based on that templates',
    'depends': ['base', 'project'],
    'data': [
        'security/ir.model.access.csv',
        'views/task_template_views.xml',
        'views/project_template_views.xml',
        'views/project_task_views.xml',
        'views/project_project_views.xml',
    ],
    'installable': True,
}
