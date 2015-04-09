<html>
    <head>
        <style type="text/css">${css}</style>
    </head>

    <body>
    <h1>${_("Product Report")}</h1>
        % for object in objects:
            product name:  ${ object.name } <br/>
            product minmum quantiy:  ${ object.min }  <br/>
            product maxmum quantiy:  ${ object.max }  <br/>
            product price :  ${ object.price }
        % endfor
    </body>
</html>
