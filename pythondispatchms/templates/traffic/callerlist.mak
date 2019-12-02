<br>
<dl class="dl-horizontal">
  <table class="table table-striped">
      <thead>
        <tr>
          <th>${_('Name')}</th>
          <th>${_('Email')}</th>
          <th>${_('Phone1')}</th>
          <th>${_('Phone2')}</th>
          <th>${_('Phone3')}</th>
        </tr>
      </thead>
      <tbody>
         % for item in list:
           <tr>
             <td>${item['name']}</td>
             <td>${item['email']}</td>
             <td>${item['phone1']}</td>
             <td>${item['phone2']}</td>
             <td>${item['phone3']}</td>
           </tr>
         % endfor
      </tbody>
  </table>
</dl>
