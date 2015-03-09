from flask import render_template, flash
from app import app
from app.visit_calculator.forms import VisitCalculatorForm
import time, datetime

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))

@app.route('/', methods=['GET', 'POST'])
def index():
    form = VisitCalculatorForm()
    if form.validate_on_submit():
        flash("start_date:{}".format(form.start_date.data))
        flash("step_size:{}".format(form.step_size.data))
        flash("visit_count:{}".format(form.visit_count.data))
        flash("visit_range:{}".format(form.visit_range.data))
        visits = list()
        date_delta = datetime.timedelta(days=form.step_size.data)
        current_date = form.start_date.data
        for _ in range(0,form.visit_count.data):
            current_date += date_delta
            visit_options = list()
            for difference in range(-form.visit_range.data,form.visit_range.data + 1):
                possible_date = current_date + datetime.timedelta(days=difference)
                if possible_date > form.start_date.data:
                    visit_options.append(possible_date.strftime('%a %b %d, %Y'))
            visits.append(visit_options)
        print(visits)
        return render_template('calculation.html',
                               visits=visits)
    flash_errors(form)
    return render_template('index.html',
                           title='index',
                           form=form,
                           current_date=time.strftime('%m/%d/%Y'))
