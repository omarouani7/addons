# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
# Generated by the OpenERP plugin for Dia !
from openerp.osv import fields,osv
class netpro_provider(osv.osv):
    _name = 'netpro.provider'
    _rec_name = 'profile_id'
    _columns = {
        'ext_id': fields.integer('Ext ID'),
        'partner': fields.boolean('Partner'),
        'non_partner': fields.boolean('Non Partner'),
        'profile_id': fields.many2one('netpro.profile', 'Profile'),
        'provider_type_id': fields.many2one('netpro.provider_type', 'Provider Type'),
        'provider_level_id': fields.many2one('netpro.provider_level', 'Provider Level'),
        'claim_pic_id': fields.many2one('res.partner', 'Claim PIC'),
        'corporate_type': fields.selection([('BO', 'Both Insurance And TPA'),('IO', 'Insurance Only'),('TO', 'TPA Only')], 'Corporate Type'),
        'ip_corporate_type': fields.selection([('BO', 'Both Insurance And TPA'),('IO', 'Insurance Only'),('TO', 'TPA Only')], 'IP Corporate Type'),
        'op_corporate_type': fields.selection([('BO', 'Both Insurance And TPA'),('IO', 'Insurance Only'),('TO', 'TPA Only')], 'OP Corporate Type'),
        'state': fields.selection([('O', 'Open'),('R', 'Released'),('C', 'Close')], 'Status'),
        'effective_date': fields.date('Effective Date'),
        'expiry_date': fields.date('Expiry Date'),
        'document_number': fields.char('MOU / Document Number'),
        'signature_by': fields.char('Signature By'),
        'signature_position': fields.char('Signature Position'),
        'billing_due': fields.integer('Billing Due'),
        'payment_due': fields.integer('Payment Due'),
        'penalty_amount': fields.float('Penalty Amount'),
        'remarks_discount': fields.text('Remarks Discount'),
        'remarks': fields.text('Remarks'),
        'edc_merchant_id': fields.char('EDC Merchant ID'),
        'online_date': fields.date('On Line Date'),
        'offline_date': fields.date('Offline Date'),
        'offline_remarks': fields.text('Offline Remarks'),
        'price_effective_date': fields.date('Price Effective'),
        'general_practitioner': fields.float('General Practitioner'),
        'specialist_doctor': fields.float('Specialist Doctor'),
        'inpatient_room_ids': fields.one2many('netpro.inpatient_room', 'provider_id', 'Inpatient Room Price List', ondelete='cascade'),
        'maternity_package_ids': fields.one2many('netpro.maternity_package', 'provider_id', 'Maternity Package', ondelete='cascade'),
        'facility_ids': fields.one2many('netpro.provider_facility', 'provider_id', 'Facility', ondelete='cascade'),
        'discount_ids': fields.one2many('netpro.provider_discount', 'provider_id', 'Discount', ondelete='cascade'),
        'service_ids': fields.one2many('netpro.provider_service', 'provider_id', 'Service', ondelete='cascade'),
        'edc_ids': fields.one2many('netpro.provider_edc', 'provider_id', 'EDC', ondelete='cascade'),
        'map_ids': fields.one2many('netpro.provider_map', 'provider_id', 'Mapping', ondelete='cascade'),
        'network_ids': fields.one2many('netpro.provider_network', 'provider_id', 'Network', ondelete='cascade'),
    }
netpro_provider()

class netpro_inpatient_room(osv.osv):
    _name = 'netpro.inpatient_room'
    _columns = {
        'provider_id': fields.many2one('netpro.provider', 'Provider'),
        'room_id': fields.many2one('netpro.room', 'Room'),
        'price': fields.float('Price'),
    }
netpro_inpatient_room()

class netpro_maternity_package(osv.osv):
    _name = 'netpro.maternity_package'
    _columns = {
        'provider_id': fields.many2one('netpro.provider', 'Provider'),
        'room_id': fields.many2one('netpro.room', 'Room'),
        'price': fields.float('Price'),
        'caesar_package': fields.float('Caesar Package'),
    }
netpro_maternity_package()

class netpro_provider_facility(osv.osv):
    _name = 'netpro.provider_facility'
    _columns = {
        'provider_id': fields.many2one('netpro.provider', 'Provider'),
        'product_type_id': fields.many2one('netpro.product_type', 'Product Type'),
        'remarks': fields.text('Remarks'),
    }
netpro_provider_facility()

class netpro_provider_discount(osv.osv):
    _name = 'netpro.provider_discount'
    _columns = {
        'provider_id': fields.many2one('netpro.provider', 'Provider'),
        'discount_type': fields.selection([('CBA', 'Claim Billing Amount'), ('LOP', 'Length Of Payment in Days')], 'Discount Type'),
        'lower': fields.float('Lower'),
        'upper': fields.float('Upper'),
        'claim_payment_discount': fields.float('Claim Payment Discount'),
        'discount_start_date': fields.date('Discount Start Date'),
        'discount_end_date': fields.date('Discount End Date'),
        'remarks': fields.text('Remarks'),
    }
netpro_provider_discount()

class netpro_provider_service(osv.osv):
    _name = 'netpro.provider_service'
    _columns = {
        'provider_id': fields.many2one('netpro.provider', 'Provider'),
        'benefit_id': fields.many2one('netpro.benefit', 'Benefit'),
        'remarks': fields.text('Remarks'),
        'schedule': fields.boolean('Schedule'),
        'provider_service_detail_ids': fields.one2many('netpro.provider_service_detail', 'provider_service_id', 'Provider Service Detail', ondelete='cascade'),
    }
netpro_provider_service()

class netpro_provider_service_detail(osv.osv):
    """(NULL)"""
    _name = 'netpro.provider_service_detail'
    _columns = {
        'provider_service_id': fields.many2one('netpro.provider_service', 'Provider Service'),
        'service_item': fields.char('Service Item'),
        'price': fields.float('Price'),
        'remarks': fields.text('Remarks'),
    }
netpro_provider_service_detail()

class netpro_provider_edc(osv.osv):
    _name = 'netpro.provider_edc'
    _columns = {
        'provider_id': fields.many2one('netpro.provider', 'Provider'),
        'tid': fields.char('TID'),
        'floor': fields.integer('Floor'),
        'room': fields.char('Room'),
        'remarks': fields.text('Remarks'),
    }
netpro_provider_edc()

class netpro_provider_map(osv.osv):
    _name = 'netpro.provider_map'
    _columns = {
        'provider_id': fields.many2one('netpro.provider', 'Provider'),
        'external_mapping_id': fields.char('External Mapping ID'),
        'description': fields.text('Description'),
        'tpa_id': fields.many2one('netpro.tpa', 'TPA'),
    }
netpro_provider_map()

class netpro_provider_network(osv.osv):
    _name = 'netpro.provider_network'
    _columns = {
        'provider_id': fields.many2one('netpro.provider', 'Provider'),
        'network_id': fields.many2one('netpro.profile', 'Network ID'),
        'remarks': fields.text('Remarks'),
    }
netpro_provider_network()

