# -*- coding: utf-8 -*-

from odoo import models


class ProjectProject(models.Model):
    _inherit = 'project.project'

    def action_create_project_template(self):
        """to create project template"""
        project_template_obj = self.env['project.template']
        created_project_template = project_template_obj.create({
            'name': self.name,
            'description': self.description,
            'partner_id': self.partner_id.id,
            'label_tasks': self.label_tasks,
            'user_id': self.user_id.id,
            'privacy_visibility': self.privacy_visibility,
            'date_start': self.date_start,
            'date': self.date,
            'tag_ids': self.tag_ids.ids,
            'allow_milestones': self.allow_milestones,
            'allow_billable': self.allow_billable,
            # 'billing_type': self.billing_type,
            # 'allow_timesheets': self.allow_timesheets,
            # 'allocated_hours': self.allocated_hours,
        })
        if self.task_ids:
            for rec in self.task_ids:
                rec.create_tasks_template(created_project_template = created_project_template.id,)

