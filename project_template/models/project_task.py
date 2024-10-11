# -*- coding: utf-8 -*-

from odoo import models

class ProjectTask(models.Model):
    _inherit = 'project.task'

    def create_tasks_template(self, created_project_template=None, self_task=None):
        """to create task template"""
        task_template_obj = self.env['task.template']
        created_task_template = task_template_obj.create({
            'name': self.name,
            'description': self.description,
            'tag_ids': self.tag_ids.ids,
            'date_deadline': self.date_deadline,
            'user_ids': self.user_ids.ids,
            'parent_id': self.parent_id.id,
            'email_cc': self.email_cc,
            'sequence': self.sequence,
            'project_id': self.project_id.id,
            'project_template_id': created_project_template,
            'self_task': self_task,
        })
        if self.child_ids:
            for rec in self.child_ids:
                rec.create_tasks_template(self_task = created_task_template.id)