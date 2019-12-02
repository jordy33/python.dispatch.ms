<br>
<dl id="eventdata" class="dl-horizontal">
  % for item in list:
    <dt>${item['left']}</dt>
    <dd id="${item['id']}" name="${item['id']}">${item['right']}</dd>
  % endfor
</dl>
