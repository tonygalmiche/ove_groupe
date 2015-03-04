# -*- coding: utf-8 -*-


from datetime import datetime, timedelta
import time
from openerp import pooler
from openerp.osv import fields, osv
from openerp.tools.translate import _

class ove_groupe(osv.osv):
    _name = 'ove.groupe'
    _description = u'Groupe OVE'
    _order = 'usager_id,code'

        
    _columns = {
        'code': fields.char('Code du groupe', readonly=True),
        'name': fields.char('Nom du groupe', required=True),
        'user_ids':  fields.many2many('res.users', 'ove_groups_users_rel', 'group_ove_id', 'user_id', string='Utilisateurs'),
        'comment': fields.text(u'Commentaire'),
        'usager_id': fields.many2one('is.usager', 'Usager', readonly=True),
    }
    
    def unlink(self, cr, uid, ids, context=None):
        """
        Interdire la suppression des groupes associés aux usagers
        """
        for group in self.read(cr, uid, ids, ['usager_id'], context=context):
            if group['usager_id']:
                raise osv.except_osv(_("Action invalide !"), _(u"Vous ne pouvez pas supprimer un groupe associé à un usager."))
                break
        return super(ove_groupe, self).unlink(cr, uid, ids, context=context)
        

#class ove_groupe_utilisateurs(osv.osv):
#    _name = 'ove.groupe.utilisateurs'
#    _description = 'Utilisateurs des groupes OVE'
#    _rec_name = 'user_id'
#    
#    _columns = {
#        'user_id': fields.many2one('res.users', 'Utilisateur', required=True),
#        'doc_id': fields.many2one('ove.groupe', 'Document'),
#    }

