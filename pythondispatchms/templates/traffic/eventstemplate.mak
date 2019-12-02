<script></script>
<div class="row">
  <div class="col-lg-12">
      <section class="panel">
          <header class="panel-heading">
              ${_('Crear Evento')}
          </header>
          <div class="panel-body">
              <div class="form" >
                  <form id="eventsForm" class="form-validate form-horizontal"  method="get" action="">

                  <div class="form-group ">
                      <label for="selectedpriority" class="control-label col-lg-2">${_('Priority')}</label>
                      <div class="col-lg-10">
                          <select id="selectedpriority" name="priority">
                                <option value="1">${_('Critical Priority')}   1 (${_('Red')})</option>
                                <option value="2">${_('High Priority')}      2 (${_('Orange')})</option>
                                <option value="3">${_('Medium Priority')}     3 (${_('Yellow')})</option>
                                <option value="4">${_('Medium Low Priority')} 4 (${_('Green')})</option>
                                <option value="5">${_('Low Priority')}        5 (${_('Blue')})</option>
                          </select>
                      </div>
                  </div>
                  <div class="form-group ">
                      <label for="event_id" class="control-label col-lg-2">${_('Event')}</label>
                      <div class="col-lg-10">
                              <select id="event_id" name="assign">
                                    % for item in list:
                                          <option id="${item['FIELD1']}" value="${item['FIELD1']}">${item['FIELD1']} - ${item['FIELD2']}</option>
                                    % endfor
                              </select>
                      </div>
                  </div>
                  <div class="form-group ">
                      <label for="callercomment" class="control-label col-lg-2">${_('Comment')}</label>
                      <div class="col-lg-10">
                          <textarea class="form-control " id="callercomment" name="callercomment" rows="3" required onpaste="return false;" onCopy="return false" onCut="return false"></textarea>
                      </div>
                  </div>
              </form>

              </div>
          </div>
      </section>
  </div>
</div>


