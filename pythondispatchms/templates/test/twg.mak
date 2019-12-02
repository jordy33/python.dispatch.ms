<script type="text/javascript" src="${tg.url('/lib/tw2/dynforms.js')}" ></script>
<link rel="stylesheet" type="text/css" href="${tg.url('/lib/tw2/forms.css')}" media="all">


<style type="text/css">
</style>
<script type="text/javascript">
</script>

<body id="movieform:page"><h1>Movie Example for TW2</h1><form onsubmit="twd_blank_deleted()" action="https://dispatch.dudewhereismy.mx/test/movie_submit" method="post" enctype="multipart/form-data" id="movieform:form">
     <span class="error"></span>
    <table id="movieform">
    <tr class="odd required"  id="movieform:title:container">
        <th><label for="title">Title</label></th>
        <td >
            <input name="movieform:title" type="text" value="" id="movieform:title"/>

            <span id="movieform:title:error"></span>
        </td>
    </tr>
    <tr class="even"  id="movieform:director:container">
        <th><label for="director">Director</label></th>
        <td >
            <input name="movieform:director" type="text" id="movieform:director"/>

            <span id="movieform:director:error"></span>
        </td>
    </tr>
    <tr class="odd"  id="movieform:genres:container">
        <th><label for="genres">Genres</label></th>
        <td >
            <ul id="movieform:genres">
        <li>
            <input type="checkbox" name="movieform:genres" value="1" id="movieform:genres:0"/>
            <label for="movieform:genres:0">Action</label>
        </li>
        <li>
            <input type="checkbox" name="movieform:genres" value="2" id="movieform:genres:1"/>
            <label for="movieform:genres:1">Comedy</label>
        </li>
        <li>
            <input type="checkbox" name="movieform:genres" value="3" id="movieform:genres:2"/>
            <label for="movieform:genres:2">Romance</label>
        </li>
        <li>
            <input type="checkbox" name="movieform:genres" value="4" id="movieform:genres:3"/>
            <label for="movieform:genres:3">Sci-fi</label>
        </li>
</ul>

            <span id="movieform:genres:error"></span>
        </td>
    </tr>
    <tr class="even"  id="movieform:cast:container">
        <th><label for="cast">Cast</label></th>
        <td >
            <table id="movieform:cast">
    <tr>
        <th>Character</th><th>Actor</th><th></th>
        <td><input style="display:none" type="image" id="movieform:cast:undo" src="${tg.url('/img/undo.png')}" title="Undo" alt="Undo" onclick="twd_grow_undo(this); return false;" /></td>
    </tr>
    <tr style="display:none;" id="movieform:cast:0" class="odd">
    <td id="movieform:cast:0:character:container">
        <input name="movieform:cast:0:character" type="text" onchange="twd_grow_add(this);" id="movieform:cast:0:character"/>
    </td>
    <td id="movieform:cast:0:actor:container">
        <input name="movieform:cast:0:actor" type="text" onchange="twd_grow_add(this);" id="movieform:cast:0:actor"/>
    </td>
    <td id="movieform:cast:0:del:container">
        <input src="${tg.url('/img/del.png')}" style="display:none;" name="movieform:cast:0:del" value="" id="movieform:cast:0:del" onclick="twd_grow_del(this); return false;" alt="Delete row" type="image"/>
    </td>
    <td>
    </td>
</tr>
<tr id="movieform:cast:1" class="even">
    <td id="movieform:cast:1:character:container">
        <input name="movieform:cast:1:character" type="text" onchange="twd_grow_add(this);" id="movieform:cast:1:character"/>
    </td>
    <td id="movieform:cast:1:actor:container">
        <input name="movieform:cast:1:actor" type="text" onchange="twd_grow_add(this);" id="movieform:cast:1:actor"/>
    </td>
    <td id="movieform:cast:1:del:container">
        <input src="${tg.url('/img/del.png')}" style="display:none;" name="movieform:cast:1:del" value="" id="movieform:cast:1:del" onclick="twd_grow_del(this); return false;" alt="Delete row" type="image"/>
    </td>
    <td>
    </td>
</tr>
</table>

            <span id="movieform:cast:error"></span>
        </td>
    </tr>
    <tr class="error"><td colspan="2">
        <input name="movieform:id" type="hidden" id="movieform:id"/>
        <span id="movieform:error"></span>
    </td></tr>
</table>

		<input onclick="return twd_no_multi_submit(this);" type="submit" value="Save"/>
</form>
<script type="text/javascript">document.onkeypress = twd_suppress_enter;</script></body>
</html>
<script type="text/javascript">document.onkeypress = twd_suppress_enter;</script></body>