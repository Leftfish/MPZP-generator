from flask import render_template
from app import app, content as static_content, content_factory
from app.forms import ChooseOptions
import urllib

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
        raw_mail = content_factory.build_raw_mail_content(static_content.TITLE_TXT, static_content.INTRO_TXT, options, person_data)
        encoded_mail = urllib.parse.quote(raw_mail)

        return render_template(
            "result.html",
            person=person_data,
            options=options,
            title=static_content.TITLE_TXT,
            intro=static_content.INTRO_TXT,
            email_body=encoded_mail,
            email_subject=urllib.parse.quote(static_content.TITLE_TXT))
    return render_template('index.html', title='Uwagi do MPZP Kobierzyńska', form=form)