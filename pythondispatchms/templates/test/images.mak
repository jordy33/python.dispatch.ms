<style>
    .container {
        width: 500px;
    }

    .container img {
        display: block;
        width: 100%;
        height: auto;
    }
</style>

<ul>
% for item in list:
    <div class="container">
  <li><img src="data:image/bmp;base64,${item}" /></li>
    </div>
% endfor
</ul>

