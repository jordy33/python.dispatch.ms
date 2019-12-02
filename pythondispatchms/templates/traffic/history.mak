<br>
<h5>${_('Account History')}</h5>
<ul>
   % for item in list:
    <li>${item['event']}</li>
   % endfor
</ul>
