<div id="addglobalExpForm" title="${_('Filter')} 01">
      <form id="globalExpForm">
        <fieldset>
            <select id='selfield' size='1'>
                <option></option>
                % for item in list:
                    <option>${item}</option>
                % endfor
            </select>
            <select id='seloperation' size='1'>
                <option></option>
                <option>=</option>
                <option>&#33;=</option>
                <option>&#60;</option>
                <option>&#62;</option>
                <option>&#60;=</option>
                <option>&#62;=</option>
            </select>
            <br>
            <label for="expressionvalue">${_('Value')}:</label>
            <textarea class="form-control" rows="2" id="expressionvalue" name="expressionvalue"></textarea>
            <br/>
        </fieldset>
      </form>
  </div>