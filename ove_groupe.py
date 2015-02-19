# -*- coding: utf-8 -*-


from datetime import datetime, timedelta
import time
from openerp import pooler
from openerp.osv import fields, osv
from openerp.tools.translate import _

class ove_groupe(osv.osv):
    _name = 'ove.groupe'
    _description = u'Groupe OVE'

        
    _columns = {
        'name': fields.char('Nom du groupe', required=True),
        'user_ids':  fields.many2many('res.users', string='Utilisateurs'),
        'comment': fields.text(u'Commentaire'),
    }





    

#class ove_groupe_utilisateurs(osv.osv):
#    _name = 'ove.groupe.utilisateurs'
#    _description = 'Utilisateurs des groupes OVE'
#    _rec_name = 'user_id'
#    
#    _columns = {
#        'user_id': fields.many2one('res.users', 'Utilisateur', required=True),
#        'doc_id': fields.many2one('ove.groupe', 'Document'),
#    }
