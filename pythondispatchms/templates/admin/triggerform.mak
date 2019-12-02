<script type="text/javascript">
$(document).ready(function() {
    var $chkboxes = $('.chkbox');
    var lastChecked = null;

    $chkboxes.click(function(e) {
        if(!lastChecked) {
            lastChecked = this;
            return;
        }

        if(e.shiftKey) {
            var start = $chkboxes.index(this);
            var end = $chkboxes.index(lastChecked);

            $chkboxes.slice(Math.min(start,end), Math.max(start,end)+ 1).prop('checked', lastChecked.checked);

        }

        lastChecked = this;
    });
});
</script>
<div id="addTriggerForm" title="${_('Filter')} 01">
      <form id="triggerExpForm">
        <fieldset>
            % for item in list:
                <input type="checkbox" id="id_chk${item["ndx"]}" class="chkbox" value=${item["value"]} name=${item["name"]} desc="test" /> ${item["name"]}<br/>
            % endfor
            <br>
            <label for="priority">${_('Priority')}:</label>
            <select id='priority' size='1'>
                <option>1</option>
                <option>2</option>
                <option>3</option>
                <option>4</option>
                <option>5</option>
            </select>
            <br/>
            <br>
            <label for="sound">${_('Sound')}:</label>
            <select id='sound' size='1'>
                <option>1</option>
                <option>2</option>
                <option>3</option>
                <option>4</option>
                <option>5</option>
            </select>
            <br/>
        </fieldset>
      </form>
  </div>