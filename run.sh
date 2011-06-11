#!/bin/sh
GOOGLE_APP_ENGINE_HOME='~/google_appengine/'
export PYTHONPATH=$PYTHONPATH:$GOOGLE_APP_ENGINE_HOME
echo $PYTHONPATH:$GOOGLE_APP_ENGINE_HOME

yaml=$GOOGLE_APP_ENGINE_HOME/lib/yaml/lib
export PYTHONPATH=$PYTHONPATH:$yaml

antlr3=$GOOGLE_APP_ENGINE_HOME/lib/antlr3
export PYTHONPATH=$PYTHONPATH:$antlr3

ipaddr=$GOOGLE_APP_ENGINE_HOME/lib/ipaddr
export PYTHONPATH=$PYTHONPATH:$ipaddr

webob=$GOOGLE_APP_ENGINE_HOME/lib/webob
export PYTHONPATH=$PYTHONPATH:$webob

/usr/bin/python manage.py runserver
