import automator
import re
attributes = ['date', 'time', 'Home or Away', 'name', 'location', 'notes', '']
html = open('demo/soccer_schedule.html', 'r').read()

automator.add(automator.get_events(html, attributes, row_class=re.compile('^seasonRowItem'), col_tag='p'))


