from jinja2 import Template
html = """
{%- macro input_func(name, placeholder, type="text") -%}
    <input type="{{ type }}" name="{{ name }}" placeholder="{{ placeholder }}">

{%- endmacro -%}

<p>{{ input_func('firstname', 'Имя') }}</p>
<p>{{ input_func('lastname','Фамилия') }}</p>
<p>{{ input_func('address', 'Адрес') }}</p>
<p>{{ input_func('phone', 'Телефон', type="tel") }}</p>
<p>{{ input_func('email', 'Почта', type="email") }}</p>
"""


tm = Template(html)
msg = tm.render(cs=html)

print(msg)