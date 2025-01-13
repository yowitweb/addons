odoo.define('product_image_gallery.WebsiteSaleGallery', function (require) {
"use strict";

    var publicWidget = require('web.public.widget');
    var ajax = require('web.ajax');

    publicWidget.registry.WebsiteSaleGallery = publicWidget.Widget.extend({
        selector: '.oe_website_sale',
        events: {
            'click .product_detail_img': '_onClickImage',
        },

        _onClickImage: function (ev) {
            ev.preventDefault();
            ev.stopPropagation();
            var self = this;
            var src = ev.currentTarget.getAttribute('src').split('/web');
            var ImageId =  parseInt(src[1].split('/')[3]);
            var productTemplateId = parseInt(this.$el.find('input.product_template_id').val());
            var productId = parseInt(this.$el.find('input.product_id').val());
            ajax.jsonRpc('/product/get_all_images', 'call' , {
                'image_id': ImageId,
                'product_tmpl_id': productTemplateId,
                'product_id': productId
            }).then(function (modalcontent) {
                if (modalcontent.length) {
                    var $modal = $(modalcontent);
                    $modal.modal({'show': true});
                    $modal.on('hidden.bs.modal', function () {
                        $modal.remove();
                    });
                }
                else {
                    this.$el.find('#product_image_gallery').remove();
                }
            })
        },
    });
})
