<style>
/* The container */
.container {
    display: block;
    position: relative;
    padding-left: 35px;
    margin-bottom: 12px;
    cursor: pointer;
    font-size: 22px;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
}

/* Hide the browser's default radio button */
.container input {
    position: absolute;
    opacity: 0;
    cursor: pointer;
}

/* Create a custom radio button */
.checkmark {
    position: absolute;
    top: 0;
    left: 0;
    height: 25px;
    width: 25px;
    background-color: #eee;
    border-radius: 50%;
}

/* On mouse-over, add a grey background color */
.container:hover input ~ .checkmark {
    background-color: #ccc;
}

/* When the radio button is checked, add a blue background */
.container input:checked ~ .checkmark {
    background-color: #2196F3;
}

/* Create the indicator (the dot/circle - hidden when not checked) */
.checkmark:after {
    content: "";
    position: absolute;
    display: none;
}

/* Show the indicator (dot/circle) when checked */
.container input:checked ~ .checkmark:after {
    display: block;
}

/* Style the indicator (dot/circle) */
.container .checkmark:after {
 	top: 9px;
	left: 9px;
	width: 8px;
	height: 8px;
	border-radius: 50%;
	background: white;
}
.group {
  margin-bottom: 20px;
}
.group label {
  font-size: 12px;
}
.group2 label {
  font-size: 12px;
}

</style>

<div id="usertriggerformat" class="group">
<!--

    <label class="container">Event Counter
      <input type="radio" checked="checked" name="radio">
      <span class="checkmark"></span>
    </label>
-->
    <form id="triggerassignForm">
        <label >${_('Descartar Eventos cuando el contador sea mayor a: ')}:</label>
        <br>
        <label for="fieldvalue">${_('Value')}: </label>
        <input class="left" id="fieldvalue" type="number" name="field" size="30" value="${value}">
        <br>
         <label for="fieldvalue">${_('Enviar Alerta a Venus cuando en una hora existan mas de:')}</label>
        <br>
        <label for="resetfieldvalue">${_('Value')}: </label>
        <input class="left" id="resetfieldvalue" type="number" name="field" size="30" value="${value}">

    </form>
</div>