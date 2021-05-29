# Copyright 2021 openNova - Juan Pablo Garza <juanp@opennova.com.ar>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = ["product.template"]

    @api.model
    def create(self, vals):

        if "company_ids" in vals:
            vals['company_ids'] = self.env.user.company_ids

        return super().create(vals)

