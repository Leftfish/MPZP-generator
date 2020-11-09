from flask import render_template, flash, redirect, url_for
from app import app, content, content_factory
from app.forms import ChooseOptions

from random import sample

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = ChooseOptions()
    if form.validate_on_submit():
        
        person_data = [form.name, form.street, form.city]
        other_remarks = [form.green_roofs, form.green_mw11, form.green_mw12, form.green_mw14, form.green_mw15, form.green_mwu6]
        opt_data = [form.green_general] + sample(other_remarks, len(other_remarks))
        
        options = []
        for o in opt_data:
            if o.data:
                try:
                    generated = content_factory.generate_paragraph(o.id)
                    content = {'header': generated[0], 'text': generated[1]}
                    options.append(content)
                except:
                    pass
                

        return render_template("result.html", person=person_data, options=options)
    return render_template('index.html', title='Uwagi do MPZP Kobierzyńska', form=form)