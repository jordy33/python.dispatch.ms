<form id="assignForm">
    <fieldset>
        <br>
        <label for="field">${_('Field')}:&nbsp;</label>
        <input class="left" id="field" name="field" size="75" value="${field}" readonly >
        <br>
        <br>
        <label for="fieldvalue">${_('Value')}: </label>
        <input class="left" id="fieldvalue" name="field" size="75" value="${value}" readonly>
        <br>
        <br>
        <select id="selectedassigned" name="assign">
                % for item in menu:
                    <option id="${item['id']}" value="${item['id']}" ${item['selected']}>${item['name']}</option>
                % endfor
        </select>
        <br>
        <br>
        <label for="fieldvalue">${_('Multiplier')}: </label>
        <input class="left" id="multiplier" name="multiplier" size="25" value="${multiplier}">
        <br>
        <br>
        <label for="fieldvalue">${_('Unit')}&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp: </label>
        <input class="left" id="unit" name="unit" size="25" value="${unit}" >
        <br>
    </fieldset>
</form>
