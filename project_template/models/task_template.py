# -*- coding: utf-8 -*-

from odoo import api,fields,models

class TaskTemplate(models.Model):
    _name = 'task.template'

    name = fields.Char(string='Title', required=True)
    description = fields.Html(string='Description')
    tag_ids = fields.Many2many('project.tags', string='Tags')
    date_deadline = fields.Datetime(string='Deadline')
    user_ids = fields.Many2many('res.users', string='Assignees')
    parent_id = fields.Many2one('project.task', string='Parent Task')
    company_id = fields.Many2one('res.company', string='Company')
    email_cc = fields.Char(help='Email addresses that were in the CC of the incoming emails from this task and that are not currently linked to an existing customer.')
    sequence = fields.Integer(string='Sequence', default=10)
    self_task = fields.Many2one('task.template')
    project_id = fields.Many2one('project.project', string='Project')
    child_ids = fields.One2many('task.template','self_task')
    project_template_id = fields.Many2one('project.template')


    def create_sub_tasks(self,created_task):
        """to create sub task"""
        task_obj = self.env['project.task']
        created_subtask = task_obj.create({
            'name': self.name,
            'description': self.description,
            'tag_ids': self.tag_ids.ids,
            'date_deadline': self.date_deadline,
            'user_ids': self.user_ids.ids,
            'parent_id': created_task.id,
            'email_cc': self.email_cc,
            'sequence': self.sequence,
            'project_id': self.project_id.id
        })
        if self.child_ids:
            for rec in self.child_ids:
                rec.create_sub_tasks(created_subtask)


    def action_create_task(self,project_id=None):
        """to create task"""
        task_obj = self.env['project.task']
        created_task = task_obj.create({
            'name':self.name,
            'description':self.description,
            'tag_ids':self.tag_ids.ids,
            'date_deadline':self.date_deadline,
            'user_ids':self.user_ids.ids,
            'parent_id':self.parent_id.id,
            'email_cc':self.email_cc,
            'sequence':self.sequence,
            'project_id':project_id or self.project_id.id
        })
        if self.child_ids:
            for rec in self.child_ids:
                rec.create_sub_tasks(created_task)




