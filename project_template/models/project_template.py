# -*- coding: utf-8 -*-

from odoo import _,api,fields,models


class ProjectTemplate(models.Model):
    _name = 'project.template'

    name = fields.Char(required=True)
    description = fields.Html()
    partner_id = fields.Many2one('res.partner', string='Customer')
    company_id = fields.Many2one('res.company', string='Company')
    label_tasks = fields.Char(string='Use Tasks as', default=lambda s: _('Tasks'), translate=True,
                              help="Name used to refer to the tasks of your project e.g. tasks, tickets, sprints, etc...")
    user_id = fields.Many2one('res.users', string='Project Manager', default=lambda self: self.env.user, tracking=True)
    privacy_visibility = fields.Selection([
        ('followers', 'Invited internal users (private)'),
        ('employees', 'All internal users'),
        ('portal', 'Invited portal users and all internal users (public)'),
    ],
        string='Visibility', required=True,
        default='portal',
        help="People to whom this project and its tasks will be visible.\n\n"
             "- Invited internal users: when following a project, internal users will get access to all of its tasks without distinction. "
             "Otherwise, they will only get access to the specific tasks they are following.\n "
             "A user with the project > administrator access right level can still access this project and its tasks, even if they are not explicitly part of the followers.\n\n"
             "- All internal users: all internal users can access the project and all of its tasks without distinction.\n\n"
             "- Invited portal users and all internal users: all internal users can access the project and all of its tasks without distinction.\n"
             "When following a project, portal users will get access to all of its tasks without distinction. Otherwise, they will only get access to the specific tasks they are following.\n\n"
             "When a project is shared in read-only, the portal user is redirected to their portal. They can view the tasks, but not edit them.\n"
             "When a project is shared in edit, the portal user is redirected to the kanban and list views of the tasks. They can modify a selected number of fields on the tasks.\n\n"
             "In any case, an internal user with no project access rights can still access a task, "
             "provided that they are given the corresponding URL (and that they are part of the followers if the project is private).")
    date_start = fields.Date(string='Start Date')
    date = fields.Date(string='Expiration Date',
                       help="Date on which this project ends. The timeframe defined on the project is taken into account when viewing its planning.")
    tag_ids = fields.Many2many('project.tags', string='Tags')
    allow_milestones = fields.Boolean('Milestones')
    allow_billable = fields.Boolean("Billable")
    # billing_type = fields.Selection(
    #     selection=[
    #         ('not_billable', 'not billable'),
    #         ('manually', 'billed manually'),
    #     ],
    #     default='not_billable',
    # )
    # allow_timesheets = fields.Boolean(
    #     "Timesheets",default=True)
    allocated_hours = fields.Float(string='Allocated Hours')
    access_instruction_message = fields.Char('Access Instruction Message', compute='_compute_access_instruction_message')
    task_ids = fields.One2many('task.template','project_template_id')
    _sql_constraints = [
        ('project_date_greater', 'check(date >= date_start)', "The project's start date must be before its end date.")
    ]

    @api.depends('privacy_visibility')
    def _compute_access_instruction_message(self):
        """to show instruction under privacy_visibility field"""
        for project in self:
            if project.privacy_visibility == 'portal':
                project.access_instruction_message = _(
                    'Grant portal users access to your project or tasks by adding them as followers. Customers automatically get access to their tasks in their portal.')
            elif project.privacy_visibility == 'followers':
                project.access_instruction_message = _(
                    'Grant employees access to your project or tasks by adding them as followers. Employees automatically get access to the tasks they are assigned to.')
            elif project.privacy_visibility == 'employees':
                project.access_instruction_message = 'Portal users will be removed from the followers of the project and its tasks.'
            else:
                project.access_instruction_message = ''


    def action_create_project(self):
        """to create a project"""
        project_obj = self.env['project.project']
        created_project = project_obj.create({
            'name':self.name,
            'description':self.description,
            'partner_id':self.partner_id.id,
            'label_tasks':self.label_tasks,
            'user_id':self.user_id.id,
            'privacy_visibility':self.privacy_visibility,
            'date_start':self.date_start,
            'date':self.date,
            'tag_ids':self.tag_ids.ids,
            'allow_milestones':self.allow_milestones,
            'allow_billable':self.allow_billable,
            # 'billing_type':self.billing_type,
            # 'allow_timesheets':self.allow_timesheets,
            # 'allocated_hours':self.allocated_hours,
        })
        if self.task_ids:
            for rec in self.task_ids:
                rec.action_create_task(created_project.id)
