from fabric.api import task
from fabric.api import cd
from fabric.api import env
from fabric.api import local
from fabric.api import run
from fabric.api import sudo
from fabric.api import task

from ade25.fabfiles import server
from ade25.fabfiles import project

from ade25.fabfiles import hotfix

env.use_ssh_config = True
env.forward_agent = True
env.port = '22222'
env.user = 'root'
env.hosts = ['6zu4']
env.webserver = '/opt/webserver/buildout.webserver'
env.code_root = '/opt/sites/plonesite/buildout.plonesite'
env.local_root = '/Users/cb/dev/ade25/ade25.blueprint'
env.sitename = 'plonesite'
env.code_user = 'root'
env.prod_user = 'www'


def ls():
    """ Low level configuration test """
    with cd(env.code_root):
        run('ls')


def supervisorctl(*cmd):
    """Runs an arbitrary supervisorctl command."""
    with cd(env.webserver):
        run('bin/supervisorctl ' + ' '.join(cmd))


def deploy():
    """ Deploy current master to production server """
    project.site.update()
    project.site.estart()


def deploy_full():
    """ Deploy current master to production and run buildout """
    project.site.update()
    project.site.build()
    project.site.restart()


def rebuild():
    """ Deploy current master and run full buildout """
    project.site.update()
    project.site.build_full()
    project.site.restart()
