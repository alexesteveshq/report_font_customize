# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models, api


class BaseDocumentLayout(models.TransientModel):
    _inherit = "base.document.layout"

    font_size = fields.Integer(related='company_id.font_size', readonly=False)

    @api.onchange('company_id')
    def _onchange_company_id(self):
        super(BaseDocumentLayout, self)._onchange_company_id()
        for wizard in self:
            wizard.font_size = wizard.company_id.font_size

    @api.depends('report_layout_id', 'logo', 'font', 'primary_color', 'secondary_color', 'report_header',
                 'report_footer', 'layout_background', 'layout_background_image', 'company_details', 'font_size')
    def _compute_preview(self):
        super(BaseDocumentLayout, self)._compute_preview()
