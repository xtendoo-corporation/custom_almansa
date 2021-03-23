# -- coding: utf-8 --

from odoo import api, models, fields


class AdministratorMixinRule(models.Model):
    _name = 'administrator.mixin.rule'
    _description = 'Administrator Mixin Rule'

    is_commercial = fields.Boolean(
        compute='_is_commercial',
        string="Is Commercial",
        default=lambda self: self._get_default_commercial()
    )

    def _is_commercial(self):
        self.is_commercial = self._get_default_commercial()

    def _get_default_commercial(self):
        return self.env["res.users"].has_group(
                "dji_administration.commercial_group"
            )




