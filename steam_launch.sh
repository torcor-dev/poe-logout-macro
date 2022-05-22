#!/usr/bin/bash

source $HOME/dev/poe/logout-macro/venv/bin/activate
python $HOME/dev/poe/logout-macro/logout_macro.py &
"$@"
kill %1
deactivate
