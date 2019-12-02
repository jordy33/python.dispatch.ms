
<!DOCTYPE html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js"> <!--<![endif]-->
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <title>jQeury.steps Demos</title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width">

        <link href="${tg.url('/lib/css/normalize.css')}" rel="stylesheet">
        <link href="${tg.url('/lib/css/main.css')}" rel="stylesheet">
      <link href="${tg.url('/lib/css/jquery.steps.css')}" rel="stylesheet">


       <script src="${tg.url('/lib/js/modernizr-2.6.2.min.js')}"></script>
       <script type="text/ecmascript" src="${tg.url('/lib/js/jquery-1.11.0.js')}"></script>

        <script src="${tg.url('/lib/js/jquery.cookie-1.3.1.js')}"></script>


        <script src="${tg.url('/lib/js/jquery.steps.js')}"></script>
          <script src="${tg.url('/lib/jquery-validation-1.17.0/dist/jquery.validate.js')}"></script>
      <script type="text/javascript">
      $(document).ready(function () {
          var form = $("#example-form");
          form.validate({
              errorPlacement: function errorPlacement(error, element) { element.before(error); },
              rules: {
                  confirm: {
                      equalTo: "#password"
                  }
              }
          });
          form.children("div").steps({
              headerTag: "h3",
              bodyTag: "section",
              transitionEffect: "slideLeft",
              onStepChanging: function (event, currentIndex, newIndex)
              {
                  form.validate().settings.ignore = ":disabled,:hidden";
                  return form.valid();
              },
              onFinishing: function (event, currentIndex)
              {
                  form.validate().settings.ignore = ":disabled";
                  return form.valid();
              },
              onFinished: function (event, currentIndex)
              {
                  alert("Submitted!");
              }
          });
      });
    </script>
    </head>
    <body>


<form id="example-form" action="#">
    <div>
        <h3>Account</h3>
        <section>
            <label for="userName">User name *</label>
            <input id="userName" name="userName" type="text" class="required">
            <label for="password">Password *</label>
            <input id="password" name="password" type="text" class="required">
            <label for="confirm">Confirm Password *</label>
            <input id="confirm" name="confirm" type="text" class="required">
            <p>(*) Mandatory</p>
        </section>
        <h3>Profile</h3>
        <section>
            <label for="name">First name *</label>
            <input id="name" name="name" type="text" class="required">
            <label for="surname">Last name *</label>
            <input id="surname" name="surname" type="text" class="required">
            <label for="email">Email *</label>
            <input id="email" name="email" type="text" class="required email">
            <label for="address">Address</label>
            <input id="address" name="address" type="text">
            <p>(*) Mandatory</p>
        </section>
        <h3>Hints</h3>
        <section>
            <ul>
                <li>Foo</li>
                <li>Bar</li>
                <li>Foobar</li>
            </ul>
        </section>
        <h3>Finish</h3>
        <section>
            <input id="acceptTerms" name="acceptTerms" type="checkbox" class="required"> <label for="acceptTerms">I agree with the Terms and Conditions.</label>
        </section>
    </div>
</form>

    </body>
</html>
