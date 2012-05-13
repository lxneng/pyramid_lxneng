from pyramid.scaffolds import PyramidTemplate


class SQLAlchemyProjectTemplate(PyramidTemplate):
    _template_dir = 'lxneng_sqlalchemy'
    summary = 'Pyramid + SQLAlchemy + Jinja2 project using url dispatch'


class MongoEngineProjectTemplate(PyramidTemplate):
    _template_dir = 'lxneng_mongoengine'
    summary = 'Pyramid + MongoEngine + Jinja2 project using url dispatch'

class PluginProjectTemplate(PyramidTemplate):
	_template_dir = 'lxneng_plugin'
	summary = 'scaffold for make plugin'