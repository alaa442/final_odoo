<html>
    <head>
        <style type="text/css">${css}</style>
    </head>

    <body>

    <h1>${"تقرير المنتج"}</h1>

        % for object in objects:
اسم المنتج:
            ${ object.name } <br/>
 اقل كميه يتحملها المخزن:
            ${ object.min }  <br/>
اكبر كمية يتحملها المخزن:
            ${ object.max }  <br/>
سعر المنتج:
            ${ object.price } <br/>
الكمية المدخله من المنتج:
            ${ object.quantity } <br/>
باب المنتج:
            ${ object.category_id } <br/>
مجموعة المنتج:
            ${ object.subcategory_id } <br/>
قسم المنتج:
            ${ object.subsubcategory_id } <br/>
كود المنتج:
            ${ object.code }

        % endfor

    </body>
</html>
