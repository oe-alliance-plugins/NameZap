from setuptools import setup
import setup_translate

pkg = 'Extensions.NameZap'
setup(name='enigma2-plugin-extensions-namezap',
       version='3.0',
       description='displays service name instead of number when zapping via number keys',
       package_dir={pkg: 'NameZap'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'maintainer.info', 'LICENSE']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
