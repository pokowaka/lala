from distutils.core import setup
setup(name='lala',
        version='0.1',
        install_requires = ['reportlab', 'progressbar2'],
        scripts=['scripts/lala'],
        package_data = {},
        package_dir={'lala': 'lala'},
        packages=['lala'],)
