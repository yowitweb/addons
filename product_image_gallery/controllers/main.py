from odoo import fields, http, _
from odoo.http import request


class ImageGallery(http.Controller):

    @http.route(['/product/get_all_images'],
                type='json', auth="public", methods=['POST'], website=True)
    def get_all_images(self, image_id, product_tmpl_id, product_id, **post):
        return request.env['ir.ui.view'].render_template(
            "product_image_gallery.modal_image_gallery", {
                'image_id': image_id,
                'product': request.env['product.template'].sudo().browse(product_tmpl_id),
                'product_variant': request.env['product.product'].sudo().browse(product_id)
            })
