# -*- coding: utf-8 -*-
"""Setup the python.dispatch.ms application"""
from __future__ import print_function, unicode_literals
import transaction
from pythondispatchms import model
from pythondispatchms.model.tables import helpComment

def bootstrap(command, conf, vars):
    """Place any commands to setup pythondispatchms here"""

    # <websetup.bootstrap.before.auth
    from sqlalchemy.exc import IntegrityError
    try:
        u = model.User()
        u.user_name = 'dispatch'
        u.display_name = 'Example manager'
        u.email_address = 'manager@somedomain.com'
        u.password = 'managepass'

        model.DBSession.add(u)

        u = model.User()
        u.user_name = 'jorge'
        u.display_name = 'Jorge Macias'
        u.email_address = 'jorge@dwim.mx'
        u.password = 'GPSc0ntr0l27'

        model.DBSession.add(u)

        u = model.User()
        u.user_name = 'isaac'
        u.display_name = 'Isaac Soto'
        u.email_address = 'maria@dwim.mx'
        u.password = 'GPSc0ntr0l27'

        model.DBSession.add(u)


        u = model.User()
        u.user_name = 'diego'
        u.display_name = 'Diego Santillan'
        u.email_address = 'diego@dwim.mx'
        u.password = '1234'

        model.DBSession.add(u)

        u = model.User()
        u.user_name = 'gerardo'
        u.display_name = 'Gerardo Jimenez'
        u.email_address = 'gerardo@dwim.mx'
        u.password = 'GPSc0ntr0l21'

        model.DBSession.add(u)

        g = model.Group()
        g.group_name = 'managers'
        g.display_name = 'Managers Group'

        g.users.append(u)

        model.DBSession.add(g)

        p = model.Permission()
        p.permission_name = 'manage'
        p.description = 'This permission gives an administrative right'
        p.groups.append(g)

        model.DBSession.add(p)

        u1 = model.User()
        u1.user_name = 'editor'
        u1.display_name = 'Example editor'
        u1.email_address = 'editor@somedomain.com'
        u1.password = 'editpass'

        model.DBSession.add(u1)
        model.DBSession.flush()

        #####
        h = helpComment()
        h.id = 1
        h.comment = ''
        model.DBSession.add(h)

        h = helpComment()
        h.id = 2
        h.comment = 'Buenos dias nos comunicamos con XXX'
        model.DBSession.add(h)

        h = helpComment()
        h.id = 3
        h.comment = 'Esta unidad ya cuenta con ticket de revisión. Seguimos pendientes de cualquier eventualidad.'
        model.DBSession.add(h)

        h = helpComment()
        h.id = 4
        h.comment = 'Esta alerta de SOS se realizo como prueba en la instalación de una unidad'
        model.DBSession.add(h)

        h = helpComment()
        h.id = 5
        h.comment = 'Alerta SOS de prueba realizada por el cliente. Todo se encuentra en orden.'
        model.DBSession.add(h)

        h = helpComment()
        h.id = 6
        h.comment = 'Falsa Alerta de Corte de Corriente debido a factores externos al equipo. Todo se encuentra en orden.'
        model.DBSession.add(h)

        h = helpComment()
        h.id = 7
        h.comment = 'Esta alerta de SOS se realizo como prueba por parte del cliente. Todo se encuentra en orden.'
        model.DBSession.add(h)

        h = helpComment()
        h.id = 8
        h.comment = 'Esta alerta se debe a que se esta instalando el equipo en la unidad.'
        model.DBSession.add(h)

        h = helpComment()
        h.id = 9
        h.comment = 'Esta unidad se encuentra en taller. Todo se encuentra en orden.'
        model.DBSession.add(h)

        h = helpComment()
        h.id = 10
        h.comment = 'Se notifico vía WhatsApp al cliente y nos responden que todo se encuentra en orden con la unidad.'
        model.DBSession.add(h)
        ####
        transaction.commit()
    except IntegrityError:
        print('Warning, there was a problem adding your auth data, '
              'it may have already been added:')
        import traceback
        print(traceback.format_exc())
        transaction.abort()
        print('Continuing with bootstrapping...')

    # <websetup.bootstrap.after.auth>
