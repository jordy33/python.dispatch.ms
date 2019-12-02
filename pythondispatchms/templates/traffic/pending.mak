% if len(pending)>0:
<br>
<h5>${_('Motivos de pendiente')}</h5>
<ul>
   % for item in pending:
    <li>${item}</li>
   % endfor
</ul>
% endif


% if len(operatorlog)>0:
<br>
<h5>${_('Historial Operador')}</h5>
<ul>
   % for item in operatorlog:
    <li>${item}</li>
   % endfor
</ul>
% endif